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

class Ui_ReadTableSecondary_GUI(object):
    def setupUi(self, ReadTableSecondary_GUI):
        ReadTableSecondary_GUI.setObjectName(_fromUtf8("ReadTableSecondary_GUI"))
        ReadTableSecondary_GUI.resize(500, 310)
        ReadTableSecondary_GUI.setWindowTitle(QtGui.QApplication.translate("ReadTableSecondary_GUI", "Data Table", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(ReadTableSecondary_GUI)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(ReadTableSecondary_GUI)
        self.groupBox.setTitle(QtGui.QApplication.translate("ReadTableSecondary_GUI", "Performance Table", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI", "Music Output File Nr.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.le_r = QtGui.QLineEdit(self.groupBox)
        self.le_r.setObjectName(_fromUtf8("le_r"))
        self.gridLayout.addWidget(self.le_r, 0, 1, 1, 1)
	self.pb_load = QtGui.QPushButton(self.groupBox)
        self.pb_load.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_load.setObjectName(_fromUtf8("pb_load"))
        self.gridLayout.addWidget(self.pb_load, 0, 2, 1, 1)
	self.pb_export = QtGui.QPushButton(self.groupBox)
	self.pb_export.setText(QtGui.QApplication.translate("ReadTabelSecondary_Gui", "Export", None, QtGui.QApplication.UnicodeUTF8))
	self.pb_export.setObjectName(_fromUtf8("pb_export"))
	self.gridLayout.addWidget(self.pb_export)
	self.pb_clipboard = QtGui.QPushButton(self.groupBox)
	self.pb_clipboard.setText(QtGui.QApplication.translate("ReadTabelSecondary_Gui", "copy to Clipboard", None, QtGui.QApplication.UnicodeUTF8))
	self.pb_clipboard.setObjectName(_fromUtf8("pb_clipboard"))
	self.gridLayout.addWidget(self.pb_clipboard)
        self.verticalLayout.addWidget(self.groupBox)
	self.table = QtGui.QTableWidget(ReadTableSecondary_GUI)
	self.table.setRowCount(5)
	self.table.setColumnCount(2)
	self.table.setColumnWidth(0,210)
	self.table.setColumnWidth(1,210)
	self.verticalLayout.addWidget(self.table)
        self.buttonBox = QtGui.QDialogButtonBox(ReadTableSecondary_GUI)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ReadTableSecondary_GUI)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ReadTableSecondary_GUI.accept)
        QtCore.QMetaObject.connectSlotsByName(ReadTableSecondary_GUI)

    def retranslateUi(self, ReadTableSecondary_GUI):
        pass
