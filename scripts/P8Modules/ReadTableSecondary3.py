from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from pydynamind import *
from ReadTableSecondary_Gui2 import *
import shlex
import numpy as np
import os.path
from subprocess import call
import platform
import ntpath
import math
import tkMessageBox


class StreamHydrologyandWaterquality(Module):
	def __init__(self):
		Module.__init__(self)

		self.createParameter("FileName", FILENAME,"")
		self.FileName = ""
		self.createParameter("SimulationCity",DOUBLE,"")
		self.SimulationCity = 2
		self.createParameter("VolumeReductionIndex",DOUBLE,"")
		self.VolumeReductionIndex = 0
		self.createParameter("VolumeReduction",DOUBLE,"")
		self.VolumeReduction = 20
		self.createParameter("AnnualUserRain", DOUBLE, "")
		self.AnnualUserRain = 650
		self.createParameter("FrequencyRunoffDays",DOUBLE,"")
		self.FrequencyRunoffDays = 12
		self.createParameter("TssTarget",DOUBLE,"")
		self.TssTarget = 20.0
		self.createParameter("TnTarget",DOUBLE,"")
		self.TnTarget = 0.6
		self.createParameter("TpTarget",DOUBLE,"")
		self.TpTarget = 0.05
		self.createParameter("UseTargets", BOOL,"")
		self.UseTargets = False
		self.createParameter("Base" , DOUBLE , "")
		self.Base = 0.0
		self.createParameter("RainThres" , DOUBLE , "")
		self.RainThres = 1
		self.createParameter("RainSoil" , DOUBLE , "")
		self.RainSoil = 120
		self.createParameter("RainInitial" , DOUBLE , "")
		self.RainInitial = 30
		self.createParameter("RainField" , DOUBLE , "")
		self.RainField = 80
		self.createParameter("RainInfil" , DOUBLE , "")
		self.RainInfil = 200
		self.createParameter("RainInfil2" , DOUBLE , "")
		self.RainInfil2 = 1
		self.createParameter("RainDepth" , DOUBLE , "")
		self.RainDepth = 10
		self.createParameter("RainRecharge" , DOUBLE , "")
		self.RainRecharge = 25
		self.createParameter("RainBaseflow" , DOUBLE , "")
		self.RainBaseflow = 5
		self.createParameter("RainDeep" , DOUBLE , "")
		self.RainDeep = 0
		self.createParameter("ConsiderFluxes", BOOL , "")
		self.ConsiderFluxes = 0
		self.createParameter("useUB", BOOL, "")
		self.useUB = 0
		self.createParameter("RainStart" ,STRING , "")
		self.RainStart = "2000.01.01"
		self.createParameter("RainEnd", STRING , "")
		self.RainEnd = "2000.01.01"
		self.createParameter("RainDays", DOUBLE, "")
		self.RainDays = 0




		#Views
		self.simulation = View("SimulationData",COMPONENT,READ)
		self.simulation.getAttribute("msfFilename")
		self.simulation.addAttribute("MusicFileNo")
		self.simulation.addAttribute("SEIurb")
		self.simulation.addAttribute("SEIwsud")	
		self.simulation.addAttribute("NoY")
		self.simulation.addAttribute("alpha")
		self.simulation.addAttribute("useUB")

		self.PastureY = [169.46, 192.602, 223.436, 246.61, 269.752, 292.894, 323.761, 339.21, 370.077, 393.219, 416.393, 439.535, 462.677, 485.851, 508.993, 532.168, 555.31, 578.451, 601.626, 624.768, 655.602, 678.776, 701.918, 725.06, 748.234, 779.069, 802.211, 825.353, 856.187, 879.361, 902.503, 933.305, 956.447, 987.314, 1010.46, 1041.29, 1064.43, 1087.57, 1118.41, 1141.55, 1172.38, 1195.53, 1226.36, 1249.47, 1280.31, 1311.14, 1334.28, 1365.08, 1388.23, 1419.03, 1442.14, 1472.97, 1503.77, 1534.61, 1557.72, 1588.52, 1619.35, 1650.16, 1673.27, 1704.07, 1734.87, 1758.01, 1788.81, 1819.62, 1842.73, 1873.53, 1896.64, 1927.44, 1958.24, 1989.08, 2019.85, 2042.95, 2073.76, 2104.56, 2135.36, 2166.13, 2196.93, 2220.04, 2250.88, 2281.65, 2304.76, 2335.56, 2366.36, 2397.16, 2420.27, 2451.04, 2481.84, 2512.65, 2543.45, 2574.25, 2597.36, 2628.13, 2658.93, 2689.73, 2720.54, 2751.34, 2774.41, 2805.22, 2836.02, 2866.79, 2897.59, 2928.36, 2951.44, 2982.27, 3013.04, 3036.15, 3066.92, 3097.72, 3128.49, 3159.26, 3190.06, 3220.83, 3251.64, 3282.41, 3305.52, 3336.29, 3359.36, 3390.16, 3420.93, 3444.04, 3474.85, 3497.92, 3528.69]
		self.PastureX = [0.0297678, 0.0382198, 0.0466879, 0.0593416, 0.0677936, 0.0762456, 0.0889155, 0.0973513, 0.110021, 0.118473, 0.131127, 0.139579, 0.148031, 0.160685, 0.169137, 0.18179, 0.190242, 0.198694, 0.211348, 0.2198, 0.228268, 0.240922, 0.249374, 0.257826, 0.270479, 0.278948, 0.2874, 0.295852, 0.30432, 0.316973, 0.325425, 0.329692, 0.338144, 0.350814, 0.359266, 0.367734, 0.376186, 0.384638, 0.393106, 0.401558, 0.410026, 0.418478, 0.426946, 0.431196, 0.439665, 0.448133, 0.456585, 0.460851, 0.469303, 0.473569, 0.47782, 0.486288, 0.490554, 0.499022, 0.503273, 0.507539, 0.516007, 0.520273, 0.524524, 0.52879, 0.533056, 0.541508, 0.545775, 0.550041, 0.554291, 0.558558, 0.562808, 0.567074, 0.571341, 0.579809, 0.579874, 0.584124, 0.58839, 0.592657, 0.596923, 0.596988, 0.601254, 0.605504, 0.613972, 0.614037, 0.618287, 0.622554, 0.62682, 0.631086, 0.635337, 0.635401, 0.639668, 0.643934, 0.648201, 0.652467, 0.656717, 0.656782, 0.661048, 0.665315, 0.669581, 0.673847, 0.673896, 0.678162, 0.682429, 0.682493, 0.68676, 0.686824, 0.686873, 0.695341, 0.695406, 0.699656, 0.69972, 0.703987, 0.704051, 0.704116, 0.708382, 0.708447, 0.712714, 0.712778, 0.717028, 0.717093, 0.717142, 0.721408, 0.721473, 0.725723, 0.729989, 0.730038, 0.730102]
		self.ForestY = [376.2, 376.2, 406.91, 429.942, 460.653, 491.363, 522.073, 545.106, 575.816, 606.526, 637.236, 660.269, 690.979, 721.689, 752.399, 775.432, 806.142, 836.852, 859.885, 890.595, 913.628, 944.338, 975.048, 998.081, 1021.11, 1051.82, 1074.86, 1105.57, 1128.6, 1159.31, 1190.02, 1213.05, 1243.76, 1266.79, 1297.5, 1328.21, 1351.25, 1381.96, 1412.67, 1435.7, 1466.41, 1497.12, 1520.15, 1550.86, 1581.57, 1612.28, 1635.32, 1666.03, 1696.74, 1727.45, 1750.48, 1781.19, 1811.9, 1842.61, 1865.64, 1896.35, 1927.06, 1957.77, 1980.81, 2011.52, 2042.23, 2072.94, 2095.97, 2126.68, 2157.39, 2188.1, 2211.13, 2241.84, 2272.55, 2303.26, 2326.3, 2357.01, 2387.72, 2418.43, 2449.14, 2472.17, 2502.88, 2533.59, 2564.3, 2595.01, 2618.04, 2648.75, 2679.46, 2710.17, 2740.88, 2763.92, 2794.63, 2825.34, 2856.05, 2886.76, 2909.79, 2940.5, 2971.21, 3001.92, 3032.63, 3063.34, 3086.37, 3117.08, 3147.79, 3178.5, 3209.21, 3239.92, 3270.63, 3293.67, 3324.38, 3355.09, 3385.8, 3416.51, 3447.22]
		self.ForestX = [0.0172019, 0.0214358, 0.0256617, 0.0340973, 0.0341296, 0.0425652, 0.0467911, 0.051025, 0.0594606, 0.0636946, 0.0679205, 0.0763561, 0.08059, 0.0848239, 0.0932515, 0.0974854, 0.105921, 0.110147, 0.118583, 0.12701, 0.131244, 0.135478, 0.143906, 0.14393, 0.152365, 0.160793, 0.165027, 0.173454, 0.18189, 0.190326, 0.194552, 0.202987, 0.211415, 0.215649, 0.224084, 0.22831, 0.236746, 0.245181, 0.249407, 0.257843, 0.266278, 0.270504, 0.27894, 0.283174, 0.287408, 0.295835, 0.300069, 0.304303, 0.308537, 0.316965, 0.321199, 0.325433, 0.329667, 0.338094, 0.342328, 0.350764, 0.354998, 0.359224, 0.363457, 0.367691, 0.371925, 0.376151, 0.384587, 0.388821, 0.393055, 0.397281, 0.405716, 0.40995, 0.414184, 0.422612, 0.426846, 0.43108, 0.435313, 0.439547, 0.443773, 0.448007, 0.452241, 0.456475, 0.460709, 0.464935, 0.469169, 0.473403, 0.477637, 0.477669, 0.481895, 0.486129, 0.490363, 0.490395, 0.498831, 0.503057, 0.50729, 0.507323, 0.511557, 0.519992, 0.520025, 0.52425, 0.528484, 0.532718, 0.536952, 0.541186, 0.54542, 0.545452, 0.549678, 0.553912, 0.558146, 0.56238, 0.562412, 0.566646, 0.570872]
		datastream =[]
		datastream.append(self.simulation)
		self.addData("City",datastream)

	def run(self):
		self.ReceivBas = ""
		self.hasBase = False
		self.hasPipe = False
		self.hasInfil = False
		self.createInfilNode = False
		realstring = ""
		self.ImpAreaToTreatment = 0.0
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
			
			musicNo = int(simuData.getAttribute("MusicFileNo").getDouble())
			if (musicNo != 0):
				musicnr = musicNo
		simu = Component()
		simu.addAttribute("useUB",str(self.useUB))
		city.addComponent(simu,self.simulation)
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
		if(realstring == ""):
			realstring = workpath + "ubeatsMUSIC-ID" + str(musicnr) + ".msf"	#if music file from urbanbeats
			number = str(musicnr)
		else:														#music nr is -1 if music file from importMSF module
			number = ""
		self.writeBatFileFromFile(realstring)
		areas = self.convertToSecondaryMusic(realstring)
		self.writeMusicConfigFileSecondaryFromFile(realstring,self.ReceivBas,number)
		imparea = areas[0] 		#total impervious area
		totalarea = areas[1] 	#total area
		print "Music is running ... "
		if(platform.system() != "Linux"):
			call([str(workpath) + "RunMusicSecondary.bat", ""])
		print "Music Done."
		print "imparea: " + str(imparea)
		EIF = imparea / totalarea
		print "EIF: " + str(EIF)
		self.FF = []
		self.VR = [] 
		self.WQ = [] 
		self.FV = []
		self.cin = 0.0
		self.tmpFile = workpath + "EBRtable.txt"
		self.WQtable = workpath + "WQtable.txt"

		self.tableTSS = []
		self.tableTP = []
		self.tableTN = []
		
		'''		t
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
		elif self.SimulationCity == 5:
			AnnualRain = self.AnnualUserRain
		'''
		# his code is no longer used because we set the  the annualUserRain when the user selects a city in the GUI
		# no need to check which value the simulation city has 
		AnnualRain = self.AnnualUserRain
		print "AnnualRain : " + str(AnnualRain)

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
		list1 = self.readFileToList(workpath + "PredevelopRunoffFrequency"+str(number)+".TXT")
		list2 = self.readFileToList(workpath + "UntreatedRunoffFrequency"+str(number)+".TXT")
		list3 = self.readFileToList(workpath + "TreatedRunoffFrequency"+str(number)+".TXT")
		list4 = self.readFileToList(workpath + "ETandRe-useFluxes"+str(number)+".TXT")
		list5 = self.readFileToList(workpath + "PredevelopTotalRunoff"+str(number)+".TXT")
		if(self.createInfilNode):
			list6 = self.readFileToList(workpath + "Exfiltration"+str(number)+".TXT")
		list7 = self.readFileToList(workpath + "WQ"+str(number)+".TXT")
		list8 = self.readFileToList(workpath + "PredevelopBaseflowFrequency"+str(number)+".TXT")
		if(self.hasBase):
			list9 = self.readFileToList(workpath + "Baseflow"+str(number)+".TXT")
		if(self.hasPipe):
			list10 = self.readFileToList(workpath + "Pipe Flow"+str(number)+".TXT")


		vec1 = []
		vec2 = []
		vec3 = []
		vec4 = []
		vec5 = []
		vec6 = []
		vec8 = []
		vec9 = []
		vec10 = []
		vecBase = []
		vecPipe = []
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
			vec10.append(list3[i])

			#if no base, pipe or infiltration in msf file, there wont be any output from music so we just fill with zeros
			if(self.hasBase):
				vecBase.append(list9[i])
			else:
				vecBase.append(0)
			if(self.hasPipe):
				vecPipe.append(list10[i])
			else:
				vecPipe.append(0)
			if(self.createInfilNode):
				vec6.append(list6[i])
			else:
				vec6.append(0)


		for i in range(len(list7)):
			if i<4 or ((i)%4==0):
				continue
			if (float(list7[i])<0):
				continue
			if i%4==1:
				tssVec.append(list7[i])
			if i%4==2:
				tpVec.append(list7[i])
			if i%4==3:
				tnVec.append(list7[i])

		tssVec = sorted(tssVec)
		tpVec = sorted(tpVec)
		tnVec = sorted(tnVec)
		tss = tssVec[len(tssVec)/2]
		tp = tpVec[len(tpVec)/2]
		tn = tnVec[len(tnVec)/2]

		#write tss tp and tn into file for analyser
		if os.path.exists(self.WQtable):
			f = open(self.WQtable,'a+')
			f.write(ntpath.basename(realstring) + ","+str(tss)+","+str(tp)+","+str(tn) + "," + str(self.TssTarget) + "," + str(self.TpTarget) + "," +str(self.TnTarget) + "\n")
			f.close()
		else:
			f = open(self.WQtable,'w')
			f.write(ntpath.basename(realstring) + ","+str(tss)+","+str(tp)+","+str(tn) + "," + str(self.TssTarget) + "," + str(self.TpTarget) + "," +str(self.TnTarget) + "\n")
			f.close()

		self.tableTN.append(round(float(tn),2))
		self.tableTP.append(round(float(tp),2))
		self.tableTSS.append(round(float(tss),2))
		tss = 1-max((float(tss)-self.TssTarget)/(150-self.TssTarget),0)
		tp = 1-max((float(tp)-self.TpTarget)/(0.35-self.TpTarget),0)
		tn = 1-max((float(tn)-self.TnTarget)/(2.2-self.TnTarget),0)


		freqVec = self.getNotZeroDays(vec1,vec2,vec8,0)
		self.FreqPredev = freqVec[0]
		FreqUntreated = freqVec[1]
		vec8 = sorted(vec8)
		self.cin = 3 * float(vec8[len(vec8)/2])
		print "len(vec8): " +str(len(vec8))		
		if(float(self.Base) != float(0.0)):
			print "using user defined cin"
			self.cin = self.Base
			print "cin: " +str(self.cin)
		else:
			print "using default cin"
			print "cin: " +str(self.cin)


		for i in range(len(list3)):
			if i<2 or ((i)%2==0):
				continue
			if (float(list3[i]) <self.cin):
				continue
			if i%2==1:
				vec3.append(list3[i])


		FreqTreated = len(vec3)
		print "FreqPredev: " +str(self.FreqPredev)
		print "FreqUntreated: " +str(FreqUntreated)
		print "FreqTreated: " +str(FreqTreated)	

		RunoffVol = self.SumAllValues(vec3)		
		ETsum = self.SumAllValues(vec4)
		VolumeET = ETsum * 60*60*24*1000/1000000
		UntreadSum = self.SumAllValues(vec2)
		VolumeUntreated = UntreadSum * 60*60*24*1000/1000000
		preRunoffsum = self.SumAllValues(vec5)
		VolumePredev = preRunoffsum * 60*60*24*1000/1000000		
		VolumeInf = self.SumAllValues(vec6) * 60*60*24*1000/1000000
		print "VolumeET: " +str(VolumeET)
		print "VolumeInf: " +str(VolumeInf)

		
		for i in range(len(list3)):
			if i<2 or ((i)%2==0):
				continue
			if (float(list3[i]) * EIF >self.cin):
				continue
			if i%2==1:
				vec9.append(list3[i])

