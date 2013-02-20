from PyQt4 import QtCore, QtGui
from pydynamind import *
from Ui_Analyser_Dialog import Ui_Analyser_GUI
import shlex
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os.path
import os

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

    def plotEBR(self):
	mpl.rcParams['toolbar'] = 'None'
	f = open(self.EBRFile,'r')
	#print f.readlines().strip('\n').split(',')
	show1 = False
	show2 = False
	show3 = False
	i = 0
	for line in f:
	    linearr = line.strip('\n').split(',')
	    tmpbar = (round(float(linearr[1])),round(float(linearr[2])),round(float(linearr[3])),round(float(linearr[4])))
	    if (int(line[0]) == 1):
		bars1 = tmpbar
		show1 = True
	    elif (int(line[0]) == 2):
		bars2 = tmpbar
		show2 = True
	    elif (int(line[0]) == 3):
		bars3 = tmpbar
		show3 = True
	    i = i+0.5
	f.close()
	n = 4
	ind = np.arange(n)
	width = 0.25
	
	fig = plt.figure()
	ax = fig.add_subplot(111)
	if (show1):
	    rects1 = ax.bar(ind,bars1,width,color = '#1f99d0')
	    rects1.set_label('Option 1')
	if (show2):
	    rects2 = ax.bar(ind+width,bars2,width,color='#8fcce7')
	    rects2.set_label('Option 2')
	if (show3):
	    rects3 = ax.bar(ind+width*2,bars3,width,color='#abcd8f')
	    rects3.set_label('Option 3')

	ax.set_ylabel('Enviromental Benefit(%)')
	ax.set_title('Stream Health Outcomes')
	ax.set_xticks(ind+width*i)
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

	f = open(filename,'r')
	text = shlex.shlex(f.read(),posix = True)
	text.whitespace = ','
	text.whitespace += '\n'
	text.whitespace_split = True
	liste = list(text)
	bars1 = (round(float(liste[7])),round(float(liste[15])),round(float(liste[19])),round(float(liste[23])))
	f.close
	if os.path.exists(self.TPRFile):
	    f = open(self.TPRFile,'r')
	    for line in f:
	        linearr = line.strip('\n').split(',')
	        tmpbar = (round(float(linearr[1])),round(float(linearr[2])),round(float(linearr[3])),round(float(linearr[4])))
	        if (int(line[0]) == 1):
		    bars2 = tmpbar
		    show2 = True
	        elif (int(line[0]) == 2):
		    bars3 = tmpbar
		    show3 = True
	    f.close()

	n = 4
	ind = np.arange(n)
	width = 0.25
	
	fig = plt.figure()
	ax = fig.add_subplot(111)
	rects1 = ax.bar(ind,bars1,width,color = '#1f99d0')
	rects1.set_label('Option 1')
	if (show2):
	    rects2 = ax.bar(ind+width,bars2,width,color='#8fcce7')
	    rects2.set_label('Option 2')
	if (show3):
	    rects3 = ax.bar(ind+width*2,bars3,width,color='#abcd8f')
	    rects3.set_label('Option 3')

	ax.set_ylabel('Reduction(%)')
	ax.set_title('Treatment/Harvesting')
	ax.set_xticks(ind+width*2)
	ax.set_xticklabels( ('Volume' , 'TSS' , 'TP' , 'TN') )
	ax.legend()# (bars1[0],bars2[0],bars3[0]) , ('Option 1', 'Option 2', 'Option 3') )
	ax.legend(loc='best')
	#plt.xlim([0,100])
	fig.canvas.set_window_title(' ') 
	fig.autofmt_xdate()
	plt.ylim([0,100])
	plt.show()
	f = open(self.TPRFile,'w')
	f.write("1,"+str(bars1[0])+","+str(bars1[1])+","+str(bars1[2])+","+str(bars1[3])+"\n")
	if (show2):	
	    f.write("2,"+str(bars2[0])+","+str(bars2[1])+","+str(bars2[2])+","+str(bars2[3])+"\n")	
	if (show3):
	    f.write("2,"+str(bars3[0])+","+str(bars3[1])+","+str(bars3[2])+","+str(bars3[3])+"\n")
	f.close()
