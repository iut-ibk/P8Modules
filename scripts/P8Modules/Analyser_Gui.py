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
			linearr = line.strip('\n').split(',')
			tmpbar = (round(float(linearr[1])),round(float(linearr[2])),round(float(linearr[3])),round(float(linearr[4])))
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
