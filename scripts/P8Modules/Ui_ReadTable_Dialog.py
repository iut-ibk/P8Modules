# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rain_gui.ui'
#
# Created: Fri Aug 03 14:40:58 2012
# by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import shlex
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ReadTable_GUI(object):
    def setupUi(self, ReadTable_GUI):
        ReadTable_GUI.setObjectName(_fromUtf8("ReadTable_GUI"))
        ReadTable_GUI.resize(565, 310)
        ReadTable_GUI.setWindowTitle(QtGui.QApplication.translate("ReadTable_GUI", "Data Table", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(ReadTable_GUI)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(ReadTable_GUI)
        self.groupBox.setTitle(QtGui.QApplication.translate("ReadTable_GUI", "Data Table", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("ReadTable_GUI", "Music Output File", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.le_r = QtGui.QLineEdit(self.groupBox)
        self.le_r.setObjectName(_fromUtf8("le_r"))
        self.gridLayout.addWidget(self.le_r, 0, 1, 1, 1)
	self.pb_r = QtGui.QPushButton(self.groupBox)
        self.pb_r.setText(QtGui.QApplication.translate("ReadTable_GUI", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_r.setObjectName(_fromUtf8("pb_r"))
        self.gridLayout.addWidget(self.pb_r, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
	self.table = QtGui.QTableWidget(ReadTable_GUI)
	self.table.setRowCount(6)
	self.table.setColumnCount(4)
	self.table.setColumnWidth(0,210)
	self.table.setColumnWidth(2,110)
	self.f = open('Perf_TTE.txt','r')
	self.text = shlex.shlex(self.f.read(),posix = True)
	self.text.whitespace = ','
	self.text.whitespace += '\n'
	self.text.whitespace_split = True
	self.list = list(self.text)
	i = 0
	for rows in range(self.table.rowCount()):
	    if rows ==2:
		i=i+4	
	    for cols in range(self.table.columnCount()):
		widget = QtGui.QLineEdit(str(self.list[i]))
		if rows == 0:
			font = QtGui.QFont()
			font.setBold(True)		
			widget.setFont(font)
		elif cols !=0:
			widget = QtGui.QLineEdit(str(float(self.list[i])))
		self.table.setCellWidget(rows,cols,widget)
		i = i + 1
	self.verticalLayout.addWidget(self.table)
        self.buttonBox = QtGui.QDialogButtonBox(ReadTable_GUI)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ReadTable_GUI)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ReadTable_GUI.accept)
        QtCore.QMetaObject.connectSlotsByName(ReadTable_GUI)

    def retranslateUi(self, ReadTable_GUI):
        pass
