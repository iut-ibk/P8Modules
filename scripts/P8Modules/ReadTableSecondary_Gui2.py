from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QSettings
from pydynamind import *
from Ui_ReadTableSecondary_Dialog2 import Ui_ReadTableSecondary_GUI2
import shlex
from Tkinter import Tk
import matplotlib.pyplot as plt
import numpy as np
import shlex
import matplotlib as mpl
import platform

class ReadTableSecondary_Gui2(QtGui.QDialog):
    def __init__(self, m, parent=None):
        self.module = Module
        self.module = m
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_ReadTableSecondary_GUI2()
        self.ui.setupUi(self)
	QtCore.QObject.connect(self.ui.pb_load, QtCore.SIGNAL("released()"),self.Load)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save)
	QtCore.QObject.connect(self.ui.pb_export, QtCore.SIGNAL("released()"),self.export)
	QtCore.QObject.connect(self.ui.pb_clipboard, QtCore.SIGNAL("released()"),self.copyToClipboard)
	#QtCore.QObject.connect(self.ui.pb_plot, QtCore.SIGNAL("released()"),self.plot)
	self.ui.city_combo.setCurrentIndex(int(self.module.getParameterAsString("SimulationCity")))

    def save(self):
	city = self.ui.city_combo.currentIndex()
	self.module.setParameterValue("SimulationCity",str(city))
	pass
	
    def Load(self):
	widget = QtGui.QLineEdit(str("Stream Hydrology and Water quality"))
	font = QtGui.QFont()
	font.setBold(True)
	widget.setFont(font)
	self.ui.table.setCellWidget(0,0,widget)
	self.ui.table.setCellWidget(1,0,QtGui.QLineEdit(str("Flow-Frequency Index (%)")))
	self.ui.table.setCellWidget(2,0,QtGui.QLineEdit(str("Volume Reduction Index (%)")))
	self.ui.table.setCellWidget(3,0,QtGui.QLineEdit(str("Filtered Flow Volume Index (%)")))
	self.ui.table.setCellWidget(4,0,QtGui.QLineEdit(str("Water Quality Index (%)")))
	for i in range(len(self.module.FF)):
	    i = i + 1
	    widget2 = QtGui.QLineEdit(str("Realisation"))# + str(i))
	    font2 = QtGui.QFont()
	    font2.setBold(True)
	    widget2.setFont(font)
	    self.ui.table.setCellWidget(0,i,widget2)
	    self.ui.table.setCellWidget(1,i,QtGui.QLineEdit(str(self.module.FF[i-1])))
	    self.ui.table.setCellWidget(2,i,QtGui.QLineEdit(str(self.module.VR[i-1])))
	    self.ui.table.setCellWidget(3,i,QtGui.QLineEdit(str(self.module.FV[i-1])))
	    self.ui.table.setCellWidget(4,i,QtGui.QLineEdit(str(self.module.WQ[i-1])))

    def export(self):
	settings = QSettings()
	workpath = settings.value("workPath").toString() + "/"
	if (platform.system() != "Linux"):
		workpath = workpath("/","\\")
	f = open(workpath + 'EnvironmentalBenefit.csv','w')
	f.write("Stream Hydrology and Water quality,%\n")
	f.write("Flow-Frequency Index," + str(self.module.FF) + "\n")
	f.write("Volume Reduction Index," + str(self.module.VR) + "\n")
	f.write("Filtered Flow Volume Index," +str(self.module.FV) + "\n")
	f.write("Water Quality Index," + str(self.module.WQ) + "\n")
	f.close()
    def plot(self):
	'''mpl.rcParams['toolbar'] = 'None'
	f = open('EBRtable.txt','r')
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
	'''

    def copyToClipboard(self):
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append("Stream Hydrology and Water quality\t%\nFlow-Frequency Index\t" + str(self.module.FF) + 
	"\nVolume Reduction Index\t" + str(self.module.VR) + 
	"\nFiltered Flow Volume Index\t" +str(self.module.FV) + 
	"\nWater Quality Index\t" + str(self.module.WQ) + "\n")




