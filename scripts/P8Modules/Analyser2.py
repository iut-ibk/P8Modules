from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pydynamind import *
from Analyser2_Gui import *
import ntpath

class AnalyserModule(Module):
	def __init__(self):
		Module.__init__(self)

		self.simulation = View("SimulationData",COMPONENT,READ)
		self.simulation.getAttribute("msfFilename")
		self.simulation.getAttribute("SEIurb")
		self.simulation.getAttribute("SEIwsud")	
		self.simulation.getAttribute("NoY")
		self.simulation.getAttribute("alpha")
		#self.simulation.getAttribute("MusicFileNo")

		datastream = []
		datastream.append(self.simulation)
		self.addData("City",datastream)
	def run(self):
		city = self.getData("City")
		strvec = city.getUUIDsOfComponentsInView(self.simulation)
		tmpvec = []
		self.SEIwsud = 0.0
		self.SEIurb = 0.0
		self.musicfile = ""
		for value in strvec:
			simuData = city.getComponent(value)
			urb = simuData.getAttribute("SEIurb").getDouble()
			wsud = simuData.getAttribute("SEIwsud").getDouble()
			stringname = simuData.getAttribute("msfFilename").getString()
			#with musicfileno
			#run = simuAttr.getAttribute("MusicFileNo").getDouble()
			#if (run != 0):
				#self.musicnr.append(int(run))
			if (stringname != ""):
				self.musicfile = stringname
			if (urb != 0):
				self.SEIurb = urb
			if(wsud != 0):
				self.SEIwsud = wsud
			if(simuData.getAttribute("NoY").getDouble() != 0):
				self.NoY = simuData.getAttribute("NoY").getDouble()
			if(simuData.getAttribute("alpha").getDouble() != 0):
				self.alpha = simuData.getAttribute("alpha").getDouble()
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		self.TPRFile = workpath + "TPRtable.txt"
		self.EBRFile = workpath + "EBRtable.txt"
		self.UtilFile = workpath + "UtilTable.txt"
		self.summaryFile = workpath + "AnalyzerSummary.csv"	

		self.calcEBR(workpath)
		self.calcTPR(workpath)
		#self.calcUTIL(workpath)
		self.calcSEI(workpath)
	def createInputDialog(self):
		form = Analyser2_Gui(self, QApplication.activeWindow())
		form.exec_()
		return True 
	def calcEBR(self,workpath):
		output = []
		#reading output form ebr module
		if(os.path.exists(self.EBRFile)):
			f = open(self.EBRFile,'r')
			for line in f:
				linearr = line.strip('\n').split(',')
				tmp = (linearr[5],round(float(linearr[1])),round(float(linearr[2])),round(float(linearr[3])),round(float(linearr[4])))
				output.append(tmp)
			#writing information into summary file
			f = open(self.summaryFile, 'w')
			f.write("------------ Analyzer Summary ------------\n\n")
			f.write(" EB: Stream Hydrology and Water Quality\nRealisation,Frequency of runoff(days/year),Proportion of total volume reduction,Proportion of iltered flows,Water Quality\n")

			for line in output:
				tmp = str(line)
				tmp = tmp.replace("(","")
				tmp = tmp.replace("]","")
				tmp = tmp.replace("[","")
				tmp = tmp.replace(")","")
				f.write(str(tmp) + "\n")
			f.write("\n------------------------------------------\n\n")
			f.close()
		else:
			print "no EB file found"
	def calcTPR(self,workpath):
		filename = workpath + "Perf_TTE.txt"
		if(os.path.exists(filename)):
			f = open(filename,'r')
			text = shlex.shlex(f.read(),posix = True)
			text.whitespace = ','
			text.whitespace += '\n'
			text.whitespace_split = True
			liste = list(text)
			output = []
			line1 = (round(float(liste[7])),round(float(liste[11])),round(float(liste[15])),round(float(liste[19])))
			f.close()
			i = 1
			if os.path.exists(self.TPRFile):
				f = open(self.TPRFile,'r')
				for line in f:
					linearr = line.strip('\n').split(',')
					tmp = (linearr[0],round(float(linearr[1])),round(float(linearr[2])),round(float(linearr[3])),round(float(linearr[4])))
					output.append(tmp)
					i = i + 1
				f.close()
			output.append([ntpath.basename(self.musicfile),line1[0],line1[1],line1[2],line1[3]])	
			#writing ouput in summary	
			if(os.path.exists(self.summaryFile)):
				f = open(self.summaryFile, 'a+')
				f.write(" TP: Treatment Performance\nRealisation,Flow(ML/year),Total Suspended Solids(kg/year), Total Phosphorus (kg/year),Total Nitrogen(kg/year)\n")
			else:
				f = open(self.summaryFile, 'w')
				f.write("------------ Analyzer Summary ------------\n\n")
				f.write(" TP: Treatment Performance\nRealisation,Flow(ML/year),Total Suspended Solids(kg/year), Total Phosphorus (kg/year),Total Nitrogen(kg/year)\n")
			for line in output:
				tmp = str(line)
				tmp = tmp.replace("(","")
				tmp = tmp.replace("]","")
				tmp = tmp.replace("[","")
				tmp = tmp.replace(")","")
				f.write(str(tmp) + "\n")
			f.write("\n------------------------------------------\n\n")
			f.close()
		else:
			print "no TP file found"
	def calcUTIL(self,workPath):
		if(os.path.exists(self.UtilFile)):
			ResultVec = self.loadUtilFile()
		if(os.path.exists(workpath + "UB_BasinStrategy No 1-" + str(self.module.musicnr) + ".csv")):
			f = open(workpath + "UB_BasinStrategy No 1-" + str(self.module.musicnr) + ".csv",'r')
			j = 0
			serviceVec = []
			lines = []
			BFsum = 0
			PBsum = 0
			ISsum = 0
			WSURsum = 0
			SWsum = 0
			for line in f:
				j = j + 1
				text = shlex.shlex(line,posix = False)
				text.whitespace += ','
				text.whitespace_split = True
				liste = list(text)
				if (j >11):
					lines.append(liste)
			for k in range(len(lines)):
				serviceVec.append((lines[k][1],float(lines[k][3])*float(lines[k][4])*float(lines[k][5])/100))
				serviceVec.append((lines[k][6],float(lines[k][8])))
				serviceVec.append((lines[k][9],float(lines[k][11])))
				serviceVec.append((lines[k][12],float(lines[k][14])))
			for k in range(len(serviceVec)):
				if (serviceVec[k][0] == "BF"):
					BFsum += serviceVec[k][1]
				elif (serviceVec[k][0] == "PB"):
					PBsum += serviceVec[k][1]
				elif (serviceVec[k][0] == "IS"):
					ISsum += serviceVec[k][1]
				elif (serviceVec[k][0] == "WSUR"):
					WSURsum += serviceVec[k][1]
				elif (serviceVec[k][0] == "SW"):
					SWsum += serviceVec[k][1]
			allsums = BFsum + PBsum + ISsum + WSURsum + SWsum
			BF = BFsum *100/allsums
			PB = PBsum *100/allsums
			IS = ISsum *100/allsums
			WSUR = WSURsum *100/allsums
			SW = SWsum *100/allsums
			print BF
			print PB
			print IS
			print WSUR
			print SW
			ResultVec.append((self.module.musicnr,allsums*100,BF,PB,IS,WSUR,SW))
			BFvec =[]
			PBvec = []
			ISvec = []
			WSURvec = []
			SWvec = []
			
			BfFlag = False
			PbFlag = False
			IsFlag = False
			WsurFlag = False
			SwFlag = False
			print ResultVec
			for i in range(len(ResultVec)):
				BFvec.append(ResultVec[i][2])
				PBvec.append(ResultVec[i][3])
				ISvec.append(ResultVec[i][4])
				WSURvec.append(ResultVec[i][5])
				SWvec.append(ResultVec[i][6])
				if(ResultVec[i][2] > 0):
					BfFlag = True
				if(ResultVec[i][3] > 0):
					PbFlag = True
				if(ResultVec[i][4] > 0):
					IsFlag = True
				if(ResultVec[i][5] > 0):
					WsurFlag = True
				if(ResultVec[i][6] > 0):
					SwFlag = True
			ind = np.arange(len(ResultVec))
			width = 0.9 / len(ResultVec)
			BFvec = np.array(BFvec)
			PBvec = np.array(PBvec)
			ISvec = np.array(ISvec)
			WSURvec = np.array(WSURvec)
			SWvec = np.array(SWvec)
			
			BFstring = " "
			PBstring = " "
			ISstring = " "
			WSURstring = " "
			SWstring = " "
			for i in range(len(BFvec)):
				if (BfFlag):
					BFstring += str('%.2f' % BFvec[i]) + "%,"
				if(PbFlag):
					PBstring += str('%.2f' % PBvec[i]) + "%,"
				if(IsFlag):
					ISstring += str('%.2f' % ISvec[i]) + "%,"
				if(WsurFlag):
					WSURstring += str('%.2f' % WSURvec[i]) + "%,"
				if(SwFlag):
					SWstring += str('%.2f' % SWvec[i]) + "%,"
			outtxt = ""
			if (BfFlag):
				outtxt += "BF-Biofiltration System," + BFstring + "\n"
			if(PbFlag):
				outtxt += "PB-Ponds & Basins," + PBstring + "\n"
			if (IsFlag):
				outtxt+= "Infiltration System," + ISstring + "\n"
			if(WsurFlag):
				outtxt += "WSUR - Surface Wetland," + WSURstring + "\n"
			if (SwFlag):
				outtxt += "Swale," + SWstring + "\n"
			if(os.path.exists(self.summaryFile)):
				f = open(self.summaryFile, 'a+')
				f.write(" UTIL: \n\n")
			else:
				f = open(self.summaryFile, 'w')
				f.write("------------ Analyzer Summary ------------\n\n")
				f.write(" UTIL: \n\n")
			f.write(str(outtxt) + "\n")
			f.write("\n------------------------------------------\n\n")
			f.close()
		else:
			print "Util file not found"

	def loadUtilFile(self):
		vec = []
		f = open(self.UtilFile,"r")
		for line in f:
			linearr = line.strip('\n').split(',')
			tmpbar = (round(float(linearr[0]),2),round(float(linearr[1]),2),round(float(linearr[2]),2),round(float(linearr[3]),2),round(float(linearr[4]),2),round(float(linearr[5]),2),round(float(linearr[6]),2))
			vec.append(tmpbar)
		f.close()
		return vec
	def calcSEI(self,workpath):
		urbs = []
		wsuds = []
		names = []
		if os.path.exists(workpath + "SEItable.txt"):
			f = open(workpath + "SEItable.txt")
			for line in f:
				linearr = line.strip('\n').split(',')
				urbs.append(round(float(linearr[2])))
				wsuds.append(round(float(linearr[3])))
				names.append(str(linearr[0]))
			f.close()
			if(os.path.exists(self.summaryFile)):
				out = open(self.summaryFile, 'a+')
				out.write(" SEI: Stream Erosion Index\nRealisation, SEI urbanised, SEI WSUD\n")
			else:
				out = open(self.summaryFile, 'w')
				out.write("------------ Analyzer Summary ------------\n\n")
				out.write(" SEI: Stream Erosion Index\nRealisation, SEI urbanised, SEI WSUD\n")
			for i in range(len(urbs)):
				out.write(str(names[i]) + "," + str(urbs[i]) + "," + str(wsuds[i]) + "\n")
			out.write("\n")
			out.write("\n------------------------------------------\n\n")
			out.close()
		else:
			print "No SEI files found"
