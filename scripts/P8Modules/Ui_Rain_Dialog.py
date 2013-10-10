# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rain_gui.ui'
#
# Created: Fri Aug 03 14:40:58 2012
# by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_P8Rain_GUI(object):
    def setupUi(self, P8Rain_GUI):
        P8Rain_GUI.setObjectName(_fromUtf8("P8Rain_GUI"))
        P8Rain_GUI.resize(456, 143)
        P8Rain_GUI.setWindowTitle(QtGui.QApplication.translate("P8Rain_GUI", "Rain", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(P8Rain_GUI)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(P8Rain_GUI)
        self.groupBox.setTitle(QtGui.QApplication.translate("P8Rain_GUI", "Data setup", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("P8Rain_GUI", "Rain (netCDF)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.le_r = QtGui.QLineEdit(self.groupBox)
        self.le_r.setObjectName(_fromUtf8("le_r"))
        self.gridLayout.addWidget(self.le_r, 0, 1, 1, 1)
        self.pb_r = QtGui.QPushButton(self.groupBox)
        self.pb_r.setText(QtGui.QApplication.translate("P8Rain_GUI", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_r.setObjectName(_fromUtf8("pb_r"))
        self.gridLayout.addWidget(self.pb_r, 0, 2, 1, 1)
        self.pb_preview = QtGui.QPushButton(self.groupBox)
        self.pb_preview.setText(QtGui.QApplication.translate("P8Rain_GUI", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_preview.setObjectName(_fromUtf8("pb_preview"))
        self.gridLayout.addWidget(self.pb_preview, 1, 2, 1, 1)

        self.labelcsv = QtGui.QLabel(self.groupBox)
        self.labelcsv.setText(QtGui.QApplication.translate("P8Rain_GUI", "Rain (CSV)", None, QtGui.QApplication.UnicodeUTF8))
        self.labelcsv.setObjectName(_fromUtf8("labelcsv"))
        self.gridLayout.addWidget(self.labelcsv, 2, 0, 1, 1)
        self.le_csv = QtGui.QLineEdit(self.groupBox)
        self.le_csv.setObjectName(_fromUtf8("le_csv"))
        self.gridLayout.addWidget(self.le_csv, 2, 1, 1, 1)
        self.pb_csv = QtGui.QPushButton(self.groupBox)
        self.pb_csv.setText(QtGui.QApplication.translate("P8Rain_GUI", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_csv.setObjectName(_fromUtf8("pb_csv"))
        self.gridLayout.addWidget(self.pb_csv, 2, 2, 1, 1)

        self.labelET = QtGui.QLabel(self.groupBox)
        self.labelET.setText(QtGui.QApplication.translate("P8Rain_GUI", "ET file", None, QtGui.QApplication.UnicodeUTF8))
        self.labelET.setObjectName(_fromUtf8("labelET"))
        self.gridLayout.addWidget(self.labelET, 3, 0, 1, 1)
        self.le_ET = QtGui.QLineEdit(self.groupBox)
        self.le_ET.setObjectName(_fromUtf8("le_ET"))
        self.gridLayout.addWidget(self.le_ET, 3, 1, 1, 1)
        self.pb_ET = QtGui.QPushButton(self.groupBox)
        self.pb_ET.setText(QtGui.QApplication.translate("P8Rain_GUI", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_ET.setObjectName(_fromUtf8("pb_Et"))
        self.gridLayout.addWidget(self.pb_ET, 3, 2, 1, 1)

        self.labelCoordX = QtGui.QLabel(self.groupBox)
        self.labelCoordX.setText(QtGui.QApplication.translate("P8Rain_GUI", "X Coordinate", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCoordX.setObjectName(_fromUtf8("labelCoordX"))
        self.gridLayout.addWidget(self.labelCoordX, 4, 0, 1, 1)
        self.le_CoordX = QtGui.QLineEdit(self.groupBox)
        self.le_CoordX.setObjectName(_fromUtf8("le_CoordX"))
        self.gridLayout.addWidget(self.le_CoordX, 4, 1, 1, 1)

        self.labelCoordY = QtGui.QLabel(self.groupBox)
        self.labelCoordY.setText(QtGui.QApplication.translate("P8Rain_GUI", "Y Coordinate", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCoordY.setObjectName(_fromUtf8("labelCoordY"))
        self.gridLayout.addWidget(self.labelCoordY, 5, 0, 1, 1)
        self.le_CoordY = QtGui.QLineEdit(self.groupBox)
        self.le_CoordY.setObjectName(_fromUtf8("le_CoordY"))
        self.gridLayout.addWidget(self.le_CoordY, 5, 1, 1, 1)

        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(P8Rain_GUI)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(P8Rain_GUI)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), P8Rain_GUI.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), P8Rain_GUI.reject)
        QtCore.QMetaObject.connectSlotsByName(P8Rain_GUI)

    def retranslateUi(self, P8Rain_GUI):
        pass
