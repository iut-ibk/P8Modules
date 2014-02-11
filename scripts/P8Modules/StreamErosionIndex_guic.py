# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QSettings
from pydynamind import *
from StreamErosionIndex_gui import Ui_StreamErosionIndexDialog
import platform


class activateStreamErosionIndexGUI(QtGui.QDialog):
	def __init__(self, m, parent=None):
		self.module = Module
		self.module = m
		QtGui.QDialog.__init__(self, parent)

		self.ui = Ui_StreamErosionIndexDialog()
		self.ui.setupUi(self)
		self.ui.le_r.setText(self.module.getParameterAsString("Csvfile"))
		self.ui.le_r2.setText(self.module.getParameterAsString("ETfile"))
		self.ui.le_A.setValue(float(self.module.getParameterAsString("alpha")))
		self.ui.le_NoY.setValue(int(self.module.getParameterAsString("NoY")))
		self.ui.city_combo.setCurrentIndex(int(self.module.getParameterAsString("SimulationCity")))
		self.ui.chkb_music.setChecked(int(self.module.getParameterAsString("useMusic")))
		self.ui.chkb_defaults.setChecked(int(self.module.getParameterAsString("useDefaults")))
		QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_values)
		QtCore.QObject.connect(self.ui.pb_r, QtCore.SIGNAL("released()"), self.load)
		QtCore.QObject.connect(self.ui.pb_r2, QtCore.SIGNAL("released()"), self.load2)
		self.ui.chkb_music.stateChanged['int'].connect(self.chkb_music_change)
		self.ui.chkb_defaults.stateChanged['int'].connect(self.chkb_defaults_change)


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

	def load(self):
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		filename = QtGui.QFileDialog.getOpenFileName(self, "Select Csv File", workpath, self.tr("Csv Files (*.csv)"))
		self.ui.le_r.setText(filename)
	def load2(self):
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		filename = QtGui.QFileDialog.getOpenFileName(self, "Select ET File", workpath, self.tr("Text Files (*.txt)"))
		self.ui.le_r2.setText(filename)
	def load3(self):
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		filename = QtGui.QFileDialog.getOpenFileName(self, "Select MUSIC template File", workpath, self.tr("Text Files (*.mlb)"))
		self.ui.le_r3.setText(filename)
	def chkb_music_change(self):
		if(self.ui.chkb_music.isChecked() == 1):
			self.ui.chkb_defaults.setChecked(int(False))
	def chkb_defaults_change(self):
		if(self.ui.chkb_defaults.isChecked() == 1):
			self.ui.chkb_music.setChecked(int(False))