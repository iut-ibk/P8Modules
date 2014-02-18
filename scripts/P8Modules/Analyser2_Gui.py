 # -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QSettings
from pydynamind import *
from Ui_Analyser2_Dialog import Ui_Analyser2_GUI
import shlex
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os.path
import os
import math
from operator import itemgetter
import platform
import ntpath



class Analyser2_Gui(QtGui.QDialog):
	def __init__(self,m,parent=None):
		self.module = Module
		self.module = m
		QtGui.QDialog.__init__(self,parent)
		self.ui = Ui_Analyser2_GUI()
		self.ui.setupUi(self)
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		self.TPRFile = workpath + "TPRtable.txt"
		self.EBRFile = workpath + "EBRtable.txt"
		self.UtilFile = workpath + "UtilTable.txt"
		self.summaryFile = workpath + "AnalyzerSummary.csv"
		QtCore.QObject.connect(self.ui.pb_plotEBR, QtCore.SIGNAL("released()"),self.plotEBR)
		QtCore.QObject.connect(self.ui.pb_plotEBR2, QtCore.SIGNAL("released()"),self.plotEBR2)
		QtCore.QObject.connect(self.ui.pb_plotEBR3, QtCore.SIGNAL("released()"),self.plotEBR3)
		QtCore.QObject.connect(self.ui.pb_plotEBR4, QtCore.SIGNAL("released()"),self.plotEBR4)
		QtCore.QObject.connect(self.ui.pb_plotTPR, QtCore.SIGNAL("released()"),self.plotTPR)
		QtCore.QObject.connect(self.ui.pb_delete, QtCore.SIGNAL("released()"),self.delete)
		QtCore.QObject.connect(self.ui.pb_plotUtil, QtCore.SIGNAL("released()"),self.plotUtil)
		QtCore.QObject.connect(self.ui.pb_plotSEI, QtCore.SIGNAL("released()"),self.plotSEI)
		QtCore.QObject.connect(self.ui.pb_plotSEI2, QtCore.SIGNAL("released()"),self.plotSEI2)


		self.colorarr = ['#1f99d0','#8fcce7','#abcd88', '#cf33e1','#ffff00','#896161','#e5e5e5','#d81417','#FF4500','#000000','#FFFFFF']#'#1f99d0','#8fcce7','#abcd8',
	def delete(self):
		if os.path.exists(self.TPRFile):
			os.remove(self.TPRFile)
		if os.path.exists(self.UtilFile):
			os.remove(self.UtilFile)
		if os.path.exists(self.EBRFile):
			os.remove(self.EBRFile)
	def plotEBR(self):
		params = {'legend.fontsize': 8,'legend.linewidth': 2,'legend.labelspacing':0.2}
		mpl.rcParams.update(params)
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		filename = workpath + "EBRtable.txt"
		mpl.rcParams['toolbar'] = 'None'
		i = 0
		FreqUn = 0.0
		FreqRun = 0.0
		FreqPredev = 0
		bars = []
		tmpbar = []
		xlabel = []
		if os.path.exists(filename):
			f = open(filename,'r')
			for line in f:
				linearr = line.strip('\n').split(',')
				FreqUn = round(float(linearr[6]))
				FreqRun = round(float(linearr[7]))
				FreqPredev = round(float(linearr[11]))
				tmpbar.append(round(float(linearr[1])))
				xlabel.append(str(linearr[5]))
				i = i + 1
			f.close()
			ind = np.arange(i)
			space = 0.25
			width = 0.75 / i
			for val in tmpbar:
				bars.append(val)
			print bars
			fig = plt.figure()
			ax = fig.add_subplot(111)
			figbars = ax.bar(ind,bars,color = '#3399FF')
			ax.set_ylabel('Frequency of runoff days per year')
			ax.set_title('Stream Hydrology and Water Quality')
			ax.set_xticks(ind+(width*i)*0.75)
			ax.set_xticklabels(xlabel)
			ax.text(0,FreqUn,"Urbanised catchment")
			plt.plot(ax.get_xlim(),[FreqUn,FreqUn], color = 'red',linestyle = '--', lw=2)#, label = "Urbanised catchment")
			ax.text(0,FreqRun,"Target")
			plt.plot(ax.get_xlim(),[FreqRun,FreqRun], color = 'green', linestyle = '--', lw=2)#, label = "Target")
 			ax.text(0,FreqPredev,"Natural catchment")
			plt.plot(ax.get_xlim(),[FreqPredev,FreqPredev], color = 'blue', linestyle = '--', lw=2)#, label = "Natural catchment")
			#plt.text(ax.get_xlim()[1],1,"SEI stretch limit", backgroundcolor = "white")
			ax.legend()# (bars1[0],bars2[0],bars3[0]) , ('Option 1', 'Option 2', 'Option 3') )
			ax.legend(loc='best')
			#plt.xlim([0,100])
			fig.canvas.set_window_title('Stream Hydrology and Water Quality') 
			fig.autofmt_xdate()
			plt.grid(True, which="both",ls="-",color="#939393")
			#plt.ylim([0,int(urb)+1])
			plt.show()
			plt.savefig(str(workpath)+"FrequencyRunOffPerDaysPlot.png")
		else:
			print "No EBR file found!!!"
	def plotEBR2(self):
		params = {'legend.fontsize': 8,'legend.linewidth': 2,'legend.labelspacing':0.2}
		mpl.rcParams.update(params)
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		filename = workpath + "EBRtable.txt"
		mpl.rcParams['toolbar'] = 'None'
		i = 0
		TotVolRed = 0.0
		bars = []
		tmpbar = []
		xlabel = []
		if os.path.exists(filename):
			f = open(filename,'r')
			for line in f:
				linearr = line.strip('\n').split(',')
				TotVolRed = round(float(linearr[8]))
				tmpbar.append(round(float(linearr[2])))
				xlabel.append(str(linearr[5]))
				i = i + 1
			f.close()
			ind = np.arange(i)
			space = 0.25
			width = 0.75 / i
			for val in tmpbar:
				bars.append(val)
			print bars
			fig = plt.figure()
			ax = fig.add_subplot(111)
			figbars = ax.bar(ind,bars,color = '#3399FF')
			ax.set_ylabel('Proportion of total volume reduction (%)')
			ax.set_title('Stream Hydrology and Water Quality')
			ax.set_xticks(ind+(width*i)*0.75)
			ax.set_xticklabels(xlabel)
			ax.text(0,100,"Natural catchment")
			plt.plot(ax.get_xlim(),[100,100], color = 'blue',linestyle = '--', lw=2)#, label = "Natural catchment")
			ax.text(0,1,"Impervious catchment")
			plt.plot(ax.get_xlim(),[0.5,0.5], color = 'red',linestyle = '--', lw=2)#, label = "Impervious catchment")
			ax.text(0,TotVolRed,"Target")
			plt.plot(ax.get_xlim(),[TotVolRed,TotVolRed], color = 'green',linestyle = '--', lw=2)#, label = "Target")
			
			#plt.text(ax.get_xlim()[1],1,"SEI stretch limit", backgroundcolor = "white")
			ax.legend()# (bars1[0],bars2[0],bars3[0]) , ('Option 1', 'Option 2', 'Option 3') )
			ax.legend(loc='best')
			#plt.xlim([0,100])
			fig.canvas.set_window_title('Stream Hydrology and Water Quality') 
			fig.autofmt_xdate()
			plt.grid(True, which="both",ls="-",color="#939393")
			plt.ylim([0,105])
			plt.show()
			plt.savefig(str(workpath)+"ProportionOfTotalVolumeReductionPlot.png")
		else:
			print "No EBR file found!!!"
	def plotEBR3(self):
		params = {'legend.fontsize': 8,'legend.linewidth': 2,'legend.labelspacing':0.2}
		mpl.rcParams.update(params)
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		filename = workpath + "EBRtable.txt"
		mpl.rcParams['toolbar'] = 'None'
		i = 0
		FvF = 0.0
		FvP = 0.0
		bars = []
		tmpbar = []
		xlabel = []
		if os.path.exists(filename):
			f = open(filename,'r')
			for line in f:
				linearr = line.strip('\n').split(',')
				FvF = round(float(linearr[9])*100)
				FvP = round(float(linearr[10])*100)
				tmpbar.append(round(float(linearr[3])))
				xlabel.append(str(linearr[5]))
				i = i + 1
			f.close()
			ind = np.arange(i)
			space = 0.25
			width = 0.75 / i
			for val in tmpbar:
				bars.append(val)
			print bars
			fig = plt.figure()
			ax = fig.add_subplot(111)
			figbars = ax.bar(ind,bars,color = '#3399FF')
			ax.set_ylabel('Proportion of filtered volume (% = stream flow coefficient)')
			ax.set_title('Stream Hydrology and Water Quality')
			ax.set_xticks(ind+(width*i)*0.75)
			ax.set_xticklabels(xlabel)
			ax.text(0,FvF,"Upper limit (area of forest)")
			plt.plot(ax.get_xlim(),[FvF,FvF], color = 'blue',linestyle = '--', lw=2)#, label = "Upper limit (area of forest)")
			ax.text(0,FvP,"Lower limit (area of pasture)")
			plt.plot(ax.get_xlim(),[FvP,FvP], color = 'green',linestyle = '--', lw=2)#, label = "Lower limit (area of pasture)")
			ax.text(0,1,"Impervious catchment")
			plt.plot(ax.get_xlim(),[0.5,0.5], color = 'red',linestyle = '--', lw=2)#, label = "Impervious catchment")
			ax.legend()# (bars1[0],bars2[0],bars3[0]) , ('Option 1', 'Option 2', 'Option 3') )
			ax.legend(loc='best')
			#plt.xlim([0,100])
			fig.canvas.set_window_title('Stream Hydrology and Water Quality') 
			fig.autofmt_xdate()
			plt.grid(True, which="both",ls="-",color="#939393")
			plt.ylim([0,100])
			plt.show()
			plt.savefig(str(workpath)+"ProportionOfFilteredVolumePlot.png")
		else:
			print "No EBR file found!!!"	
	def plotEBR4(self):
		params = {'legend.fontsize': 8,'legend.linewidth': 2,'legend.labelspacing':0.2}
		mpl.rcParams.update(params)
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		filename = workpath + "WQtable.txt"
		mpl.rcParams['toolbar'] = 'None'
		i = 0
		tsstop = 150
		tptop = 0.35
		tntop = 2.2
		tsstarget = 0
		tptarget = 0
		tntarget = 0
		bars = []
		tss = []
		tp = []
		tn = []
		xlabel = []
		if os.path.exists(filename):
			f = open(filename,'r')
			for line in f:
				linearr = line.strip('\n').split(',')
				tsstarget = round(float(linearr[4]),2)
				tptarget = round(float(linearr[5]),2)
				tntarget = round(float(linearr[6]),2)
				tss.append(round(float(linearr[1]),2))
				tp.append(round(float(linearr[2]),2))
				tn.append(round(float(linearr[3]),2))
				xlabel.append(str(linearr[0]))
				i = i + 1
			f.close()
			ind = np.arange(i)
			space = 0.25
			width = 0.75 / i

			fig = plt.figure()
			ax = fig.add_subplot(111)
			figbars = ax.bar(ind,tss,color = '#3399FF')
			ax.set_ylabel('TSS mean concentration (mg/l)')
			ax.set_title('Stream Hydrology and Water Quality')
			ax.set_xticks(ind+(width*i)*0.75)
			ax.set_xticklabels(xlabel)
			ax.text(0,tsstop,"Untreadted stormwater")
			ax.plot(ax.get_xlim(),[tsstop,tsstop], color = 'red',linestyle = '--', lw=2)
			ax.text(0,tsstarget,"Target")
			ax.plot(ax.get_xlim(),[tsstarget,tsstarget], color = 'green',linestyle = '--', lw=2)
			fig.canvas.set_window_title('Stream Hydrology and Water Quality') 
			fig.autofmt_xdate()
			plt.grid(True, which="both",ls="-",color="#939393")
			plt.savefig(str(workpath)+"WQtss.png")

			fig1 = plt.figure()
			ax1 = fig1.add_subplot(111)
			figbars1 = ax1.bar(ind,tp,color = '#3399FF')
			ax1.set_ylabel('TP mean concentration (mg/l)')
			ax1.set_title('Stream Hydrology and Water Quality')
			ax1.set_xticks(ind+(width*i)*0.75)
			ax1.set_xticklabels(xlabel)
			ax1.text(0,tptop,"Untreadted stormwater")
			ax1.plot(ax.get_xlim(),[tptop,tptop], color = 'red',linestyle = '--', lw=2)
			ax1.text(0,tptarget,"Target")
			ax1.plot(ax.get_xlim(),[tptarget,tptarget], color = 'green',linestyle = '--', lw=2)
			fig1.canvas.set_window_title('Stream Hydrology and Water Quality') 
			fig1.autofmt_xdate()
			plt.grid(True, which="both",ls="-",color="#939393")
			plt.savefig(str(workpath)+"WQtp.png")

			fig2 = plt.figure()
			ax2 = fig2.add_subplot(111)
			figbars2 = ax2.bar(ind,tn,color = '#3399FF')
			ax2.set_ylabel('TN mean concentration (mg/l)')
			ax2.set_title('Stream Hydrology and Water Quality')
			ax2.set_xticks(ind+(width*i)*0.75)
			ax2.set_xticklabels(xlabel)
			ax2.text(0,tntop,"Untreadted stormwater")
			ax2.plot(ax.get_xlim(),[tntop,tntop], color = 'red',linestyle = '--', lw=2)
			ax2.text(0,tntarget,"Target")
			ax2.plot(ax.get_xlim(),[tntarget,tntarget], color = 'green',linestyle = '--', lw=2)
			fig2.canvas.set_window_title('Stream Hydrology and Water Quality') 
			fig2.autofmt_xdate()

			plt.grid(True, which="both",ls="-",color="#939393")
			plt.savefig(str(workpath)+"WQtn.png")
			plt.show()
		else:
			print "No WQ file found!!!"
	def plotTPR(self):
		params = {'legend.fontsize': 8,'legend.linewidth': 2,'legend.labelspacing':0.2}
		mpl.rcParams.update(params)
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		filename = workpath + "Perf_TTE.txt"#QtGui.QFileDialog.getOpenFileName(self, "Open MUSIC Output File", workpath,self.tr("Text Files (*.txt)"))
		mpl.rcParams['toolbar'] = 'None'
		show2 = False
		show3 = False
		i = 1
		f = open(filename,'r')
		text = shlex.shlex(f.read(),posix = True)
		text.whitespace = ','
		text.whitespace += '\n'
		text.whitespace_split = True
		liste = list(text)
		#number = filename[len(filename)-5]
		bars = []
		bars1 = (round(float(liste[7])),round(float(liste[11])),round(float(liste[15])),round(float(liste[19])))
		f.close
		if os.path.exists(self.TPRFile):
			f = open(self.TPRFile,'r')
			for line in f:
				linearr = line.strip('\n').split(',')
				tmpbar = (round(float(linearr[1])),round(float(linearr[2])),round(float(linearr[3])),round(float(linearr[4])))
				bars.append([tmpbar,linearr[0]])
				'''
				if (int(line[0]) == 1):
					bars2 = tmpbar
					show2 = True
				elif (int(line[0]) == 2):
					bars3 = tmpbar
					show3 = True
				'''
				i = i + 1
			f.close()
		bars.append([bars1,ntpath.basename(self.module.musicfile)])
		n = 4
		ind = np.arange(n)
		space = 0.25
		width = 0.75 / i
		j = 0
		fig = plt.figure()
		ax = fig.add_subplot(111)
		for bar in bars:
			tmp = ax.bar(ind + width * j,bar[0],width,color = self.colorarr[j])
			tmp.set_label('' + str(bar[1]))
			j = j + 1
		'''
		rects1 = ax.bar(ind,bars1,width,color = '#1f99d0')
		rects1.set_label('Realisation 1')
		if (show2):
			rects2 = ax.bar(ind+width,bars2,width,color='#8fcce7')
			rects2.set_label('Realisation 2')
		if (show3):
			rects3 = ax.bar(ind+width*2,bars3,width,color='#abcd8f')
			rects3.set_label('Realisation 3')
		'''
		ax.set_ylabel('Reduction(%)')
		ax.set_title('Treatment/Harvesting')
		ax.set_xticks(ind+((width*i)*0.75))
		ax.set_xticklabels( ('Volume' , 'TSS' , 'TP' , 'TN') )
		ax.legend()# (bars1[0],bars2[0],bars3[0]) , ('Option 1', 'Option 2', 'Option 3') )
		ax.legend(loc='best')
		#plt.xlim([0,100])
		fig.canvas.set_window_title(' ') 
		fig.autofmt_xdate()
		plt.ylim([0,100])
		plt.show()
		f = open(self.TPRFile,'w')
		j = 1
		for bar in bars:
			f.write(str(bar[1]) + "," +str(bar[0][0])+","+str(bar[0][1])+","+str(bar[0][2])+","+str(bar[0][3])+"\n")
		'''
		f.write("1,"+str(bars1[0])+","+str(bars1[1])+","+str(bars1[2])+","+str(bars1[3])+"\n")
		if (show2):	
			f.write("2,"+str(bars2[0])+","+str(bars2[1])+","+str(bars2[2])+","+str(bars2[3])+"\n")	
		if (show3):
			f.write("2,"+str(bars3[0])+","+str(bars3[1])+","+str(bars3[2])+","+str(bars3[3])+"\n")
		'''
		f.close()
		plt.savefig(str(workpath) + 'TreatmentPerformancePlot.png')
		#writing information into summary file
		'''if(os.path.exists(self.summaryFile)):
			f = open(self.summaryFile, 'a+')
			f.write("------------ Analyzer Summary ------------\n\n\n")
			f.write(" TP: \n\n")
			for bar in bars:
				f.write(str(bar[0]) + "\n")
			f.write("\n------------------------------------------\n\n")
		else:
			f = open(self.summaryFile, 'w')
			f.write(" TP: \n")
			for bar in bars:
				f.write(str(bar[0]) + "\n")
			f.write("\n------------------------------------------\n\n")
		'''
	def plotUtil(self):
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		mpl.rcParams['toolbar'] = 'None'
		ResultVec = []
		if(os.path.exists(self.UtilFile)):
			ResultVec = self.loadUtilFile()
		print len(ResultVec)
		fig = plt.figure()
		ax = fig.add_subplot(111)
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
		if(BfFlag):
			p1 = plt.bar(ind,BFvec,width,color ='b')
		p1.set_label('BF')
		if(PbFlag):
			p2 = plt.bar(ind,PBvec,width,color = 'r',bottom = BFvec)
			p2.set_label('PB')
		if(IsFlag):
			p3 = plt.bar(ind,ISvec,width,color = 'y',bottom = BFvec + PBvec)
			p3.set_label('IS')
		if(WsurFlag):
			p4 = plt.bar(ind,WSURvec,width,color = 'g',bottom = ISvec + BFvec + PBvec)
			p4.set_label('WSUR')
		if(SwFlag):
			p5 = plt.bar(ind,SWvec,width, color = 'black',bottom = BFvec + PBvec + ISvec + WSURvec)
			p5.set_label('SW')
		plt.ylim([0,100])
		ax.set_xticks(ind+width)
		xticksvec = []
		for i in range(len(ResultVec)):
			xticksvec.append("Realisation " + str(int(ResultVec[i][0])) + "\n" + str('%.2f' % ResultVec[i][1]) + "%")
		ax.set_xticklabels(xticksvec)
		ax.set_ylabel("Proportion of Utilisation (%)")
		ax.legend()
		ax.legend(loc='best')
		fig.canvas.set_window_title(' ')
		box = ax.get_position()
		ax.set_position([box.x0, box.y0 + box.height * 0.2, box.width * 0.8, box.height *0.8 ])
		ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
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
		txt = ""
		outtxt = ""
		if (BfFlag):
			txt += "BF-Biofiltration System       " + BFstring + "\n"
			outtxt += "BF-Biofiltration System," + BFstring + "\n"
		if(PbFlag):
			txt += "PB-Ponds & Basins             " + PBstring + "\n"
			outtxt += "PB-Ponds & Basins," + PBstring + "\n"
		if (IsFlag):
			txt += "Infiltration System               " + ISstring + "\n"
			outtxt+= "Infiltration System," + ISstring + "\n"
		if(WsurFlag):
			txt += "WSUR - Surface Wetland    " + WSURstring + "\n"
			outtxt += "WSUR - Surface Wetland," + WSURstring + "\n"
		if (SwFlag):
			txt += "Swale                                  " + SWstring + "\n"
			outtxt += "Swale," + SWstring + "\n"
		fig.text(0.05,0.01,txt)
		plt.show()
		plt.savefig(str(workath) + 'UtilisationsPlot.png')
		f = open(workpath + "util.csv", "w")
		f.write(outtxt)
		f.close()
		self.writeUtilFile(ResultVec)
	def plotSEI(self):
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		mpl.rcParams['toolbar'] = 'None'
		a = []
		b = []
		c = []
		d = []
		e = []
		f = []
		fil = open(workpath + "urbtable.csv","r")
		for line in fil:
			linearr = line.strip(" \n").split(",")
			c.append(float(linearr[0]))
			d.append(linearr[1])
		fil.close()
		fil = open(workpath + "wsudtable.csv","r")
		for line in fil:
			linearr = line.strip(" \n").split(",")
			e.append(float(linearr[0]))
			f.append(linearr[1])
		fil.close()
		fil = open(workpath + "pretable.csv","r")
		for line in fil:
			linearr = line.strip(" \n").split(",")
			a.append(float(linearr[0]))
			b.append(linearr[1])
		fil.close()
		border = []
		border1 = []
		border2 = []
		''' old code
		for i in range(len(a)):
			if(b[i] < 0.3):
				continue
			border.append(a[i])
		for i in range(len(c)):
			if(d[i] < 0.3):
				continue
			border1.append(c[i])
		for i in range(len(e)):
			if(f[i] < 0.3):
				continue
			border2.append(e[i])
		positions = self.getYposForText(border,border1,border2,maxi)
		'''
		fig = plt.figure(figsize = (12,8))
 		ax = fig.add_subplot(111)
		plt.plot(b,a,"gx",label = "Pre-developed Catchment")
		plt.plot(d,c,"r+",label = "Urbanised Catchment no treatment")
		plt.plot(f,e,"b.",label = "Post WSUD")
		plt.yscale("log")
		plt.xscale("log")
		plt.plot([0.25, 0.25],ax.get_ylim(), 'b-', lw=2, label = "~1 in 3 months >> Stormwater\nquality improvement")
		plt.plot([0.5, 0.5], ax.get_ylim(), 'y-', lw=2, label = "~1 in 6 months >> Managing \nstormwater as a resource")
		plt.plot([1, 1], ax.get_ylim(), color = 'brown',linestyle = '-', lw=2, label = "~1 in 12 months >> Reducing hydrological\ndisturbance in urban waterway")
		plt.plot([2, 2], ax.get_ylim(), 'k-', lw=2 , label = "~1 in 24 months >> Waterway geomorphic\nprotection")
		plt.title(" ")
		fig.canvas.set_window_title('SEI Peak flows')
		plt.ylabel(u"Flow m³/s")
		plt.xlabel("Plotting Position (ARI)")
		plt.text(0.01,ax.get_ylim()[1]/5,"SEI Urbanised = " + str(round(self.module.SEIurb,2)) + "\nSEI WSUD = " + str(round(self.module.SEIwsud,2)), backgroundcolor = "white")
		#plt.text(0.3,maxi,"~1 in 3 months >> Stormwater quality improvement",size = "small")#,backgroundcolor = "b",color = "white", picker = True)
		#plt.text(0.6,maxi/10,"~1 in 6 months >> Managing stormwater as a resource",size = "small")#,backgroundcolor = "y", picker = True)
		#plt.text(1,maxi/100,"~1 in 12 months >> Reducing hydrological\ndisturbance in urban waterway",size = "small")#,backgroundcolor = "brown", picker = True)
		#plt.text(2,maxi/1000,"~1 in 24 months >> Waterway geomorphic\nprotection",size = "small")#, backgroundcolor = "k", color = "white", picker = True)
		plt.legend(loc = "best",prop={"size":8})
		plt.grid(True, which="both",ls="-",color="#939393")
		xlim = ax.get_xlim()
		plt.xlim([0.01,xlim[1]])
		plt.show()
		plt.savefig(str(workpath) + 'SEIplot.png')	
	def plotSEI2(self):
		params = {'legend.fontsize': 8,'legend.linewidth': 2,'legend.labelspacing':0.2}
		mpl.rcParams.update(params)
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		filename = workpath + "SEItable.txt"#QtGui.QFileDialog.getOpenFileName(self, "Open MUSIC Output File", workpath,self.tr("Text Files (*.txt)"))
		mpl.rcParams['toolbar'] = 'None'
		i = 0
		urb = 0.0
		bars = []
		tmpbar = []
		xlabel = []
		xlabel.append("Urbanised")
		if os.path.exists(filename):
			f = open(filename,'r')
			for line in f:
				linearr = line.strip('\n').split(',')
				urb = round(float(linearr[2]))
				tmpbar.append(round(float(linearr[3])))
				xlabel.append(str(linearr[0]))
				i = i + 1
			f.close()
			xlabel.append("Natural")
			n = i+2
			ind = np.arange(n)
			space = 0.25
			width = 0.75 / i
			bars.append(urb)
			for val in tmpbar:
				bars.append(val)
			bars.append(1)
			print bars
			fig = plt.figure()
			ax = fig.add_subplot(111)
			figbars = ax.bar(ind,bars,color = '#3399FF')
			figbars[0].set_color('#CC3300')
			figbars[n-1].set_color('#66FF33')
			ax.set_ylabel('Stream Erosion index (SEI)')
			ax.set_title('Stream Erosion Index')
			ax.set_xticks(ind+(width*i)*0.75)
			ax.set_xticklabels(xlabel)
			plt.plot(ax.get_xlim(),[1,1], color = 'brown',linestyle = '--', lw=2, label = "SEI strech limit")
			plt.plot(ax.get_xlim(),[3,3], 'b--', lw=2, label = "SEI lower limit")
			plt.plot(ax.get_xlim(),[5,5], 'k--', lw=2, label = "SEI upper limit")
			#plt.text(ax.get_xlim()[1],1,"SEI stretch limit", backgroundcolor = "white")
			ax.legend()# (bars1[0],bars2[0],bars3[0]) , ('Option 1', 'Option 2', 'Option 3') )
			ax.legend(loc='best')
			#plt.xlim([0,100])
			fig.canvas.set_window_title('SEI Indices') 
			fig.autofmt_xdate()
			plt.grid(True, which="both",ls="-",color="#939393")
			plt.ylim([0,int(urb)+1])
			plt.show()
			plt.savefig(str(workpath) + 'SEIindicesPlot.png')
		else:
			print "No SEI file found!!!"
	def loadUtilFile(self):
		vec = []
		f = open(self.UtilFile,"r")
		for line in f:
			linearr = line.strip('\n').split(',')
			tmpbar = (round(float(linearr[0]),2),round(float(linearr[1]),2),round(float(linearr[2]),2),round(float(linearr[3]),2),round(float(linearr[4]),2),round(float(linearr[5]),2),round(float(linearr[6]),2))
			vec.append(tmpbar)
		f.close()
		return vec
	def writeUtilFile(self,vec):
		f = open(self.UtilFile,"w")
		for i in range(len(vec)):
			f.write(str(vec[i][0])+","+str(vec[i][1])+","+str(vec[i][2])+","+str(vec[i][3])+","+str(vec[i][4])+","+str(vec[i][5])+","+str(vec[i][6])+"\n")
		f.close()
	def readSEItable(self,filename):
		arr = []
		f = open(filename,"r")
		for line in f:
			linearr = line.strip("\n").split(",")
			tmp = []
			tmp.append(float(linearr[0]))
			tmp.append(float(linearr[1]))
			arr.append(tmp)
		f.close()
		return arr
	def getYposForText(self,arr1,arr2,arr3, maxi):
		#arr1.sort()
		#arr2.sort()
		#arr3.sort()
		skip1 = False
		skip2 = False
		skip3 = False
		jump = False
		append = True
		step = math.log(maxi,10)
		positions = []
		cursor = 0.0
		cursor = maxi #-(maxi - math.pow(10,step-0.3))
		while(len(positions)<4):
			print jump
			print "maxi: " + str(maxi) 
			print "cursor: " + str(cursor)
			if (jump):
				while(jump):
					if (cursor - (maxi - math.pow(10,(step-0.3))) <= maxi/10):
						maxi = maxi / 10.0
						cursor = maxi
						step = math.log(maxi,10)
					else:
						cursor = cursor - (maxi - math.pow(10,step-0.3))
						jump = False
			else:
				cursor = cursor - (maxi - math.pow(10,step-0.3))
			append = True
			for i in range(len(arr1)):
				if(cursor > arr1[i] or skip1):
					pass
				else:
					skip1 = True
					cursor = arr1[0]
					jump = True
					append = False
					break
			if (append):
				continue
			for i in range(len(arr2)):
				if(cursor > arr2[i] or skip2):
					pass
				else:
					skip2 = True
					cursor = arr2[0]
					jump = True
					append = False
					break
			if (append):
				continue
			for i in range(len(arr3)):
				if(cursor > arr3[i] or skip3):
					pass
				else:
					skip3 = True
					cursor = arr3[0]
					jump = True
					append = False
					break
			if (append):
				continue
			positions.append(cursor)


		print positions
		return positions