#       ## we need to calculated the impervious area of the treated areas (sum of impervious areas going to some treatment)
#       treatimparea = sum of impervious areas going to some treatment
#      ###### for each day in the timeseries 	i = 1 to end of infiltration fluxes 	
		Filtflow = []
		for i in range(len(vecBase)):
			Filtflow.append(float(vec6[i]) + float(vecPipe[i]) + float(vecBase[i]))
#			print Filtflow[i]
			if(Filtflow[i] > self.cin):
				Filtflow[i] = 0
		#print "super summe of DOOOOOMMM: "+str(math.fsum(Filtflow))

		print self.ImpAreaToTreatment
		TreatFiltVol = math.fsum(Filtflow)* 60*60*24*1000/1000000
		FVg=TreatFiltVol *1000 /(self.ImpAreaToTreatment*10000*AnnualRain/1000)

		VolImpArea = (imparea*10000*AnnualRain/1000)/1000
		print "TreatFiltVol: " +str(TreatFiltVol)
		print "VolImpArea: " +str(VolImpArea)
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

		FvForest = np.abs(1-(((Fx2-Fx1)*(Fy2-AnnualRain))/(Fy2-Fy1))-Fx2)
		FvPasture = np.abs(1-(((Px2-Px1)*(Py2-AnnualRain))/(Py2-Py1))-Px2)
		print "FvForest: " + str(FvForest)
		print "FvPasture: " + str(FvPasture)

		#if FVg < FvForest:
		#	tmpFV = FVg/FvForest
		#elif FVg > FvPasture:
		#	tmpFV = max(0,(1-(FVg-FvPasture)/FvForest))
		#else:
		tmpFV = FVg

		print "tmpFV: " + str(tmpFV)
		tmpFF = FreqTreated

		if(self.ConsiderFluxes):
			tmpVR = ((VolumeET+VolumeInf)*1000)/((imparea*10000*AnnualRain/1000))
		else:
			tmpVR = ((VolumeET)*1000)/((imparea*10000*AnnualRain/1000))


		print "self.FF " + str(tmpFF)
		print "days " + str(self.RainDays)
		start = int(self.RainStart.split(".")[0])
		end = int(self.RainEnd.split(".")[0])
		extraDays = 0
		yearDays = 365

		for i in range(start,end):
			if(QDate.isLeapYear(i)):
				extraDays = extraDays + 1
				yearDays = 366
		showMsgBox = False
		if(self.RainDays < yearDays):
			tmpFF = 0
			showMsgBox = True
		else:
			tmpFF = tmpFF / ((self.RainDays - extraDays) / 365)
			tmpVR = tmpVR / ((self.RainDays - extraDays) / 365)
			tmpFV = tmpFV / ((self.RainDays - extraDays) / 365)
			self.FreqPredev = self.FreqPredev / ((self.RainDays - extraDays) / 365)
		print "self.FF " + str(tmpFF)



		print "tmp VR: " + str(tmpVR)
		tmpWQ = (tss+tn+tp)/3
		print "tmp WQ: " + str(tmpWQ)

		print "ImpAreaToTreatment: " + str(self.ImpAreaToTreatment) 
		#for numbers with only value after the comma
		self.FF.append(float(int(tmpFF*1))/1) 
		self.VR.append(float(int(tmpVR*1000))/10) 
		self.WQ.append(float(int(tmpWQ*1000))/10)
		self.FV.append(float(int(tmpFV*1000))/10)
		#print str(musicnr)+","+str(self.FF[0])+","+str(self.VR[0])+","+str(self.FV[0])+","+str(self.WQ[0])
		if os.path.exists(self.tmpFile):
			f = open(self.tmpFile,'a+')
			nr = 0
			for line in f:
				linearr = line.strip("\n").split(",")
				if(nr < int(linearr[0])):
					nr = int(linearr[0])
			f.write(str(nr+1)+","+str(self.FF[0])+","+str(self.VR[0])+","+str(self.FV[0])+","+str(self.WQ[0])+"," + ntpath.basename(realstring) + "," + str(FreqUntreated) + "," + str(self.FrequencyRunoffDays) + "," + str(self.VolumeReduction) + "," + str(FvForest) + "," + str(FvPasture) + ","+ str(self.FreqPredev) + "," + str(self.cin) + "," + str(self.getConsiderFluxes()) + "," + str(self.tableTSS[0]) + "," + str(self.tableTP[0]) + "," + str(self.tableTN[0]) + "\n")
			f.close()
		else:
			f = open(self.tmpFile,'w')
			f.write("1,"+str(self.FF[0])+","+str(self.VR[0])+","+str(self.FV[0])+","+str(self.WQ[0])+"," + ntpath.basename(realstring) + "," + str(FreqUntreated) + "," + str(self.FrequencyRunoffDays) + "," + str(self.VolumeReduction) + "," + str(FvForest) + "," + str(FvPasture) + ","+ str(self.FreqPredev) + "," + str(self.cin) + "," + str(self.getConsiderFluxes()) + "," + str(self.tableTSS[0]) + "," + str(self.tableTP[0]) + "," + str(self.tableTN[0]) + "\n")
			#f.write(ntpath.basename(realstring)+"," + str(self.getConsiderFluxes()) + "," +  str(FvPasture) + "," +str(self.cin) + "," + str(self.FF[0])+","+str(self.VR[0])+","+str(self.FV[0])+"," + str(self.WQ[0]) + "," + str(tss) + "," + str(tp) + "," + str(tn) + "\n")		
			f.close()
		if(showMsgBox):
			window = Tk()
			window.wm_withdraw()
			window.geometry("1x1+"+str(window.winfo_screenwidth()/2)+"+"+str(window.winfo_screenheight()/2))
			tkMessageBox.showinfo(title="P8-WSC", message="This model requires at least one year of rainfall data")
			window.destroy()

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
		workpath += "/"#RunMusicSecondary.bat"
		if (platform.system() != "Linux"):
			file = file.replace("/","\\")
			workpath = workpath.replace("/","\\")
		f = open(workpath + "RunMusicSecondary.bat" ,'w')
		filearr = file.split(".")
		f.write("\"" + settings.value("Music").toString() + "\MUSIC.exe\" \""+ filearr[0] + "Secondary." + filearr[1] +"\" \"" + workpath +  "musicConfigFileSecondary.mcf\" -light -silent\n")
		f.close()
	def writeBatFileFromNr(self,nr):
		settings = QSettings()
		workpath = settings.value("workPath").toString()
		workpath += "/"#RunMusicSecondary.bat"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		f = open(workpath,'w')
		f.write("\"" + settings.value("Music").toString() + "\MUSIC.exe\" \".\ubeatsMUSIC-1960PCsecondary"+str(nr)+".msf\" \"" + workpath + "RunMusicSecondary.bat\" \"" + workpath + "musicConfigFileSecondary"+str(nr)+".mcf\" -light -silent\n")
		f.close()
	def writeMusicConfigFileSecondaryFromFile(self,file,name,number):
		settings = QSettings()
		workpath = settings.value("workPath").toString()
		workpath += "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		f = open(workpath + "musicConfigFileSecondary.mcf", 'w')
		f.write("Version = 100\n")
		f.write("Delimiter = #44\n")
		f.write("Export_TS (Reuse and ET fluxes, Inflow, \"ETandRe-useFluxes"+str(number)+".TXT\",1d)\n")
		if(self.createInfilNode):
			f.write("Export_TS (Infiltration Fluxes, Inflow, \"Exfiltration"+str(number)+".TXT\",1d)\n")
		f.write("Export_TS (Pre-developed Total Runoff, Outflow, \"PredevelopTotalRunoff"+str(number)+".TXT\",1d)\n")
		f.write("Export_TS (Pre-developed Runoff Frequency, Inflow, \"PredevelopRunoffFrequency"+str(number)+".TXT \",1d)\n")
		f.write("Export_TS (Pre-developed Baseflows, Inflow, \"PredevelopBaseflowFrequency"+str(number)+".TXT\",1d)\n")
		f.write("Export_TS (Urbanised Catchment, Outflow, \"UrbanisedCatchment"+str(number)+".TXT\",1d)\n")
		f.write("Export_TS (Untreated Runoff Frequency, Inflow, \"UntreatedRunoffFrequency"+str(number)+".TXT\",1d)\n")
		if(self.hasBase):
			f.write("Export_TS (Baseflow, Inflow, \"Baseflow"+str(number)+".TXT\",1d)\n")
		if(self.hasPipe):
			f.write("Export_TS (Pipe Flow, Inflow, \"Pipe Flow"+str(number)+".TXT\",1d)\n")
		f.write("Export_TS ("+str(name)+", Inflow, \"TreatedRunoffFrequency"+str(number)+".TXT\",1d)\n")
		f.write("Export_TS ("+str(name)+", InflowTSSConc; InflowTPConc; InflowTNConc, \"WQ"+str(number)+".TXT\",1d)\n")
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
		settings = QSettings()
		if(self.useUB):
			import ubeats_music_interface_5 as umusic
		else:
			if (settings.value("Music").toString().contains("MUSIC 5")):
				import ubeats_music_interface_5 as umusic
			else:
				import ubeats_music_interface as umusic
		fileIn = open(filename,"r")
		filearr = filename.split(".")
		fileOut = open(filearr[0] + "Secondary." + filearr[1] ,"w")
		urbfirst = ""
		urbsec = ""
		urbsplit1 = ""
		urbsplit2 = ""
		urbtmp = ""
		receiveBasName = ""
		recvcounter = 0
		foundOutBas = 0
		OutBasId = 0
		receivingnodeid = 0		
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
		totalimparea = 0.0
		imp = 0.0
		per = 0.0
		splitlist = []
		splitlist2 = []
		EtFlux_list = []
		fluxinfl_list = []
		fluxinfl_list2 = []
		tanklist = []
		pipelist = []
		infillist = []
		baseflowlist = []
		reclist = []
		readcatchmentlist = False
		writetop = True
		writebot = False
		catchment_paramter_list = [] #[1,120,30,20,200,1,10,25,5,0]
		catchment_paramter_list2 = [self.RainThres,self.RainSoil,self.RainInitial,self.RainField,self.RainInfil,self.RainInfil2,self.RainDepth,self.RainRecharge,self.RainBaseflow,self.RainDeep]
		j = -1
		i = 0
		
		impnodes =[]
		ImpIDtoImpArea = {}
		NodeIDToType = {}
		StartNodeConnectionsPrimary = {}
		currentNodeType = ""
		is_primary_connection = True
		
		target_id = ""
		source_id = ""
		PipeFlowLinkList = []
		DrainageLinkList = []

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
				if(foundOutBas):
					OutBasId = linearr[1]
					foundOutBas = 0
				NodeIDToType[str(linearr[1])] = currentNodeType
				if(int(linearr[1]) > sumID):
					sumID = int(linearr[1])
			if(linearr[0] == "Node Name"):
				if(linearr[1].find("OUT_Bas") != -1):
					receiveBasName = linearr[1]
					foundOutBas = 1
			if(linearr[0] == "Node Type"):
				self.printsplitNodes(split,tmpID,urbfirst,urbsec,urbsplit1,urbsplit2,urbtmp,fileOut)
				currentNodeType = linearr[1]
				if(split):
					print "split!!!"
					splitlist.append(str(tmpID))
					splitlist2.append([str(tmpID) + "99","0"])
					NodeIDToType[str(tmpID) + "99"] = NodeIDToType[str(tmpID)]
					baseflowlist.append(str(tmpID) + "99")
					
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
					totalimparea += imp * tmparea / 100
					ImpIDtoImpArea[str(tmpID)] = imp * tmparea / 100
					impnodes.append(tmpID)
					#if(imp == 100):
						#EtFlux_list.append(tmpID)
				if(writetop):
					urbfirst += line
				if(writebot):
					urbsec += line
				if(linearr[0] == "Areas - Pervious (%)"):
					urbtmp += line
					per = float(linearr[1])
					if (per < 100 and per > 0):
						split = True
						#EtFlux_list.append(tmpID)
					calc = True
					writebot = True
			else:
				fileOut.write(line)
			if(idfound):
				if(linearr[0] == "Target Node ID"):
					if is_primary_connection:
						StartNodeConnectionsPrimary[source_id] = str(linearr[1])
					print "j = " + str(j)
					if((NodeIDToType[linearr[1]] == "BioRetentionNodeV4") or (NodeIDToType[linearr[1]] == "SwaleNode") or (NodeIDToType[linearr[1]] == "WetlandNode") or (NodeIDToType[linearr[1]] == "PondNode") or (NodeIDToType[linearr[1]] == "InfiltrationSystemNodeV4")):
						reclist.append(str(source_id) + "99")
					else:
						splitlist2[j][1] = str(linearr[1])
					idfound = False
			if(linearr[0] == "Link Name"):
				is_primary_connection = False
				if linearr[1] == "Drainage Link":
					is_primary_connection = True
			if(linearr[0] == "Target Node ID"):
				target_id = str(linearr[1])
				if is_primary_connection:
					StartNodeConnectionsPrimary[source_id] = target_id
					DrainageLinkList.append(Link(source_id,target_id))
				
				PipeFlowLinkList.append(Link(source_id,target_id))
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
				self.createInfilNode = True
			if(linearr[0] == "Node Type" and linearr[1] == "PondNode"):
				PB = True
				self.createInfilNode = True
			if(linearr[0] == "Node Type" and linearr[1] == "InfiltrationSystemNodeV4"):
				IS = True
				self.createInfilNode = True
			if(linearr[0] == "Node Type" and linearr[1] == "BioRetentionNodeV4"):
				BF = True
				self.createInfilNode = True
			if(linearr[0] == "Node Type" and linearr[1] == "SwaleNode"):
				SW = True
				self.createInfilNode = True
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
				pipelist.append(linearr[1])
				#fluxinfl_list2.append(linearr[1])
			if(linearr[0] == "Node ID" and (WSUR or PB or BF)):
				EtFlux_list.append(linearr[1])
				infillist.append(linearr[1])
				pipelist.append(linearr[1])
				WSUR = False
				PB = False
				BF = False
			if (linearr[0] == "Node ID" and (SW)):
				SW = False
				EtFlux_list.append(linearr[1])
				#fluxinfl_list.append(linearr[1])
			
			# get all pipeflow
			#if((linearr[0] == "Secondary Outflow Components") and (linearr[1].find("Pipe Flow") >= 0)):
				#PipeFlowLinkList.append(Link(source_id,target_id))
				#pipelist.append(source_id)			
			'''
			# get all fluxes
			if(linearr[0] == "Secondary Outflow Components" and linearr[1].find("Infiltration")):
				infillist.append(source_id)
			# get all baseflow
			if(linearr[0] == "Secondary Outflow Components" and linearr[1].find("Impervious Storm Flow")):
				baseflowlist.append(source_id)
			'''

		for ID in impnodes:
			'''if(ID in StartNodeConnectionsPrimary):
				end_node = StartNodeConnectionsPrimary[ID]
				if NodeIDToType[end_node] == "PondNode":
					self.ImpAreaToTreatment += ImpIDtoImpArea[ID]
					continue
				if NodeIDToType[end_node] == "WetlandNode":
					self.ImpAreaToTreatment += ImpIDtoImpArea[ID]
					continue
				if NodeIDToType[end_node] == "DetentionBasinNode":
					self.ImpAreaToTreatment += ImpIDtoImpArea[ID]
					continue
				if NodeIDToType[end_node] == "InfiltrationSystemNodeV4":
					self.ImpAreaToTreatment += ImpIDtoImpArea[ID]
					continue				
				if NodeIDToType[end_node] == "BioRetentionNodeV4":
					self.ImpAreaToTreatment += ImpIDtoImpArea[ID]
					continue
				if NodeIDToType[end_node] == "SwaleNode":
					self.ImpAreaToTreatment += ImpIDtoImpArea[ID]
					continue
			'''

			if(not self.createInfilNode):
				self.ImpAreaToTreatment = totalimparea
			if(self.linkedToTreatment(ID,DrainageLinkList,NodeIDToType)):
				self.ImpAreaToTreatment += ImpIDtoImpArea[ID]

		print "DrainageLinkList"
		for link in DrainageLinkList:
			print link
		fileIn.close()
		fileOut.write("\n")
		print ImpIDtoImpArea
		print "Summary:"
		print "sumID: " + str(sumID)
		print "Area sum: " + str(area)
		print "ReceivingNode: " + str(receivingnodeid)
		print "OutBasId: " + str(OutBasId)
		print "receiveBasName: " + str(receiveBasName)
		print "Lists: "
		print catchment_paramter_list

		print "impnodes"
		print impnodes
		print "StartNodeConnection:"
		print StartNodeConnectionsPrimary
		print "Node Types List: " 
		print NodeIDToType
		print "ImpIDtoImpArea"
		print ImpIDtoImpArea
		print EtFlux_list
		print fluxinfl_list
		print fluxinfl_list2
		areaSumID = sumID + 1

		#write all the new nodes
		umusic.writeMUSICcatchmentnode2(fileOut, "Pre-developed Total Runoff", "", areaSumID, 0, 0, totalarea,1, catchment_paramter_list2)
		umusic.writeMUSICjunction2(fileOut, "Pre-developed Baseflows", areaSumID+1, 0, 0)
		umusic.writeMUSIClinkToIgnore(fileOut,areaSumID,areaSumID+1)
		umusic.writeMUSICjunction2(fileOut, "Pre-developed Runoff Frequency", areaSumID+2, 0, 0)
		umusic.writeMUSIClinkToFrequenzy(fileOut,areaSumID,areaSumID+2)
		umusic.writeMUSICjunction2(fileOut, "Reuse and ET fluxes",areaSumID+3,0,0)
		if(self.createInfilNode):
			umusic.writeMUSICjunction2(fileOut, "Infiltration Fluxes",areaSumID+4,0,0) # if we have no treatment node except rain tank dont create and put zeros for list6
		umusic.writeMUSICcatchmentnode3(fileOut, "Urbanised Catchment", "", areaSumID+5, 0, 0, totalarea,1, catchment_paramter_list)
		umusic.writeMUSICjunction2(fileOut, "Ignore", areaSumID+6, 0, 0)
		umusic.writeMUSIClinkToIgnore(fileOut,areaSumID+5,areaSumID+6)
		umusic.writeMUSICjunction2(fileOut, "Untreated Runoff Frequency", areaSumID+7, 0, 0)
		umusic.writeMUSIClinkToFrequenzy(fileOut,areaSumID+5,areaSumID+7)



		if(len(baseflowlist) != 0):
			self.hasBase = True
			umusic.writeMUSICjunction2(fileOut,"Baseflow",areaSumID+8,0,0)
		if(len(pipelist) != 0):
			self.hasPipe = True
			umusic.writeMUSICjunction2(fileOut,"Pipe Flow",areaSumID+9,0,0)
		if(len(infillist) != 0):
			self.hasInfil = True

		if(foundDetention):
			for nodeid in detIds:
				if(self.createInfilNode):
					umusic.writeMUSIClinkToInfilFlux1(fileOut,nodeid,areaSumID+4)
				umusic.writeMUSIClinkToFlux(fileOut,nodeid,areaSumID+3)
		i = 0

		for IDs in splitlist:
			if(splitlist2[i][1] != "0"):
				umusic.writeMUSIClink(fileOut,str(splitlist2[i][0]),splitlist2[i][1])
			i = i + 1
		for i in EtFlux_list:
		    umusic.writeMUSIClinkToFlux(fileOut, i, areaSumID+3)
		# Link to Infiltration
		print "start Flux list"
		print fluxinfl_list
		print "StartNodeConnectionsPrimary"
		print StartNodeConnectionsPrimary
		for j in fluxinfl_list:
			# CheckIfConnectedToPond
			print str(j)
			start_node = str(j)
			if(str(j) in StartNodeConnectionsPrimary):
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
			print "writing link for " + str(j)
			#umusic.writeMUSIClinkToInfilFlux1(fileOut, j, areaSumID+4)
		#for k in fluxinfl_list2:
		    #umusic.writeMUSIClinkToInfilFlux2(fileOut, k, areaSumID+4)

		#linknig infilflux baseflow and pipeflow nodes to receiving or outbasin node
		outid = 0
		if(OutBasId == 0 and receivingnodeid != 0):
			if(self.createInfilNode):
				umusic.writeMUSIClinkToInfilFlux2(fileOut, areaSumID+4,int(receivingnodeid))
			if(self.hasBase):
				umusic.writeMUSIClink(fileOut, areaSumID+8,int(receivingnodeid))
			if(self.hasPipe):
				umusic.writeMUSIClink(fileOut, areaSumID+9,int(receivingnodeid))
			self.ReceivBas = "Receiving Node"
			outid = receivingnodeid
		if(OutBasId != 0 and receivingnodeid == 0):
			if(self.createInfilNode):
				umusic.writeMUSIClinkToInfilFlux2(fileOut, areaSumID+4,int(OutBasId))
			if(self.hasBase):
				umusic.writeMUSIClink(fileOut, areaSumID+8,int(OutBasId))
			if(self.hasPipe):
				umusic.writeMUSIClink(fileOut, areaSumID+9,int(OutBasId))
			self.ReceivBas = receiveBasName
			outid = OutBasId
		if(OutBasId != 0 and receivingnodeid != 0):
			if(self.createInfilNode):
				umusic.writeMUSIClinkToInfilFlux2(fileOut, areaSumID+4,int(receivingnodeid))
			if(self.hasBase):
				umusic.writeMUSIClink(fileOut, areaSumID+8,int(receivingnodeid))
			if(self.hasPipe):
				umusic.writeMUSIClink(fileOut, areaSumID+9,int(receivingnodeid))
			self.ReceivBas = "Receiving Node"
			outid = receivingnodeid
		if (OutBasId == 0 and receivingnodeid == 0):
			print "didnt find any receiving nodes!!!"
		for l in tanklist:
			umusic.writeTankLinkReuse(fileOut,l,areaSumID + 3)

		# SEI links from predeveloped and urbanised catchmens
		L = math.sqrt( 2 *totalarea)
		Ku = L * 0.75 / 60
		Kp = L * 0.2 /60



		print "pipe ,infil and base list"
		print pipelist
		print infillist
		print baseflowlist
		print PipeFlowLinkList
		#make links
		if(receivingnodeid != 0): #rec links to recv node
			for r in reclist:
				umusic.writeMUSIClink(fileOut,r,int(receivingnodeid))
		else:
			for r in reclist:	#rec links to outbas
				umusic.writeMUSIClink(fileOut,r,int(OutBasId))

		#pipe links
		if(self.hasPipe):
			for p in pipelist:	
				if(self.isLastInTrain(p,PipeFlowLinkList,NodeIDToType)): 	#check if technology is last in train
					print str(p) + " is last"
					umusic.writeMUSIClinkPipe(fileOut,p,areaSumID+9)		# if yes link it to pipeflow node

		# links to infil node
		if(self.hasInfil):
			for i in infillist:
				if(self.createInfilNode):
					umusic.writeMUSIClinkToInfilFlux2(fileOut,i,areaSumID+4)

		#links to baseflow node
		if(self.hasBase):	
			for b in baseflowlist:	
				umusic.writeMUSIClinkBase(fileOut,b,areaSumID+8)


		#check if outbas last node or if its connected to another technology
		found = False
		techid = 0
		#get tech id from successor
		fileIn = open(filename,"r")
		for line in fileIn:
			linearr = line.strip("\n").split(",")
			if(linearr[0] == "Source Node ID"):
				if(linearr[1] == outid):
					found = True
			if(found):		
				if(linearr[0] == "Target Node ID"):
					techid = linearr[1]
					break
		fileIn.close()

		# get name of tech
		name = ""
		fileIn = open(filename,"r")
		for line in fileIn:
			linearr = line.strip("\n").split(",")
			if(linearr[0] == "Node Name"):
				tmpname = linearr[1]
			if(linearr[0] == "Node ID" and linearr[1] == techid):
				name = tmpname
				break
		fileIn.close()		
		if(name != ""):
			self.ReceivBas = name
		print "techname: " + self.ReceivBas

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
	def getClassName(self):
		return "Stream Hydrology and Water Quality"
	def getFileName(self):
		return "Scenario Simulation and Assessment"
	def isLastInTrain(self,id,linkList,NodeToType):
		for link in linkList:
			if(link.getSRC() == id):
				if(self.isTech(link.getDST(),NodeToType)):
					return False
		return True
	def isTech(self, id , NodeToType):
		if(NodeToType[id] == "PondNode"):
			return True
		if(NodeToType[id] == "WetlandNode"):
			return True
		if(NodeToType[id] == "DetentionBasinNode"):
			return True
		if(NodeToType[id] == "InfiltrationSystemNodeV4"):
			return True
		if(NodeToType[id] == "BioRetentionNodeV4"):
			return True
		if(NodeToType[id] == "SwaleNode"):
			return True
		return False
	def getConsiderFluxes(self):
		if(int(self.ConsiderFluxes)):
			return "Yes"
		else:
			return "No"
	def linkedToTreatment(self,id,DrainageLinkList,NodeToType):
		for link in DrainageLinkList:
			if(link.getSRC() == id):
				if(self.isTech(link.getDST(),NodeToType)):
					return True
				else:
					if(self.linkedToTreatment(link.getDST(),DrainageLinkList,NodeToType)):
						return True
		return False

class Link:
	def __init__(self,src,dst):
		self.src = src
		self.dst = dst
	def getDST(self):
		return self.dst
	def getSRC(self):
		return self.src
	def __str__(self):
		return "src: " + str(self.src) + " dst: " + str(self.dst)