from PyQt4 import QtCore, QtGui
from pydynamind import *
from Ui_ReadTableSecondary_Dialog import Ui_ReadTableSecondary_GUI
import shlex
from Tkinter import Tk
class ReadTableSecondary_Gui(QtGui.QDialog):
    def __init__(self, m, parent=None):
        self.module = Module
        self.module = m
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_ReadTableSecondary_GUI()
        self.ui.setupUi(self)
	QtCore.QObject.connect(self.ui.pb_load, QtCore.SIGNAL("released()"),self.Load)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save)
	QtCore.QObject.connect(self.ui.pb_export, QtCore.SIGNAL("released()"),self.export)
	QtCore.QObject.connect(self.ui.pb_clipboard, QtCore.SIGNAL("released()"),self.copyToClipboard)
    def save(self):
        filename = str(self.ui.le_r.text())
        self.module.setParameterValue("FileName", filename)
	
    def Load(self):
	widget = QtGui.QLineEdit(str("Enviromental Benefit"))
	font = QtGui.QFont()
	font.setBold(True)	
	widget.setFont(font)
	widget2 = QtGui.QLineEdit(str("%"))
	font2 = QtGui.QFont()
	font2.setBold(True)	
	widget2.setFont(font)
	self.ui.table.setCellWidget(0,0,widget)
	self.ui.table.setCellWidget(1,0,QtGui.QLineEdit(str("Flow-Frequency Index")))
	self.ui.table.setCellWidget(2,0,QtGui.QLineEdit(str("Volume Reduction Index")))
	self.ui.table.setCellWidget(3,0,QtGui.QLineEdit(str("Filtered Flow Volume Index")))
	self.ui.table.setCellWidget(4,0,QtGui.QLineEdit(str("Water Quality Index")))
	self.ui.table.setCellWidget(0,1,widget2)
	self.ui.table.setCellWidget(1,1,QtGui.QLineEdit(str(self.module.FF)))
	self.ui.table.setCellWidget(2,1,QtGui.QLineEdit(str(self.module.VR)))
	self.ui.table.setCellWidget(3,1,QtGui.QLineEdit(str(self.module.FV)))
	self.ui.table.setCellWidget(4,1,QtGui.QLineEdit(str(self.module.WQ)))
    def export(self):
	f = open('TableSecondaryExport.csv','w')
	f.write("Enviromental Benefit,%\n")
	f.write("Flow-Frequency Index," + str(self.module.FF) + "\n")
	f.write("Volume Reduction Index," + str(self.module.VR) + "\n")
	f.write("Filtered Flow Volume Index," +str(self.module.FV) + "\n")
	f.write("Water Quality Index," + str(self.module.WQ) + "\n")
	f.close()
    def copyToClipboard(self):
	print " drin"
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append("Enviromental Benefit\t%\nFlow-Frequency Index\t" + str(self.module.FF) + 
	"\nVolume Reduction Index\t" + str(self.module.VR) + 
	"\nFiltered Flow Volume Index\t" +str(self.module.FV) + 
	"\nWater Quality Index\t" + str(self.module.WQ) + "\n")




