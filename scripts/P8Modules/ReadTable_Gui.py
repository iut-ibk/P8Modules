from PyQt4 import QtCore, QtGui
from pydynamind import *
from Ui_ReadTable_Dialog import Ui_ReadTable_GUI
import shlex
class ReadTable_Gui(QtGui.QDialog):
    def __init__(self, m, parent=None):
        self.module = Module
        self.module = m
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_ReadTable_GUI()
        self.ui.setupUi(self)
	QtCore.QObject.connect(self.ui.pb_r, QtCore.SIGNAL("released()"),self.load)

    def load(self):
	filename = QtGui.QFileDialog.getOpenFileName(self, "Open MUSIC Output File", "Open New File",self.tr("Text Files (*.txt)"))
	self.module.setParameterValue("FileName",str(filename))	
	self.loadTable(filename)
	
    def loadTable(self,filename):
	f = open(filename,'r')
	text = shlex.shlex(f.read(),posix = True)
	text.whitespace = ','
	text.whitespace += '\n'
	text.whitespace_split = True
	liste = list(text)
	i = 0
	for rows in range(self.ui.table.rowCount()):
	    if rows ==2:
		i=i+4	
	    for cols in range(self.ui.table.columnCount()):
		widget = QtGui.QLineEdit(str(liste[i]))
		if rows == 0:
			font = QtGui.QFont()
			font.setBold(True)		
			widget.setFont(font)
		elif cols !=0:
			widget = QtGui.QLineEdit(str(float(liste[i])))
		self.ui.table.setCellWidget(rows,cols,widget)
		i = i + 1
