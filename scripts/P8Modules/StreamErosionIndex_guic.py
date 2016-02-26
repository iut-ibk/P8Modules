# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QSettings, QFileInfo
from pydynamind import *
from StreamErosionIndex_gui import Ui_StreamErosionIndexDialog
import platform
from shutil import copyfile


class activateStreamErosionIndexGUI(QtGui.QDialog):
	def __init__(self, m, parent=None):
		self.module = Module
		self.module = m
		QtGui.QDialog.__init__(self, parent)

		self.ui = Ui_StreamErosionIndexDialog()
		self.ui.setupUi(self)
		self.ui.le_r.setText(self.module.getParameterAsString("Csvfile"))
		self.ui.le_r2.setText(self.module.getParameterAsString("ETfile"))
		self.ui.le_r3.setText(self.module.getParameterAsString("MusicTemplateFile"))
		self.ui.le_A.setValue(float(self.module.getParameterAsString("alpha")))
		self.ui.le_NoY.setValue(int(self.module.getParameterAsString("NoY")))
		self.ui.city_combo.setCurrentIndex(int(self.module.getParameterAsString("SimulationCity")))
		self.ui.chkb_music.setChecked(int(self.module.getParameterAsString("useMusic")))
		self.ui.chkb_defaults.setChecked(int(self.module.getParameterAsString("useDefaults")))
		self.ui.chkb_UB.setChecked(int(self.module.getParameterAsString("useUB")))
		QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_values)
		QtCore.QObject.connect(self.ui.pb_r, QtCore.SIGNAL("released()"), self.load)
		QtCore.QObject.connect(self.ui.pb_r2, QtCore.SIGNAL("released()"), self.load2)
		QtCore.QObject.connect(self.ui.pb_r3, QtCore.SIGNAL("released()"), self.load3)
		self.ui.city_combo.currentIndexChanged['QString'].connect(self.cityChanged)
		self.ui.chkb_music.stateChanged['int'].connect(self.chkb_music_change)
		self.ui.chkb_defaults.stateChanged['int'].connect(self.chkb_defaults_change)
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

	def save_values(self):
		Filename = str(self.ui.le_r.text())
		self.module.setParameterValue("Csvfile", Filename)
		Filename = str(self.ui.le_r2.text())
		self.module.setParameterValue("ETfile",Filename)
		Filename = str(self.ui.le_r3.text())
		self.module.setParameterValue("MusicTemplateFile", Filename)
		city = self.ui.city_combo.currentIndex()
		self.module.setParameterValue("SimulationCity",str(city))
		self.module.setParameterValue("alpha",str(self.ui.le_A.text()))
		self.module.setParameterValue("NoY", str(self.ui.le_NoY.text()))
		self.module.setParameterValue("useMusic",str(int(self.ui.chkb_music.isChecked())))
		self.module.setParameterValue("useDefaults",str(int(self.ui.chkb_defaults.isChecked())))
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
		if(self.ui.chkb_UB.isChecked()):
			self.module.setParameterValue("useUB",str(1))
		else:
			self.module.setParameterValue("useUB",str(0))
	def cityChanged(self):
		
		if self.ui.city_combo.currentIndex() == 0:
			self.ui.le_rainthres.setText("1")
			self.ui.le_rainsoil.setText("120")
			self.ui.le_raininitial.setText("30")
			self.ui.le_rainfield.setText("80")
			self.ui.le_raininfil.setText("200")
			self.ui.le_raininfil2.setText("1")
			self.ui.le_raindepth.setText("10")
			self.ui.le_rainrecharge.setText("25")
			self.ui.le_rainbaseflow.setText("5")
			self.ui.le_raindeep.setText("0")
		elif self.ui.city_combo.currentIndex() == 1:
			self.ui.le_rainthres.setText("1")
			self.ui.le_rainsoil.setText("200")
			self.ui.le_raininitial.setText("30")
			self.ui.le_rainfield.setText("170")
			self.ui.le_raininfil.setText("200")
			self.ui.le_raininfil2.setText("1")
			self.ui.le_raindepth.setText("10")
			self.ui.le_rainrecharge.setText("25")
			self.ui.le_rainbaseflow.setText("5")
			self.ui.le_raindeep.setText("0")
		elif self.ui.city_combo.currentIndex() == 2:
			self.ui.le_rainthres.setText("1")
			self.ui.le_rainsoil.setText("40")
			self.ui.le_raininitial.setText("30")
			self.ui.le_rainfield.setText("25")
			self.ui.le_raininfil.setText("200")
			self.ui.le_raininfil2.setText("1")
			self.ui.le_raindepth.setText("10")
			self.ui.le_rainrecharge.setText("25")
			self.ui.le_rainbaseflow.setText("5")
			self.ui.le_raindeep.setText("0")
		elif self.ui.city_combo.currentIndex() == 3:
			self.ui.le_rainthres.setText("1")
			self.ui.le_rainsoil.setText("60")
			self.ui.le_raininitial.setText("30")
			self.ui.le_rainfield.setText("20")
			self.ui.le_raininfil.setText("200")
			self.ui.le_raininfil2.setText("1")
			self.ui.le_raindepth.setText("10")
			self.ui.le_rainrecharge.setText("25")
			self.ui.le_rainbaseflow.setText("5")
			self.ui.le_raindeep.setText("0")
		elif self.ui.city_combo.currentIndex() == 4:
			self.ui.le_rainthres.setText("1")
			self.ui.le_rainsoil.setText("30")
			self.ui.le_raininitial.setText("30")
			self.ui.le_rainfield.setText("20")
			self.ui.le_raininfil.setText("200")
			self.ui.le_raininfil2.setText("1")
			self.ui.le_raindepth.setText("10")
			self.ui.le_rainrecharge.setText("25")
			self.ui.le_rainbaseflow.setText("5")
			self.ui.le_raindeep.setText("0")
		elif self.ui.city_combo.currentIndex() == 5:
			self.ui.le_rainthres.setText("1")
			self.ui.le_rainsoil.setText("40")
			self.ui.le_raininitial.setText("30")
			self.ui.le_rainfield.setText("30")
			self.ui.le_raininfil.setText("200")
			self.ui.le_raininfil2.setText("1")
			self.ui.le_raindepth.setText("10")
			self.ui.le_rainrecharge.setText("25")
			self.ui.le_rainbaseflow.setText("5")
			self.ui.le_raindeep.setText("0")
		elif self.ui.city_combo.currentIndex() == 6:
			self.ui.le_rainthres.setText("1")
			self.ui.le_rainsoil.setText("250")
			self.ui.le_raininitial.setText("30")
			self.ui.le_rainfield.setText("230")
			self.ui.le_raininfil.setText("200")
			self.ui.le_raininfil2.setText("1")
			self.ui.le_raindepth.setText("10")
			self.ui.le_rainrecharge.setText("25")
			self.ui.le_rainbaseflow.setText("5")
			self.ui.le_raindeep.setText("0")
		elif self.ui.city_combo.currentIndex() == 7:
			self.ui.le_rainthres.setText("0")
			self.ui.le_rainsoil.setText("0")
			self.ui.le_raininitial.setText("0")
			self.ui.le_rainfield.setText("0")
			self.ui.le_raininfil.setText("0")
			self.ui.le_raininfil2.setText("0")
			self.ui.le_raindepth.setText("0")
			self.ui.le_rainrecharge.setText("0")
			self.ui.le_rainbaseflow.setText("0")
			self.ui.le_raindeep.setText("0")
		
		self.ui.le_NoY.setValue(10)
		self.ui.le_A.setValue(0.4)
	def load(self):
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		datapath = settings.value("dataPath").toString() + "/"

		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
			datapath = datapath.replace("/","\\")
		filename = QtGui.QFileDialog.getOpenFileName(self, "Select Csv File", datapath, self.tr("Csv Files (*.csv)"))
		if(filename != ""):
			self.module.setParameterValue("Csvfile", str(QFileInfo(filename).fileName()))
			self.ui.le_r.setText(QFileInfo(filename).fileName())
			settings.setValue("dataPath",QFileInfo(filename).absolutePath())
			copyfile(filename,workpath + QFileInfo(filename).fileName())
	def load2(self):
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		datapath = settings.value("dataPath").toString() + "/"

		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
			datapath = datapath.replace("/","\\")
		filename = QtGui.QFileDialog.getOpenFileName(self, "Select ET File", datapath, self.tr("Text Files (*.txt)"))
		if(filename != ""):
			self.module.setParameterValue("ETfile", str(QFileInfo(filename).fileName()))
			self.ui.le_r2.setText(QFileInfo(filename).fileName())
			settings.setValue("dataPath",QFileInfo(filename).absolutePath())
			copyfile(filename,workpath + QFileInfo(filename).fileName())
	def load3(self):
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		datapath = settings.value("dataPath").toString() + "/"

		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
			datapath = datapath.replace("/","\\")
		filename = QtGui.QFileDialog.getOpenFileName(self, "Select MUSIC template File", datapath, self.tr("Text Files (*.mlb)"))
		if(filename != ""):
			self.module.setParameterValue("MusicTemplateFile", str(QFileInfo(filename).fileName()))
			self.ui.le_r3.setText(QFileInfo(filename).fileName())
			settings.setValue("dataPath",QFileInfo(filename).absolutePath())
			copyfile(filename,workpath + QFileInfo(filename).fileName())
	def chkb_music_change(self):
		if(self.ui.chkb_music.isChecked() == 1):
			self.ui.chkb_defaults.setChecked(int(False))
	def chkb_defaults_change(self):
		if(self.ui.chkb_defaults.isChecked() == 1):
			self.ui.chkb_music.setChecked(int(False))