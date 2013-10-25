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
		self.ui.le_A.setText(self.module.getParameterAsString("alpha"))
		self.ui.le_NoY.setText(self.module.getParameterAsString("NoY"))
		self.ui.city_combo.setCurrentIndex(int(self.module.getParameterAsString("SimulationCity")))

		QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_values)
		QtCore.QObject.connect(self.ui.pb_r, QtCore.SIGNAL("released()"), self.load)
		QtCore.QObject.connect(self.ui.pb_r2, QtCore.SIGNAL("released()"), self.load2)

	def save_values(self):
		Filename = str(self.ui.le_r.text())
		self.module.setParameterValue("Csvfile", Filename)
		Filename = str(self.ui.le_r2.text())
		self.module.setParameterValue("ETfile",Filename)
		city = self.ui.city_combo.currentIndex()
		self.module.setParameterValue("SimulationCity",str(city))
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
