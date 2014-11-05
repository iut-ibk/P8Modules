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
	self.ui.city_combo.currentIndexChanged['QString'].connect(self.cityChanged)
	QtCore.QObject.connect(self.ui.pb_clipboard, QtCore.SIGNAL("released()"),self.copyToClipboard)
	self.ui.vol_combo.currentIndexChanged['QString'].connect(self.volChanged)
	self.ui.city_combo.setCurrentIndex(int(self.module.getParameterAsString("SimulationCity")))
	self.ui.vol_combo.setCurrentIndex(int(self.module.getParameterAsString("VolumeReductionIndex")))
	self.ui.spb_vol.setValue(int(self.module.getParameterAsString("VolumeReduction")))
	self.ui.spb_city.setValue(int(self.module.getParameterAsString("AnnualUserRain")))
	self.ui.spb_freq.setValue(int(self.module.getParameterAsString("FrequencyRunoffDays")))
	self.ui.spb_base.setValue(float(self.module.getParameterAsString("Base")))
	self.ui.le_tss.setValue(float(self.module.getParameterAsString("TssTarget")))
	self.ui.le_tp.setValue(float(self.module.getParameterAsString("TpTarget")))
	self.ui.le_tn.setValue(float(self.module.getParameterAsString("TnTarget")))
	self.ui.chkb_flux.setChecked(int(self.module.getParameterAsString("ConsiderFluxes")))
	self.ui.chkb_ub.setChecked(int(self.module.getParameterAsString("useUB")))
	self.ui.le_rainthres.setText((self.module.getParameterAsString("RainThres")))
	self.ui.le_rainsoil.setText((self.module.getParameterAsString("RainSoil")))
	self.ui.le_raininitial.setText((self.module.getParameterAsString("RainInitial")))
	self.ui.le_rainfield.setText((self.module.getParameterAsString("RainField")))
	self.ui.le_raininfil.setText((self.module.getParameterAsString("RainInfil")))
	self.ui.le_raininfil2.setText((self.module.getParameterAsString("RainInfil2")))
	self.ui.le_raindepth.setText((self.module.getParameterAsString("RainDepth")))
	self.ui.le_rainrecharge.setText((self.module.getParameterAsString("RainRecharge")))
	self.ui.le_rainbaseflow.setText((self.module.getParameterAsString("RainBaseflow")))
	self.ui.le_raindeep.setText((self.module.getParameterAsString("RainDeep")))
	#self.setMouseTracking(True)
	#self.ui.label_base.installEventFilter(self)

	'''
    def eventFilter(self, source, event):
	if source is self.ui.label_base:
		if event.type() == QtCore.QEvent.MouseMove:
			pos = event.globalPos()
			print('pos: %d, %d' % (pos.x(), pos.y()))
		elif event.type() == QtCore.QEvent.Enter:
			#print('ENTER')
		elif event.type() == QtCore.QEvent.Leave:
			#print('LEAVE')
		return QtGui.QWidget.eventFilter(self, source, event)
	'''
    def save(self):
	city = self.ui.city_combo.currentIndex()
	self.module.setParameterValue("AnnualUserRain",str(self.ui.spb_city.value()))
	self.module.setParameterValue("VolumeReduction",str(self.ui.spb_vol.value()))
	self.module.setParameterValue("SimulationCity",str(city))
	self.module.setParameterValue("VolumeReductionIndex",str(self.ui.vol_combo.currentIndex()))
	self.module.setParameterValue("FrequencyRunoffDays",str(self.ui.spb_freq.value()))
	self.module.setParameterValue("Base",str(self.ui.spb_base.value()))
	self.module.setParameterValue("UseTargets",str(1))
	self.module.setParameterValue("TssTarget",str(self.ui.le_tss.text()))
	self.module.setParameterValue("TnTarget",str(self.ui.le_tn.text()))
	self.module.setParameterValue("TpTarget",str(self.ui.le_tp.text()))
	self.module.setParameterValue("RainThres",str(self.ui.le_rainthres.text()))
	self.module.setParameterValue("RainSoil",str(self.ui.le_rainsoil.text()))
	self.module.setParameterValue("RainInitial",str(self.ui.le_raininitial.text()))
	self.module.setParameterValue("RainField",str(self.ui.le_rainfield.text()))
	self.module.setParameterValue("RainInfil",str(self.ui.le_raininfil.text()))
	self.module.setParameterValue("RainInfil2",str(self.ui.le_raininfil2.text()))
	self.module.setParameterValue("RainDepth",str(self.ui.le_raindepth.text()))
	self.module.setParameterValue("RainRecharge",str(self.ui.le_rainrecharge.text()))
	self.module.setParameterValue("RainBaseflow",str(self.ui.le_rainbaseflow.text()))
	self.module.setParameterValue("RainDeep",str(self.ui.le_raindeep.text()))
	if(self.ui.chkb_flux.isChecked()):
		self.module.setParameterValue("ConsiderFluxes",str(1))
	else:
		self.module.setParameterValue("ConsiderFluxes",str(0))
	if(self.ui.chkb_ub.isChecked()):
		self.module.setParameterValue("useUB",str(1))
	else:
		self.module.setParameterValue("useUB",str(0))
	pass
	
    def Load(self):
	widget = QtGui.QLineEdit(str("Stream Hydrology and Water quality"))
	font = QtGui.QFont()
	font.setBold(True)
	widget.setFont(font)
	self.ui.table.setCellWidget(0,0,widget)
	self.ui.table.setCellWidget(1,0,QtGui.QLineEdit(str("Considered infiltration fluxes?")))
	self.ui.table.setCellWidget(2,0,QtGui.QLineEdit(str("Number of runoff days in the natural catchement (days/year)")))
	self.ui.table.setCellWidget(3,0,QtGui.QLineEdit(str("Baseflow rate allowed in the WSUD catchment(m3/s)")))
	self.ui.table.setCellWidget(4,0,QtGui.QLineEdit(str("Frequency of Runoff Days (days/year)")))
	self.ui.table.setCellWidget(5,0,QtGui.QLineEdit(str("Proportion of Total Volume Reduction (%)")))
	self.ui.table.setCellWidget(6,0,QtGui.QLineEdit(str("Proportion of Filtered Flow Volume  (%)")))
	self.ui.table.setCellWidget(7,0,QtGui.QLineEdit(str("TSS mean concentration (mg/L)")))
	self.ui.table.setCellWidget(8,0,QtGui.QLineEdit(str("TP mean concentration (mg/L)")))
	self.ui.table.setCellWidget(9,0,QtGui.QLineEdit(str("TN mean concentration (mg/L)")))

	for i in range(len(self.module.FF)):
	    i = i + 1
	    widget2 = QtGui.QLineEdit(str("Realisation"))# + str(i))
	    font2 = QtGui.QFont()
	    font2.setBold(True)
	    widget2.setFont(font)
	    self.ui.table.setCellWidget(0,i,widget2)
	    if(int(self.module.getParameterAsString("ConsiderFluxes"))):
	    	self.ui.table.setCellWidget(1,i,QtGui.QLineEdit(str("Yes")))
	    else:
	    	self.ui.table.setCellWidget(1,i,QtGui.QLineEdit(str("No")))
	    self.ui.table.setCellWidget(2,i,QtGui.QLineEdit(str(self.module.FreqPredev)))
	    self.ui.table.setCellWidget(3,i,QtGui.QLineEdit(str(self.module.cin)))
	    self.ui.table.setCellWidget(4,i,QtGui.QLineEdit(str(self.module.FF[i-1])))
	    self.ui.table.setCellWidget(5,i,QtGui.QLineEdit(str(self.module.VR[i-1])))
	    self.ui.table.setCellWidget(6,i,QtGui.QLineEdit(str(self.module.FV[i-1])))
	    self.ui.table.setCellWidget(7,i,QtGui.QLineEdit(str(self.module.tableTSS[i-1])))
	    self.ui.table.setCellWidget(8,i,QtGui.QLineEdit(str(self.module.tableTP[i-1])))
	    self.ui.table.setCellWidget(9,i,QtGui.QLineEdit(str(self.module.tableTN[i-1])))


    def cityChanged(self):
	if self.ui.city_combo.currentIndex() == 0:
		self.ui.spb_city.setValue(1149)
		self.ui.le_rainsoil.setText("120")
		self.ui.le_rainfield.setText("80")
	elif self.ui.city_combo.currentIndex() == 1:
		self.ui.spb_city.setValue(1212)
		self.ui.le_rainsoil.setText("200")
		self.ui.le_rainfield.setText("170")
	elif self.ui.city_combo.currentIndex() == 2:
		self.ui.spb_city.setValue(632)
		self.ui.le_rainsoil.setText("40")
		self.ui.le_rainfield.setText("25")
	elif self.ui.city_combo.currentIndex() == 3:
		self.ui.spb_city.setValue(649)
		self.ui.le_rainsoil.setText("30")
		self.ui.le_rainfield.setText("20")
	elif self.ui.city_combo.currentIndex() == 4:
		self.ui.spb_city.setValue(614)
		self.ui.le_rainsoil.setText("30")
		self.ui.le_rainfield.setText("20")
	elif self.ui.city_combo.currentIndex() == 5:
		self.ui.spb_city.setValue(545)
		self.ui.le_rainsoil.setText("40")
		self.ui.le_rainfield.setText("30")
	elif self.ui.city_combo.currentIndex() == 6:
		self.ui.spb_city.setValue(730)
		self.ui.le_rainsoil.setText("250")
		self.ui.le_rainfield.setText("23")
	elif self.ui.city_combo.currentIndex() == 7:
		self.ui.spb_city.setValue(0)

    def volChanged(self):
	if self.ui.vol_combo.currentIndex() == 0:
		self.ui.spb_vol.setValue(20)
	elif self.ui.vol_combo.currentIndex() == 1:
		self.ui.spb_vol.setValue(60)
	elif self.ui.vol_combo.currentIndex() == 2:
		self.ui.spb_vol.setValue(0)
    def export(self):
	settings = QSettings()
	workpath = settings.value("workPath").toString() + "/"
	if (platform.system() != "Linux"):
		workpath = workpath.replace("/","\\")
	f = open(workpath + 'EnvironmentalBenefit.csv','w')
	f.write("Stream Hydrology and Water quality,%\n")
	if(int(self.module.getParameterAsString("ConsiderFluxes"))):
		f.write("Considered infiltration fluxes?," + str("Yes") + "\n")
	else:
		f.write("Considered infiltration fluxes?," + str("No") + "\n")
	f.write("Number of runoff days in the natural catchement (days/year)," + str(self.module.FreqPredev) + "\n")
	f.write("Baseflow rate allowed in the WSUD catchment(m3/s)," + str(self.module.cin) + "\n")
	f.write("Frequency of Runoff Days (days/year)," + str(self.module.FF) + "\n")
	f.write("Proportion of Total Volume Reduction (%)," + str(self.module.VR) + "\n")
	f.write("Proportion of Filtered Flow Volume  (%)," +str(self.module.FV) + "\n")
	f.write("TSS mean concentration (mg/L)," + str(self.module.tableTSS)+"\n")
	f.write("TP mean concentration (mg/L)," + str(self.module.tableTP)+"\n")
	f.write("TN mean concentration (mg/L)," + str(self.module.tableTN)+"\n")
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
	r.clipboard_append("Stream Hydrology and Water quality\t%\nFrequency of Runoff Days (days/year)\t" + str(self.module.FF) + 
	"\nProportion of Total Volume Reduction (%)\t" + str(self.module.VR) + 
	"\nProportion of Filtered Flow Volume \t" +str(self.module.FV) + 
	"\nWater Quality Index\t" + str(self.module.WQ) +
	"\nTSS mean concentration (mg/L)\t" + str(self.module.tableTSS) + 
	"\nTP mean concentration (mg/L)\t" + str(self.module.tableTP) + 
	"\nTN mean concentration (mg/L)\t" + str(self.module.tableTN)+"\n")