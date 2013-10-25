from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from pydynamind import *
from ReadTableSecondary_Gui2 import *
import shlex
import numpy as np
import os.path
from subprocess import call
import ubeats_music_interface as umusic
import platform
import ntpath


class StreamHydrologyandWaterquality(Module):
	def __init__(self):
		Module.__init__(self)

		self.createParameter("FileName", FILENAME,"")
		self.FileName = ""
		self.createParameter("SimulationCity",DOUBLE,"")
		self.SimulationCity = 2

		#Views
		self.simulation = View("SimulationData",COMPONENT,READ)
		self.simulation.getAttribute("msfFilename")
		self.simulation.addAttribute("MusicFileNo")
		self.simulation.addAttribute("SEIurb")
		self.simulation.addAttribute("SEIwsud")	
		self.simulation.addAttribute("NoY")
		self.simulation.addAttribute("alpha")

		self.PastureY = [169.46, 192.602, 223.436, 246.61, 269.752, 292.894, 323.761, 339.21, 370.077, 393.219, 416.393, 439.535, 462.677, 485.851, 508.993, 532.168, 555.31, 578.451, 601.626, 624.768, 655.602, 678.776, 701.918, 725.06, 748.234, 779.069, 802.211, 825.353, 856.187, 879.361, 902.503, 933.305, 956.447, 987.314, 1010.46, 1041.29, 1064.43, 1087.57, 1118.41, 1141.55, 1172.38, 1195.53, 1226.36, 1249.47, 1280.31, 1311.14, 1334.28, 1365.08, 1388.23, 1419.03, 1442.14, 1472.97, 1503.77, 1534.61, 1557.72, 1588.52, 1619.35, 1650.16, 1673.27, 1704.07, 1734.87, 1758.01, 1788.81, 1819.62, 1842.73, 1873.53, 1896.64, 1927.44, 1958.24, 1989.08, 2019.85, 2042.95, 2073.76, 2104.56, 2135.36, 2166.13, 2196.93, 2220.04, 2250.88, 2281.65, 2304.76, 2335.56, 2366.36, 2397.16, 2420.27, 2451.04, 2481.84, 2512.65, 2543.45, 2574.25, 2597.36, 2628.13, 2658.93, 2689.73, 2720.54, 2751.34, 2774.41, 2805.22, 2836.02, 2866.79, 2897.59, 2928.36, 2951.44, 2982.27, 3013.04, 3036.15, 3066.92, 3097.72, 3128.49, 3159.26, 3190.06, 3220.83, 3251.64, 3282.41, 3305.52, 3336.29, 3359.36, 3390.16, 3420.93, 3444.04, 3474.85, 3497.92, 3528.69]
		self.PastureX = [0.0297678, 0.0382198, 0.0466879, 0.0593416, 0.0677936, 0.0762456, 0.0889155, 0.0973513, 0.110021, 0.118473, 0.131127, 0.139579, 0.148031, 0.160685, 0.169137, 0.18179, 0.190242, 0.198694, 0.211348, 0.2198, 0.228268, 0.240922, 0.249374, 0.257826, 0.270479, 0.278948, 0.2874, 0.295852, 0.30432, 0.316973, 0.325425, 0.329692, 0.338144, 0.350814, 0.359266, 0.367734, 0.376186, 0.384638, 0.393106, 0.401558, 0.410026, 0.418478, 0.426946, 0.431196, 0.439665, 0.448133, 0.456585, 0.460851, 0.469303, 0.473569, 0.47782, 0.486288, 0.490554, 0.499022, 0.503273, 0.507539, 0.516007, 0.520273, 0.524524, 0.52879, 0.533056, 0.541508, 0.545775, 0.550041, 0.554291, 0.558558, 0.562808, 0.567074, 0.571341, 0.579809, 0.579874, 0.584124, 0.58839, 0.592657, 0.596923, 0.596988, 0.601254, 0.605504, 0.613972, 0.614037, 0.618287, 0.622554, 0.62682, 0.631086, 0.635337, 0.635401, 0.639668, 0.643934, 0.648201, 0.652467, 0.656717, 0.656782, 0.661048, 0.665315, 0.669581, 0.673847, 0.673896, 0.678162, 0.682429, 0.682493, 0.68676, 0.686824, 0.686873, 0.695341, 0.695406, 0.699656, 0.69972, 0.703987, 0.704051, 0.704116, 0.708382, 0.708447, 0.712714, 0.712778, 0.717028, 0.717093, 0.717142, 0.721408, 0.721473, 0.725723, 0.729989, 0.730038, 0.730102]
		self.ForestY = [376.2, 376.2, 406.91, 429.942, 460.653, 491.363, 522.073, 545.106, 575.816, 606.526, 637.236, 660.269, 690.979, 721.689, 752.399, 775.432, 806.142, 836.852, 859.885, 890.595, 913.628, 944.338, 975.048, 998.081, 1021.11, 1051.82, 1074.86, 1105.57, 1128.6, 1159.31, 1190.02, 1213.05, 1243.76, 1266.79, 1297.5, 1328.21, 1351.25, 1381.96, 1412.67, 1435.7, 1466.41, 1497.12, 1520.15, 1550.86, 1581.57, 1612.28, 1635.32, 1666.03, 1696.74, 1727.45, 1750.48, 1781.19, 1811.9, 1842.61, 1865.64, 1896.35, 1927.06, 1957.77, 1980.81, 2011.52, 2042.23, 2072.94, 2095.97, 2126.68, 2157.39, 2188.1, 2211.13, 2241.84, 2272.55, 2303.26, 2326.3, 2357.01, 2387.72, 2418.43, 2449.14, 2472.17, 2502.88, 2533.59, 2564.3, 2595.01, 2618.04, 2648.75, 2679.46, 2710.17, 2740.88, 2763.92, 2794.63, 2825.34, 2856.05, 2886.76, 2909.79, 2940.5, 2971.21, 3001.92, 3032.63, 3063.34, 3086.37, 3117.08, 3147.79, 3178.5, 3209.21, 3239.92, 3270.63, 3293.67, 3324.38, 3355.09, 3385.8, 3416.51, 3447.22]
		self.ForestX = [0.0172019, 0.0214358, 0.0256617, 0.0340973, 0.0341296, 0.0425652, 0.0467911, 0.051025, 0.0594606, 0.0636946, 0.0679205, 0.0763561, 0.08059, 0.0848239, 0.0932515, 0.0974854, 0.105921, 0.110147, 0.118583, 0.12701, 0.131244, 0.135478, 0.143906, 0.14393, 0.152365, 0.160793, 0.165027, 0.173454, 0.18189, 0.190326, 0.194552, 0.202987, 0.211415, 0.215649, 0.224084, 0.22831, 0.236746, 0.245181, 0.249407, 0.257843, 0.266278, 0.270504, 0.27894, 0.283174, 0.287408, 0.295835, 0.300069, 0.304303, 0.308537, 0.316965, 0.321199, 0.325433, 0.329667, 0.338094, 0.342328, 0.350764, 0.354998, 0.359224, 0.363457, 0.367691, 0.371925, 0.376151, 0.384587, 0.388821, 0.393055, 0.397281, 0.405716, 0.40995, 0.414184, 0.422612, 0.426846, 0.43108, 0.435313, 0.439547, 0.443773, 0.448007, 0.452241, 0.456475, 0.460709, 0.464935, 0.469169, 0.473403, 0.477637, 0.477669, 0.481895, 0.486129, 0.490363, 0.490395, 0.498831, 0.503057, 0.50729, 0.507323, 0.511557, 0.519992, 0.520025, 0.52425, 0.528484, 0.532718, 0.536952, 0.541186, 0.54542, 0.545452, 0.549678, 0.553912, 0.558146, 0.56238, 0.562412, 0.566646, 0.570872]
		datastream =[]
		datastream.append(self.simulation)
		self.addData("City",datastream)

	def run(self):
		settings = QSettings()
		workpath = settings.value("workPath").toString()
		workpath += "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		city = self.getData("City")
		strvec = city.getUUIDsOfComponentsInView(self.simulation)
		''' version with musicnr'''
		for value in strvec:
			simuData = city.getComponent(value)
			stringname = simuData.getAttribute("msfFilename").getString()
			if (stringname != ""):
				realstring = stringname
			'''
			musicNo = int(simuData.getAttribute("MusicFileNo").getDouble())
			if (musicNo != 0):
				musicnr = musicNo
			'''
		'''
		self.writeBatFileFromNr(musicnr)
		self.writeMusicConfigFileSecondaryFromNr(musicnr)
		'''
		#version with musicfile
		for value in strvec:
			simuAttr = city.getComponent(value)
			stringname = simuAttr.getAttribute("msfFilename").getString()
			if (stringname != ""):
				realstring = stringname
		self.writeBatFileFromFile(realstring)
		self.writeMusicConfigFileSecondaryFromFile(realstring)
		areas = self.convertToSecondaryMusic(realstring)
		imparea = areas[0] 		#total impervious area
		totalarea = areas[1] 	#total area
		print "Music is running ... "
		if(platform.system() != "Linux"):
			call(["RunMusicSecondary.bat", ""])
		print "Music Done."
		print "imparea: " + str(imparea)
		EIF = imparea / totalarea
		print "EIF: " + str(EIF)
		self.FF = []
		self.VR = [] 
		self.WQ = [] 
		self.FV = []
		self.tmpFile = workpath + "EBRtable.txt"

		if self.SimulationCity == 0:
			AnnualRain = 520
		elif self.SimulationCity == 1:
			AnnualRain = 1200
		elif self.SimulationCity == 2:
			AnnualRain = 650
		elif self.SimulationCity == 3:
			AnnualRain = 790
		elif self.SimulationCity == 4:
			AnnualRain = 1175

		'''version with musicnr
		list1 = self.readFileToList("PredevelopRunoffFrequency"+str(musicnr)+".TXT")
		list2 = self.readFileToList("UntreatedRunoffFrequency"+str(musicnr)+".TXT")
		list3 = self.readFileToList("TreatedRunoffFrequency"+str(musicnr)+".TXT")
		list4 = self.readFileToList("ETandRe-useFluxes"+str(musicnr)+".TXT")
		list5 = self.readFileToList("PredevelopTotalRunoff"+str(musicnr)+".TXT")
		list6 = self.readFileToList("Exfiltration"+str(musicnr)+".TXT")
		list7 = self.readFileToList("WQ"+str(musicnr)+".TXT")
		list8 = self.readFileToList("PredevelopBaseflowFrequency"+str(musicnr)+".TXT")
		'''
		#version with music file
		list1 = self.readFileToList("PredevelopRunoffFrequency.TXT")
		list2 = self.readFileToList("UntreatedRunoffFrequency.TXT")
		list3 = self.readFileToList("TreatedRunoffFrequency.TXT")
		list4 = self.readFileToList("ETandRe-useFluxes.TXT")
		list5 = self.readFileToList("PredevelopTotalRunoff.TXT")
		list6 = self.readFileToList("Exfiltration.TXT")
		list7 = self.readFileToList("WQ.TXT")
		list8 = self.readFileToList("PredevelopBaseflowFrequency.TXT")

		vec1 = []
		vec2 = []
		vec3 = []
		vec4 = []
		vec5 = []
		vec6 = []
		vec8 = []
		vec9 = []
		tssVec = []
		tnVec = []
		tpVec = []
		for i in range(len(list1)):
			if i <2 or (i+1)%2:
				continue
			vec1.append(list1[i])
			vec2.append(list2[i])
			vec5.append(list5[i])
			vec8.append(list8[i])

		for i in range(len(list4)):
			if i <2 or (i+1)%2:
				continue
			vec4.append(list4[i])

		for i in range(len(list7)):
			if i<4 or ((i)%4==0):
				continue
			if (float(list7[i])<0):
				continue
			if i%4==1:
				tssVec.append(list7[i])
			if i%4==2:
				tnVec.append(list7[i])
			if i%4==3:
				tpVec.append(list7[i])

		tssVec = sorted(tssVec)
		tpVec = sorted(tpVec)
		tnVec = sorted(tnVec)
		tss = tssVec[len(tssVec)/2]
		tp = tpVec[len(tpVec)/2]
		tn = tnVec[len(tnVec)/2]
		tss = 1-max((float(tss)-20)/(150-20),0)
		tp = 1-max((float(tp)-0.6)/(2.2-0.6),0)
		tn = 1-max((float(tn)-0.05)/(0.35-0.05),0)


		freqVec = self.getNotZeroDays(vec1,vec2,vec2,0)
		FreqPredev = freqVec[0]
		FreqUntreated = freqVec[1]
		vec8 = sorted(vec8)
		cin = 3 * float(vec8[len(vec8)/2])
		print "cin: " +str(cin)

		for i in range(len(list3)):
			if i<2 or ((i)%2==0):
				continue
			if (float(list3[i]) * EIF <cin):
				continue
			if i%2==1:
				vec3.append(list3[i])

		FreqTreated = len(vec3)
		ETsum = self.SumAllValues(vec4)
		VolumeET = ETsum * 60*60*24*1000/1000000
		UntreadSum = self.SumAllValues(vec2)
		VolumeUntreated = UntreadSum * 60*60*24*1000/1000000
		preRunoffsum = self.SumAllValues(vec5)
		VolumePredev = preRunoffsum * 60*60*24*1000/1000000

		for i in range(len(list6)):
			if i<2 or ((i)%2==0):
				continue
			if (float(list6[i]) * EIF >cin):
				continue
			if i%2==1:
				vec6.append(list6[i])


		exfilSum = self.SumAllValues(vec6)
		FVg = (exfilSum * 60*60*24*1000/1000000) / VolumeUntreated
		print "exfilSum: " +str(exfilSum)
		print "VolumeUntreated: " +str(VolumeUntreated)
		print "FVg: " +str(FVg)

		#FvForest = self.find_nearest(self.ForestX,FVg)
		#FvPasture = self.find_nearest(self.PastureX,FVg)
		indexPX = self.find_nearest(self.PastureY,AnnualRain)
		indexFX = self.find_nearest(self.ForestY,AnnualRain)

		if self.ForestY[indexFX] > AnnualRain:
			Fx1 = self.ForestX[indexFX-1]
			Fx2 = self.ForestX[indexFX]
			Fy1 = self.ForestY[indexFX-1]
			Fy2 = self.ForestY[indexFX]
		else:
			Fx1 = self.ForestX[indexFX]
			Fx2 = self.ForestX[indexFX+1]
			Fy1 = self.ForestY[indexFX]
			Fy2 = self.ForestY[indexFX+1]

		if self.PastureY[indexPX] > AnnualRain:
			Px1 = self.PastureX[indexPX-1]
			Px2 = self.PastureX[indexPX]
			Py1 = self.PastureY[indexPX-1]
			Py2 = self.PastureY[indexPX]
		else:
			Px1 = self.PastureX[indexPX]
			Px2 = self.PastureX[indexPX+1]
			Py1 = self.PastureY[indexPX]
			Py2 = self.PastureY[indexPX+1]

		FvForest = np.abs((((Fx2-Fx1)*(Fy2-AnnualRain))/(Fy2-Fy1))-Fx2)
		FvPasture = np.abs((((Px2-Px1)*(Py2-AnnualRain))/(Py2-Py1))-Px2)
		print "FvForest: " + str(FvForest)
		print "FvPasture: " + str(FvPasture)
		if FVg < FvForest:
			tmpFV = FVg/FvForest
		elif FVg > FvPasture:
			tmpFV = max(0,(1-(FVg-FvPasture)/FvForest))
		else:
			tmpFV = 1

		print "tmpFV: " + str(tmpFV)
		tmpFF = 1 - max((float(FreqTreated)-float(FreqPredev))/(float(FreqUntreated)-float(FreqPredev)),0)
		tmpVR = 1-((VolumeUntreated-VolumePredev-VolumeET)/(VolumeUntreated-VolumePredev))
		tmpWQ = (tss+tn+tp)/3


		#for numbers with only value after the comma
		self.FF.append(float(int(tmpFF*1000))/10) 
		self.VR.append(float(int(tmpVR*1000))/10) 
		self.WQ.append(float(int(tmpWQ*1000))/10)
		self.FV.append(float(int(tmpFV*1000))/10)
		#print str(musicnr)+","+str(self.FF[0])+","+str(self.VR[0])+","+str(self.FV[0])+","+str(self.WQ[0])
		if os.path.exists(self.tmpFile):
			f = open(self.tmpFile,'a+')
			nr = 0
			for line in f:
				linearr = line.strip("\n").split(",")
				if(nr < linearr[0]):
					nr = linearr[0]
			f.write(str(nr)+","+str(self.FF[0])+","+str(self.VR[0])+","+str(self.FV[0])+","+str(self.WQ[0])+"," + ntpath.basename(realstring) + "\n")		
			f.close()
		else:
			f = open(self.tmpFile,'w')
			#f.write(str(musicnr)+","+str(self.FF[0])+","+str(self.VR[0])+","+str(self.FV[0])+","+str(self.WQ[0])+"\n")
			f.write("1,"+str(self.FF[0])+","+str(self.VR[0])+","+str(self.FV[0])+","+str(self.WQ[0])+"," + ntpath.basename(realstring) + "\n")
			f.close()
	def createInputDialog(self):
		form = ReadTableSecondary_Gui2(self, QApplication.activeWindow())
		form.exec_()
		return True
	def getNotZeroDays(self,vec1,vec2,vec3, boundry):
		count1 = 0
		count2 = 0
		count3 = 0
		tmpVec = vec3
		sorted(tmpVec)
		index = (80/100)*len(tmpVec) 
		boundry2 = tmpVec[index]#float(max(vec3)) * 0.2
		
		for i in range(len(vec1)):
			if float(vec1[i]) > float(boundry):
				count1 += 1
			if float(vec2[i]) > float(boundry):
				count2 += 1
			if float(vec3[i]) > float(boundry2):
				count3 += 1
		ergVec = [count1,count2,count3]
		return ergVec
	def readFileToList(self,Filename):
		f = open(Filename,'r')
		t = shlex.shlex(f.read(),posix= True)
		t.whitespace = ','
		t.whitespace += '\n\r'
		t.whitespace_split = True
		liste = list(t)
		f.close
		return liste

	def SumAllValues(self,vec):
		sum = 0 
		for i in vec:
			sum += float(i)
		return sum
	def find_nearest(self,array,value):
		tmp = []
		for i in array:
			tmp.append(i-value)
		idx=(np.abs(tmp)).argmin()
		return idx
	def writeBatFileFromFile(self,file):
		settings = QSettings()
		workpath = settings.value("workPath").toString()
		workpath += "/RunMusicSecondary.bat"
		if (platform.system() != "Linux"):
			file = file.replace("/","\\")
			workpath = workpath.replace("/","\\")
		f = open(workpath,'w')
		filearr = file.split(".")
		f.write("\"" + settings.value("Music").toString() + "\MUSIC.exe\" \""+ filearr[0] + "Secondary." + filearr[1] +"\" \"" + workpath + "musicConfigFileSecondary.mcf\" -light -silent\n")
		f.close()
	def writeBatFileFromNr(self,nr):
		settings = QSettings()
		workpath = settings.value("workPath").toString()
		workpath += "/RunMusicSecondary.bat"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		f = open(workpath,'w')
		f.write("\"" + settings.value("Music").toString() + "\MUSIC.exe\" \".\ubeatsMUSIC-1960PCsecondary"+str(nr)+".msf\" \"" + workpath + "musicConfigFileSecondary"+str(nr)+".mcf\" -light -silent\n")
		f.close()
	def writeMusicConfigFileSecondaryFromFile(self,file):
		settings = QSettings()
		workpath = settings.value("workPath").toString()
		workpath += "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		f = open(workpath + "musicConfigFileSecondary.mcf", 'w')
		f.write("Version = 100\n")
		f.write("Delimiter = #44\n")
		f.write("Export_TS (Reuse and ET fluxes, Inflow, \"ETandRe-useFluxes.TXT\",1d)\n")
		f.write("Export_TS (Infiltration Fluxes, Inflow, \"Exfiltration.TXT\",1d)\n")
		f.write("Export_TS (Pre-developed Total Runoff, Outflow, \"PredevelopTotalRunoff.TXT\",1d)\n")
		f.write("Export_TS (Pre-developed Runoff Frequency, Inflow, \"PredevelopRunoffFrequency.TXT \",1d)\n")
		f.write("Export_TS (Pre-developed Baseflows, Inflow, \"PredevelopBaseflowFrequency.TXT\",1d)\n")
		f.write("Export_TS (Urbanised Catchment, Outflow, \"UrbanisedCatchment.TXT\",1d)\n")
		f.write("Export_TS (Untreated Runoff Frequency, Inflow, \"UntreatedRunoffFrequency.TXT\",1d)\n")
		f.write("Export_TS (Receiving Node, Inflow, \"TreatedRunoffFrequency.TXT\",1d)\n")
		f.write("Export_TS (Receiving Node, InflowTSSConc; InflowTPConc; InflowTNConc, \"WQ.TXT\",1d)\n")
		f.close()
	def writeMusicConfigFileSecondaryFromNr(self,nr):
		settings = QSettings()
		workpath = settings.value("workPath").toString()
		workpath += "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		f = open(workpath + "musicConfigFileSecondary"+str(nr)+".mcf", 'w')
		f.write("Version = 100\n")
		f.write("Delimiter = #44\n")
		f.write("Export_TS (Reuse and ET fluxes, Inflow, \"ETandRe-useFluxes"+str(nr)+".TXT\",1d)\n")
		f.write("Export_TS (Infiltration Fluxes, Inflow, \"Exfiltration"+str(nr)+".TXT\",1d)\n")
		f.write("Export_TS (Pre-developed Total Runoff, Outflow, \"PredevelopTotalRunoff"+str(nr)+".TXT\",1d)\n")
		f.write("Export_TS (Pre-developed Runoff Frequency, Inflow, \"PredevelopRunoffFrequency"+str(nr)+".TXT \",1d)\n")
		f.write("Export_TS (Pre-developed Baseflows, Inflow, \"PredevelopBaseflowFrequency"+str(nr)+".TXT\",1d)\n")
		f.write("Export_TS (Urbanised Catchment, Outflow, \"UrbanisedCatchment"+str(nr)+".TXT\",1d)\n")
		f.write("Export_TS (Untreated Runoff Frequency, Inflow, \"UntreatedRunoffFrequency"+str(nr)+".TXT\",1d)\n")
		f.write("Export_TS (Receiving Node, Inflow, \"TreatedRunoffFrequency"+str(nr)+".TXT\",1d)\n")
		f.write("Export_TS (Receiving Node, InflowTSSConc; InflowTPConc; InflowTNConc, \"WQ"+str(nr)+".TXT\",1d)\n")
		f.close()
	def convertToSecondaryMusic(self, filename):
		fileIn = open(filename,"r")
		filearr = filename.split(".")
		fileOut = open(filearr[0] + "Secondary." + filearr[1] ,"w")
		urbfirst = ""
		urbsec = ""
		urbsplit1 = ""
		urbsplit2 = ""
		urbtmp = ""
		recvcounter = 0
		sumID = 0
		tmpID = 0
		idfound = False
		printing = False
		urbansourcenode = False
		WSUR = False
		PB = False
		IS = False
		BF = False
		SW = False
		tank = False
		calc = False
		notread = True
		foundDetention = False
		split = False
		detIds = []
		deten = False
		area = 0.0
		tmparea = 0.0
		totalarea = 0.0
		imp = 0.0
		per = 0.0
		splitlist = []
		splitlist2 = []
		EtFlux_list = []
		fluxinfl_list = []
		fluxinfl_list2 = []
		tanklist = []
		readcatchmentlist = False
		writetop = True
		writebot = False
		catchment_paramter_list = [] #[1,120,30,20,200,1,10,25,5,0]
		j = -1
		i = 0
		
		NodeIDToType = {}
		StartNodeConnectionsPrimary = {}
		currentNodeType = ""
		is_primary_connection = True
		
		source_id = ""
		for line in fileIn:
			i = i + 1
			linearr = line.strip("\n").split(",")
			if (recvcounter == 2):
				receivingnodeid = int(linearr[1])
				recvcounter = 0
			if (recvcounter == 1):
				recvcounter = 2
			if(linearr[0] == "Node Type"):
				if(linearr[1] == "ReceivingNode"):
					recvcounter = 1
			if(linearr[0] == "Node ID"):
				NodeIDToType[str(linearr[1])] = currentNodeType
				if(int(linearr[1]) > sumID):
					sumID = int(linearr[1])

			if(linearr[0] == "Node Type"):
				self.printsplitNodes(split,tmpID,urbfirst,urbsec,urbsplit1,urbsplit2,urbtmp,fileOut)
				currentNodeType = linearr[1]
				if(split):
					print "split!!!"
					splitlist.append(str(tmpID))
					splitlist2.append([str(tmpID) + "99","0"])
					NodeIDToType[str(tmpID) + "99"] = NodeIDToType[str(tmpID)]
					
					print splitlist2
				urbfirst = ""
				urbsec = ""
				urbtmp = ""
				split = False
				urbsplit1 = ""
				urbsplit2 = ""
				urbansourcenode = False
				writebot = False
				writetop = False
				if(linearr[1] == "UrbanSourceNode"):
					writetop = True
					urbansourcenode = True
			if(urbansourcenode):
				if(linearr[0] == "Node ID"):
					tmpID = linearr[1]
				if(linearr[0] == "Areas - Total Area (ha)"):
					urbtmp += line
					writetop = False
					tmparea = float(linearr[1])
					totalarea = totalarea + float(linearr[1])
				if(linearr[0] == "Areas - Impervious (%)"):
					urbtmp += line
					imp = float(linearr[1])
					if(imp == 100):
						EtFlux_list.append(tmpID)
				if(writetop):
					urbfirst += line
				if(writebot):
					urbsec += line
				if(linearr[0] == "Areas - Pervious (%)"):
					urbtmp += line
					per = float(linearr[1])
					if (per < 100 and per > 0):
						split = True
						EtFlux_list.append(tmpID)
					calc = True
					writebot = True
			else:
				fileOut.write(line)
			if(idfound):
				if(linearr[0] == "Target Node ID"):
					if is_primary_connection:
						StartNodeConnectionsPrimary[source_id] = str(linearr[1])
					print "j = " + str(j)
					splitlist2[j][1] = str(linearr[1])
					idfound = False
			if(linearr[0] == "Link Name"):
				is_primary_connection = False
				if linearr[1] == "Drainage Link":
					is_primary_connection = True
			if(linearr[0] == "Target Node ID"):
				if is_primary_connection:
					StartNodeConnectionsPrimary[source_id] = str(linearr[1])
			if(linearr[0] == "Source Node ID"):
				source_id = str(linearr[1])
				j = -1
				print len(splitlist)
				print "splitlist"
				print splitlist
				print len(splitlist2)
				print splitlist2
				for ID in splitlist:
					j = j + 1
					if(linearr[1] == ID):
						idfound = True
						break
			if(calc):
				if(imp < 100 and per < 100):
					urbsplit1 = "Areas - Total Area (ha)," + str(float(tmparea * imp /100)) + ",{ha}\n"
					urbsplit1 += "Areas - Impervious (%),100,{%}\n"
					urbsplit1 += "Areas - Pervious (%),0,{%}\n"
					urbsplit2 = "Areas - Total Area (ha)," + str(float(tmparea * per /100)) + ",{ha}\n"
					urbsplit2 += "Areas - Impervious (%),0,{%}\n"
					urbsplit2 += "Areas - Pervious (%),100,{%}\n"
				area =  area + tmparea * (imp/100)
				calc = False
			#first line of parameter list
			if(linearr[0] == "Rainfall-Runoff - Impervious Area - Rainfall Threshold (mm/day)" and notread):
				readcatchmentlist = True
			if(readcatchmentlist):
				catchment_paramter_list.append(linearr[1])
			#last line of parameter list
			if(linearr[0] == "Rainfall-Runoff - Groundwater Properties - Daily Deep Seepage Rate (%)"):
				readcatchmentlist = False
				notread = False

			if(linearr[0] == "Node Type" and linearr[1] == "WetlandNode"):
				WSUR = True
			if(linearr[0] == "Node Type" and linearr[1] == "PondNode"):
				PB = True
			if(linearr[0] == "Node Type" and linearr[1] == "InfiltrationSystemNodeV4"):
				IS = True
			if(linearr[0] == "Node Type" and linearr[1] == "BioRetentionNodeV4"):
				BF = True
			if(linearr[0] == "Node Type" and linearr[1] == "SwaleNode"):
				SW = True
			if(linearr[0] == "Node Type" and linearr[1] == "RainWaterTankNode"):
				tank = True
			if(linearr[0] == "Node Type" and linearr[1] == "DetentionBasinNode"):
				foundDetention = True
				deten = True
			if(deten and linearr[0] == "Node ID"):
				detIds.append(int(linearr[1]))
				deten = False
			if ( tank and linearr[0] == "Node ID"):
				tanklist.append(linearr[1])
				tank = False
			if (IS and linearr[0] == "Node ID"):
				IS = False
				EtFlux_list.append(linearr[1])
				fluxinfl_list2.append(linearr[1])
			if (linearr[0] == "Node ID" and (WSUR or PB or BF or SW)):
				WSUR = False
				PB = False
				BF = False
				SW = False
				EtFlux_list.append(linearr[1])
				fluxinfl_list.append(linearr[1])
		fileIn.close()
		fileOut.write("\n")
		print splitlist2
		print "Summary:"
		print "sumID: " + str(sumID)
		print "Area sum: " + str(area)
		print "ReceivingNode: " + str(receivingnodeid)
		print "Lists: " 
		print catchment_paramter_list

		print "Node Types List: " 
		print NodeIDToType
		print StartNodeConnectionsPrimary
		print EtFlux_list
		print fluxinfl_list
		print fluxinfl_list2
		areaSumID = sumID + 1
		umusic.writeMUSICcatchmentnode2(fileOut, "Pre-developed Total Runoff", "", areaSumID, 0, 0, area,1, catchment_paramter_list)
		umusic.writeMUSICjunction2(fileOut, "Pre-developed Baseflows", areaSumID+1, 0, 0)
		umusic.writeMUSIClinkToIgnore(fileOut,areaSumID,areaSumID+1)
		umusic.writeMUSICjunction2(fileOut, "Pre-developed Runoff Frequency", areaSumID+2, 0, 0)
		umusic.writeMUSIClinkToFrequenzy(fileOut,areaSumID,areaSumID+2)
		umusic.writeMUSICjunction2(fileOut, "Reuse and ET fluxes",areaSumID+3,0,0)
		umusic.writeMUSICjunction2(fileOut, "Infiltration Fluxes",areaSumID+4,0,0)
		umusic.writeMUSICcatchmentnode3(fileOut, "Urbanised Catchment", "", areaSumID+5, 0, 0, area,1, catchment_paramter_list)
		umusic.writeMUSICjunction2(fileOut, "Ignore", areaSumID+6, 0, 0)
		umusic.writeMUSIClinkToIgnore(fileOut,areaSumID+5,areaSumID+6)
		umusic.writeMUSICjunction2(fileOut, "Untreated Runoff Frequency", areaSumID+7, 0, 0)
		umusic.writeMUSIClinkToFrequenzy(fileOut,areaSumID+5,areaSumID+7)
		if(foundDetention):
			for nodeid in detIds:
				umusic.writeMUSIClinkToInfilFlux1(fileOut,nodeid,areaSumID+4)
				umusic.writeMUSIClinkToFlux(fileOut,nodeid,areaSumID+3)
		i = 0

		for IDs in splitlist:
			umusic.writeMUSIClink(fileOut,str(splitlist2[i][0]),splitlist2[i][1])
			i = i + 1
		for i in EtFlux_list:
		    umusic.writeMUSIClinkToFlux(fileOut, i, areaSumID+3)
		#Link to Infiltration
		for j in fluxinfl_list:
			#CechkIfConnectedToPound
			print str(j)
			start_node = str(j)
			end_node = StartNodeConnectionsPrimary[str(j)]
			print NodeIDToType[end_node]
			print NodeIDToType[start_node]
			if NodeIDToType[end_node] == "PondNode":
				print "PondNode Found"
				continue
			if NodeIDToType[end_node] == "WetlandNode":
				print "Wetland Found"
				continue
			if NodeIDToType[end_node] == "DetentionBasinNode":
				print "DetentionBasinNode Found"
				continue
			if NodeIDToType[end_node] == "InfiltrationSystemNodeV4":
				print "InfiltrationSystemNode Found"
				continue				
			if NodeIDToType[end_node] == "BioRetentionNodeV4":
				print "BioRetentionNode Found"
				continue
			if NodeIDToType[end_node] == "SwaleNode":
				print "SwaleNode Found"
				continue				
			umusic.writeMUSIClinkToInfilFlux1(fileOut, j, areaSumID+4)
		for k in fluxinfl_list2:
		    umusic.writeMUSIClinkToInfilFlux2(fileOut, k, areaSumID+4)
		umusic.writeMUSIClink(fileOut, areaSumID+4,int(receivingnodeid))
		for l in tanklist:
			umusic.writeTankLinkReuse(fileOut,l,areaSumID + 3)
		umusic.writeMUSICfooter(fileOut)
		fileOut.close()
		retvals = []
		retvals.append(area)
		retvals.append(totalarea)
		return retvals
	def printsplitNodes(self,split,tmpID,urbfirst,urbsec,urbsplit1,urbsplit2,urbtmp,fileOut):
		if(split):
			fileOut.write(urbfirst)
			fileOut.write(urbsplit1)
			fileOut.write(urbsec)
			urbfirst = urbfirst.replace("Node ID,"+ str(tmpID),"Node ID," + str(tmpID) + "99")
			fileOut.write(urbfirst)
			fileOut.write(urbsplit2)
			fileOut.write(urbsec)
		else:
			fileOut.write(urbfirst)
			fileOut.write(urbtmp)
			fileOut.write(urbsec)
