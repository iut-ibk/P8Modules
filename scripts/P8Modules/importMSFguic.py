# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from pydynamind import *
from importMSFgui import Ui_importMSFDialog

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
		filename = QtGui.QFileDialog.getOpenFileName(self, "Select Music File", "Open new file", self.tr("Text Files (*.msf)"))
		self.ui.le_r.setText(filename)