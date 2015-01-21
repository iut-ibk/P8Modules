from PyQt4 import QtCore, QtGui
from pydynamind import *
from Ui_Analyser_Dialog import Ui_Analyser_GUI
import shlex
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os.path
import os
import random

class Analyser_Gui(QtGui.QDialog):
	def __init__(self,m,parent=None):
		self.module = Module
		self.module = m
		QtGui.QDialog.__init__(self,parent)
		self.ui = Ui_Analyser_GUI()
		self.ui.setupUi(self)
		self.TPRFile = "TPRtable.txt"
		self.EBRFile = "EBRtable.txt"
		QtCore.QObject.connect(self.ui.pb_plotEBR, QtCore.SIGNAL("released()"),self.plotEBR)
		QtCore.QObject.connect(self.ui.pb_plotTPR, QtCore.SIGNAL("released()"),self.plotTPR)
		QtCore.QObject.connect(self.ui.pb_delete, QtCore.SIGNAL("released()"),self.delete)
		QtCore.QObject.connect(self.ui.pb_plotUtil, QtCore.SIGNAL("released()"),self.plotUtil)
		self.colorarr = ['#0b09ae','#b01717','#37c855','#cf33e1','#ffff00','#896161','#e5e5e5','#d81417','#FF4500','#000000','#FFFFFF']
	def delete(self):
		if os.path.exists(self.TPRFile):
			os.remove(self.TPRFile)
	def plotEBR(self):
		random.seed()
		mpl.rcParams['toolbar'] = 'None'
		f = open(self.EBRFile,'r')
		#print f.readlines().strip('\n').split(',')
		show1 = False
		show2 = False
		show3 = False
		i = 0
		bars = []
		for line in f:
			if(i == 0):
				i = i+1
				continue
			linearr = line.strip('\n').split(',')
			tmpbar = (round(float(linearr[4])),round(float(linearr[5])),round(float(linearr[6])),round(float(linearr[7])))
			arr2 = [tmpbar,linearr[0]]
			bars.append(arr2)
			'''
			if (int(line[0]) == 1):
				bars1 = tmpbar
				show1 = True
			elif (int(line[0]) == 2):
				bars2 = tmpbar
				show2 = True
			elif (int(line[0]) == 3):
				bars3 = tmpbar
				show3 = True
			'''
			i = i+1
		f.close()
		ind = np.arange(4)
		print bars[0]
		print ind
		space = 0.25
		if (i == 0):
			width = space
		else:
			width = 0.75 / i

		fig = plt.figure()
		ax = fig.add_subplot(111)
		j = 0
		#tmpaxes = []
		for bar in bars:
			tmp = ax.bar(ind + width * j,bar[0],width,color = self.colorarr[j])
			tmp.set_label('Realisation ' + str(bar[1]))
			j = j + 1
			#tmpaxes.append(ax)
		'''
		if (show1):
			rects1 = ax.bar(ind,bars1,width,color = '#1f99d0')
			rects1.set_label('Realisation 1')
		if (show2):
			rects2 = ax.bar(ind+width,bars2,width,color='#8fcce7')
			rects2.set_label('Realisation 2')
		if (show3):
			rects3 = ax.bar(ind+width*2,bars3,width,color='#abcd8f')
			rects3.set_label('Realisation 3')
		'''
		ax.set_ylabel('Enviromental Benefit(%)')
		ax.set_title('Stream Health Outcomes')
		ax.set_xticks(ind+(width*i)*0.75)
		ax.set_xticklabels( ('FF' , 'VR' , 'FVg' , 'WQ') )

		ax.legend()# (bars1[0],bars2[0],bars3[0]) , ('Option 1', 'Option 2', 'Option 3') )
		ax.legend(loc='best')
		fig.canvas.set_window_title(' ') 
		#plt.xlim([0,100])
		#fig.autofmt_xdate()
		plt.ylim([0,100])
		plt.show()
		plt.savefig('EviromentalBenefitsPlot.png')
		
	def plotTPR(self):
		filename = QtGui.QFileDialog.getOpenFileName(self, "Open MUSIC Output File", "Open New File",self.tr("Text Files (*.txt)"))
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
		number = filename[len(filename)-5]
		bars = []
		bars1 = (round(float(liste[7])),round(float(liste[15])),round(float(liste[19])),round(float(liste[23])))
		bars.append([bars1,number])
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

		n = 4
		ind = np.arange(n)
		space = 0.25
		width = 0.75 / i
		j = 0
		fig = plt.figure()
		ax = fig.add_subplot(111)
		for bar in bars:
			tmp = ax.bar(ind + width * j,bar[0],width,color = self.colorarr[j])
			tmp.set_label('Realisation ' + str(bar[1]))
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
		plt.savefig('TreatmentPerformancePlot.png')
	def plotUtil(self):
		mpl.rcParams['toolbar'] = 'None'
		ResultVec = []
		fig = plt.figure()
		ax = fig.add_subplot(111)
		for i in self.module.Utilvec:
			f = open("UB_BasinStrategy No 1-" + str(i) + ".csv",'r')
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
			ResultVec.append((allsums*100,BF,PB,IS,WSUR,SW))
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

		for i in range(len(ResultVec)):
			BFvec.append(ResultVec[i][1])
			PBvec.append(ResultVec[i][2])
			ISvec.append(ResultVec[i][3])
			WSURvec.append(ResultVec[i][4])
			SWvec.append(ResultVec[i][5])
			if(ResultVec[i][1] > 0):
				BfFlag = True
			if(ResultVec[i][2] > 0):
				PbFlag = True
			if(ResultVec[i][3] > 0):
				IsFlag = True
			if(ResultVec[i][4] > 0):
				WsurFlag = True
			if(ResultVec[i][5] > 0):
				SwFlag = True


		ind = np.arange(self.module.runs)
		width = 0.9 / self.module.runs
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
		for i in range(self.module.runs):
			xticksvec.append("Realisation " + str(i+1) + "\n" + str('%.2f' % ResultVec[i][0]) + "%")
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
				SWstring += str('%.2f' % SWstring[i] + "%,")
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
		plt.savefig('UtilisationsPlot.png')
		f = open("util.csv", "w")
		f.write(outtxt)
		f.close()
