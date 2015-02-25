from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pydynamind import *
from Analyser2_Gui import *
import ntpath
import Tkinter, tkFileDialog

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
		self.useUB = ""
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
			if(simuData.getAttribute("useUB").getString() != ""):
				self.useUB = simuData.getAttribute("useUB").getString()
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
		print "useUB: " + str(self.useUB)
		if(self.useUB == "1"):
			self.calcUTIL(workpath)
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
				#f.write("1,"+str(self.FF[0])+","+str(self.VR[0])+","+str(self.FV[0])+","+str(self.WQ[0])+"," + ntpath.basename(realstring) + "," + str(FreqUntreated) + "," + str(self.FrequencyRunoffDays) + "," + str(self.VolumeReduction) + "," + str(FvForest) + "," + str(FvPasture) + ","+ str(self.FreqPredev) + "," + str(self.cin) + "," + str(self.getConsiderFluxes())+"\n")
				#f.write(str(self.getConsiderFluxes()) + "," +  str(FvPasture) + "," +str(self.cin) + "," + str(self.FF[0])+","+str(self.VR[0])+","+str(self.FV[0])+","+ "," + str(tss) + "," + str(tp) + "," + str(tn) + "\n")	
				#													4																							9															13
				#(nr+1) self.FF[0]) (self.VR[0]) (self.FV[0]) (self.WQ[0]) (realstring)  (FreqUntreated) (self.FrequencyRunoffDays) (self.VolumeReduction) (FvForest) (FvPasture) (self.FreqPredev) (self.cin) (self.getConsiderFluxes()) (tss) (tp) (tn)

				tmp = (linearr[13],int(linearr[11]),float(linearr[12]),round(float(linearr[1]),2),round(float(linearr[2]),2),round(float(linearr[3]),2),round(float(linearr[14]),2),round(float(linearr[15]),2),round(float(linearr[16]),2))
				output.append(tmp)
			#writing information into summary file
			f = open(self.summaryFile, 'w')
			f.write("------------ Analyzer Summary ------------\n\n")
			f.write(" EB: Stream Hydrology and Water Quality\nConsidered infiltration fluxes?,Number of runoff days in the natural catchment (days/year), Baseflow rate allowed in the WSUD catchment(m3/s), Frequency of Runoff Days (days/year), Proportion of Total Volume Reduction (%), Proportion of Filtered Flow Volume (%), TSS mean concentration (mg/L), TP mean concentration (mg/L), TN mean concentration (mg/L)\n")

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
				f.write(" TP: Treatment Performance (Load reduction)\nRealisation,Flow(ML/year),Total Suspended Solids(kg/year), Total Phosphorus (kg/year),Total Nitrogen(kg/year)\n")
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
		ResultVec = []
		if(os.path.exists(self.UtilFile)):
			ResultVec = self.loadUtilFile()
		dbfFile = ""
		dbfFile = self.findDBFfile()
		if(dbfFile != ""):
			print dbfFile
			simnr = 0
			simnr = self.getSimNr(self.musicfile)
			print simnr
			tmpvec = self.readUtilDataFromDBF(dbfFile,simnr)
																#zeros are		IS          SW
			ResultVec.append((ntpath.basename(self.musicfile),tmpvec[0],tmpvec[2],tmpvec[3],0,tmpvec[1],0))
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
			self.writeUtilFile(ResultVec)
		else:
			print "Util file not found"

	def loadUtilFile(self):
		vec = []
		f = open(self.UtilFile,"r")
		for line in f:
			linearr = line.strip('\n').split(',')
			tmpbar = (linearr[0],round(float(linearr[1]),2),round(float(linearr[2]),2),round(float(linearr[3]),2),round(float(linearr[4]),2),round(float(linearr[5]),2),round(float(linearr[6]),2))
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

	def getClassName(self):
		return "Analyser"
	def getFileName(self):
		return "Scenario Simulation and Assessment"
	def writeUtilFile(self,vec):
		f = open(self.UtilFile,"w")
		for i in range(len(vec)):
			f.write(str(vec[i][0])+","+str(vec[i][1])+","+str(vec[i][2])+","+str(vec[i][3])+","+str(vec[i][4])+","+str(vec[i][5])+","+str(vec[i][6])+"\n")
		f.close()
	def findDBFfile(self):
		root = Tkinter.Tk()
		root.withdraw()
		self.file_opt = options = {}
		options['defaultextension'] = '.dbf'
		options['filetypes'] = [('dbf files', '.dbf')]
		options['title'] = 'Please select the DBF file to load for Utilisation calculations'
		file_path = tkFileDialog.askopenfilename(**self.file_opt)
		return file_path
	def getSimNr(self,filename):
		splitfile = filename.split("-")
		return splitfile[2]
	def readUtilDataFromDBF(self,dbfFile, simnr):
		total = 0.0
		wsur = 0.0
		bf = 0.0
		pb = 0.0
		f = open(dbfFile, "r")
		for line in f:
			print line
			linearr = line.strip("\n").split("\t")
			#check for current sim nr
			if(linearr[3] == simnr):
				total += float(linearr[13])
				if(linearr[6] == "WSUR"):
					wsur += float(linearr[13])
				if(linearr[6] == "BF"):
					bf += float(linearr[13])
				if(linearr[6] == "PB"):
					pb += float(linearr[13])
			else:
				continue
		wsur /= total
		bf /= total
		pb /= total
		print "wsur " + str(wsur)
		print "bf " + str(bf)
		print "pb " + str(pb)
		print "sum " + str(wsur+bf+pb)
		recVec = []
		recVec.append(total)
		recVec.append(wsur)
		recVec.append(bf)
		recVec.append(pb)
		return recVec
