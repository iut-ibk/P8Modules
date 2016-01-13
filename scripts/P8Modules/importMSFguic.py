# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from pydynamind import *
from PyQt4.QtCore import QSettings, QFileInfo
from importMSFgui import Ui_importMSFDialog
import platform
from shutil import copyfile
from Tkinter import *
import tkMessageBox
import os.path



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
		self.errmsg = ""

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
			window = Tk()
			window.wm_withdraw()
			window.geometry('700x700')#+str(window.winfo_screenwidth()/2+400)+"+"+str(window.winfo_screenheight()/2))
			if(self.checkForFile(filename)):
				self.module.setParameterValue("Filename", str(QFileInfo(filename).fileName()))
				self.ui.le_r.setText(QFileInfo(filename).fileName())
				settings.setValue("dataPath",QFileInfo(filename).absolutePath())
				copyfile(filename,workpath + QFileInfo(filename).fileName())
				tkMessageBox.showinfo(title="File load", message="MUSIC project loaded successfully")
			else:
				tkMessageBox.showinfo(title="File load", message="The Climate Files in the provided msf couldnt be found:\n" + self.errmsg)
			window.destroy()
	def checkForFile(self,filename):
		if(platform.system() == "Linux"):
			return True
		missingFiles = False
		filesToCheck = []
		f = open(filename,"r")
		for line in f:
			linearr = line.strip("\n").split(",")
			if(linearr[0] == "MeteorologicalTemplate"):
				filesToCheck.append(str(linearr[1]))
			if(linearr[0] == "RainfallFile"):
				filesToCheck.append(str(linearr[1]))
			if(linearr[0] == "PETFile"):
				filesToCheck.append(str(linearr[1]))
		print filesToCheck
		for f in filesToCheck:
			if not (os.path.exists(f)):
				self.errmsg += f + " "
				missingFiles = True
		if(missingFiles):
			return False
		else:
			return True