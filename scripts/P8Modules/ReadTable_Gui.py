from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QSettings, QFileInfo
from pydynamind import *
from Ui_ReadTable_Dialog import Ui_ReadTable_GUI
import shlex
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os.path
import os
import platform
from shutil import copyfile


class ReadTable_Gui(QtGui.QDialog):
    def __init__(self, m, parent=None):
        self.module = Module
        self.module = m
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_ReadTable_GUI()
        self.ui.setupUi(self)
	self.tmpFile = "TPRtable.txt"
	QtCore.QObject.connect(self.ui.pb_r, QtCore.SIGNAL("released()"),self.load)
	QtCore.QObject.connect(self.ui.pb_del, QtCore.SIGNAL("released()"),self.delete)

    def delete(self):
	if os.path.exists(self.tmpFile):
	    os.remove(self.tmpFile)
    def load(self):
	settings = QSettings()
	workpath = settings.value("workPath").toString() + "/"
	datapath = settings.value("dataPath").toString() + "/"
	if (platform.system() != "Linux"):
		workpath = workpath.replace("/","\\")
		datapath = datapath.replace("/","\\")
	filename = QtGui.QFileDialog.getOpenFileName(self, "Open MUSIC Output File", datapath,self.tr("Text Files (*.txt)"))
	if(filename != ""):
		finfo = QFileInfo(filename)
		self.ui.le_r.setText(QFileInfo(filename).fileName())
		settings.setValue("dataPath",finfo.absolutePath())
		if(os.path.exists(workpath + finfo.fileName())):
			selectedpath = str(finfo.absolutePath() + "/")
			if(platform.system() != "Linux"):
				selectedpath = selectedpath.replace("/","\\")
			if(selectedpath != str(workpath)):
				os.remove(str(workpath) + str(finfo.fileName()))
				copyfile(filename, str(workpath) + str(finfo.fileName()))
		else:
			copyfile(filename,str(workpath) + str(finfo.fileName()))
		self.loadTable(str(workpath) + str(finfo.fileName()))

    def loadTable(self,filename):
	'''mpl.rcParams['toolbar'] = 'None'
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
	if os.path.exists(self.tmpFile):
	    f = open(self.tmpFile,'r')
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
	f = open(self.tmpFile,'w')
	f.write("1,"+str(bars1[0])+","+str(bars1[1])+","+str(bars1[2])+","+str(bars1[3])+"\n")
	if (show2):	
	    f.write("2,"+str(bars2[0])+","+str(bars2[1])+","+str(bars2[2])+","+str(bars2[3])+"\n")	
	if (show3):
	    f.write("2,"+str(bars3[0])+","+str(bars3[1])+","+str(bars3[2])+","+str(bars3[3])+"\n")
	f.close()
	'''
	settings = QSettings()
	if (settings.value("Music").toString().contains("MUSIC 5")):
		music5 = True
	else:
		music5 = False

	f = open(filename,'r')
	text = shlex.shlex(f.read(),posix = True)
	text.whitespace = ','
	text.whitespace += '\n'
	text.whitespace_split = True
	liste = list(text)
	i = 0
	colnr = 0
	rownr = 0
	rowcounter = self.ui.table.rowCount()
	colcounter = self.ui.table.columnCount()
	for rows in range(rowcounter):
		if(i >= len(liste)):
			break
		if rows == 2:
			if(music5):
				i = i + 4
				continue
		for cols in range(colcounter):
			widget = QtGui.QLineEdit(str(liste[i]))
			if rows == 0:
				font = QtGui.QFont()
				font.setBold(True)		
				widget.setFont(font)
			elif cols !=0:
				widget = QtGui.QLineEdit(str(float(liste[i])))
			self.ui.table.setCellWidget(rownr,colnr,widget)
			colnr = colnr + 1
			i = i + 1
		rownr = rownr + 1
		colnr = 0