# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from pydynamind import *
from PyQt4.QtCore import QSettings, QFileInfo
from importMSFgui import Ui_importMSFDialog
import platform
from shutil import copyfile


class activateimportMSFGUI(QtGui.QDialog):
	def __init__(self, m, parent=None):
		self.module = Module
		self.module = m
		QtGui.QDialog.__init__(self, parent)
		self.ui = Ui_importMSFDialog()
		self.ui.setupUi(self)
		self.ui.le_r.setText(self.module.getParameterAsString("Filename"))
		QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_values)
		QtCore.QObject.connect(self.ui.pb_r, QtCore.SIGNAL("released()"), self.load)

	def save_values(self):
		Filename = str(self.ui.le_r.text())
		self.module.setParameterValue("Filename", Filename)
	def load(self):
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		datapath = settings.value("dataPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
			datapath = datapath.replace("/","\\")
		filename = QtGui.QFileDialog.getOpenFileName(self, "Select Music File",  datapath, self.tr("Text Files (*.msf)"))
		if(filename != ""):
			self.module.setParameterValue("Filename", str(QFileInfo(filename).fileName()))
			self.ui.le_r.setText(QFileInfo(filename).fileName())
			settings.setValue("dataPath",QFileInfo(filename).absolutePath())
			copyfile(filename,workpath + QFileInfo(filename).fileName())