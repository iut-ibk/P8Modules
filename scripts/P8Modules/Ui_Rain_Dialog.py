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
        P8Rain_GUI.setWindowTitle(QtGui.QApplication.translate("P8Rain_GUI", "Data Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(P8Rain_GUI)
        #self.verticalLayout.setTitle(QtGui.QApplication.translate("P8Rain_GUI", "Data Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        # Group Box Top
        self.groupBoxTop = QtGui.QGroupBox(P8Rain_GUI)
        self.groupBoxTop.setTitle(QtGui.QApplication.translate("P8Rain_GUI", "Rainfall Project Data", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxTop.setObjectName(_fromUtf8("groupBoxTop"))
        self.gridLayoutTop = QtGui.QGridLayout(self.groupBoxTop)
        self.gridLayoutTop.setObjectName(_fromUtf8("gridLayoutTop"))
        self.label = QtGui.QLabel(self.groupBoxTop)
        self.label.setText(QtGui.QApplication.translate("P8Rain_GUI", "Rain (netCDF)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayoutTop.addWidget(self.label, 0, 0, 1, 1)
        self.le_r = QtGui.QLineEdit(self.groupBoxTop)
        self.le_r.setObjectName(_fromUtf8("le_r"))
        self.gridLayoutTop.addWidget(self.le_r, 0, 1, 1, 1)
        self.pb_r = QtGui.QPushButton(self.groupBoxTop)
        self.pb_r.setText(QtGui.QApplication.translate("P8Rain_GUI", "Import File", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_r.setObjectName(_fromUtf8("pb_r"))
        self.gridLayoutTop.addWidget(self.pb_r, 0, 2, 1, 1)
        self.pb_preview = QtGui.QPushButton(self.groupBoxTop)
        self.pb_preview.setText(QtGui.QApplication.translate("P8Rain_GUI", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_preview.setObjectName(_fromUtf8("pb_preview"))
        self.gridLayoutTop.addWidget(self.pb_preview, 1, 2, 1, 1)

        #Group Box Mid
        self.groupBoxMid = QtGui.QGroupBox(P8Rain_GUI)
        self.groupBoxMid.setObjectName(_fromUtf8("groupBoxMid"))
        self.gridLayoutMid = QtGui.QGridLayout(self.groupBoxMid)
        self.gridLayoutMid.setObjectName(_fromUtf8("gridLayoutMid"))

        self.labelCoordX = QtGui.QLabel(self.groupBoxMid)
        self.labelCoordX.setText(QtGui.QApplication.translate("P8Rain_GUI", "Longitude Coordinate", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCoordX.setObjectName(_fromUtf8("labelCoordX"))
        self.gridLayoutMid.addWidget(self.labelCoordX, 0, 2, 1, 1)
        self.labelCoordY = QtGui.QLabel(self.groupBoxMid)
        self.labelCoordY.setText(QtGui.QApplication.translate("P8Rain_GUI", "Latitude Coordinate", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCoordY.setObjectName(_fromUtf8("labelCoordY"))
        self.gridLayoutMid.addWidget(self.labelCoordY, 0, 3, 1, 1)

        self.radio1 = QtGui.QRadioButton(self.groupBoxMid)
        self.radio1.setObjectName(_fromUtf8("radio1"))
        self.gridLayoutMid.addWidget(self.radio1,1,0,1,1)
        self.lblLoc1 = QtGui.QLabel(self.groupBoxMid)
        self.lblLoc1.setText(QtGui.QApplication.translate("P8Rain_GUI", "Location 1", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLoc1.setObjectName(_fromUtf8("lblLoc1"))
        self.gridLayoutMid.addWidget(self.lblLoc1,1,1,1,1)
        self.le_CoordX1 = QtGui.QLineEdit(self.groupBoxMid)
        self.le_CoordX1.setObjectName(_fromUtf8("le_CoordX1"))
        self.gridLayoutMid.addWidget(self.le_CoordX1, 1, 2, 1, 1)
        self.le_CoordY1 = QtGui.QLineEdit(self.groupBoxMid)
        self.le_CoordY1.setObjectName(_fromUtf8("le_CoordY1"))
        self.gridLayoutMid.addWidget(self.le_CoordY1, 1, 3, 1, 1)

        self.radio2 = QtGui.QRadioButton(self.groupBoxMid)
        self.radio2.setObjectName(_fromUtf8("radio2"))
        self.gridLayoutMid.addWidget(self.radio2,2,0,1,1)
        self.lblLoc2 = QtGui.QLabel(self.groupBoxMid)
        self.lblLoc2.setText(QtGui.QApplication.translate("P8Rain_GUI", "Location 2", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLoc2.setObjectName(_fromUtf8("lblLoc2"))
        self.gridLayoutMid.addWidget(self.lblLoc2,2,1,1,1)
        self.le_CoordX2 = QtGui.QLineEdit(self.groupBoxMid)
        self.le_CoordX2.setObjectName(_fromUtf8("le_CoordX2"))
        self.gridLayoutMid.addWidget(self.le_CoordX2, 2, 2, 1, 1)
        self.le_CoordY2 = QtGui.QLineEdit(self.groupBoxMid)
        self.le_CoordY2.setObjectName(_fromUtf8("le_CoordY2"))
        self.gridLayoutMid.addWidget(self.le_CoordY2, 2, 3, 1, 1)

        self.radio3 = QtGui.QRadioButton(self.groupBoxMid)
        self.radio3.setObjectName(_fromUtf8("radio3"))
        self.gridLayoutMid.addWidget(self.radio3,3,0,1,1)
        self.lblLoc3 = QtGui.QLabel(self.groupBoxMid)
        self.lblLoc3.setText(QtGui.QApplication.translate("P8Rain_GUI", "Location 3", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLoc3.setObjectName(_fromUtf8("lblLoc3"))
        self.gridLayoutMid.addWidget(self.lblLoc3,3,1,1,1)
        self.le_CoordX3 = QtGui.QLineEdit(self.groupBoxMid)
        self.le_CoordX3.setObjectName(_fromUtf8("le_CoordX3"))
        self.gridLayoutMid.addWidget(self.le_CoordX3, 3, 2, 1, 1)
        self.le_CoordY3 = QtGui.QLineEdit(self.groupBoxMid)
        self.le_CoordY3.setObjectName(_fromUtf8("le_CoordY3"))
        self.gridLayoutMid.addWidget(self.le_CoordY3, 3, 3, 1, 1)

        self.radio4 = QtGui.QRadioButton(self.groupBoxMid)
        self.radio4.setObjectName(_fromUtf8("radio4"))
        self.gridLayoutMid.addWidget(self.radio4,4,0,1,1)
        self.lblLoc4 = QtGui.QLabel(self.groupBoxMid)
        self.lblLoc4.setText(QtGui.QApplication.translate("P8Rain_GUI", "Location 4", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLoc4.setObjectName(_fromUtf8("lblLoc4"))
        self.gridLayoutMid.addWidget(self.lblLoc4,4,1,1,1)
        self.le_CoordX4 = QtGui.QLineEdit(self.groupBoxMid)
        self.le_CoordX4.setObjectName(_fromUtf8("le_CoordX4"))
        self.gridLayoutMid.addWidget(self.le_CoordX4, 4, 2, 1, 1)
        self.le_CoordY4 = QtGui.QLineEdit(self.groupBoxMid)
        self.le_CoordY4.setObjectName(_fromUtf8("le_CoordY4"))
        self.gridLayoutMid.addWidget(self.le_CoordY4, 4, 3, 1, 1)

        self.radio5 = QtGui.QRadioButton(self.groupBoxMid)
        self.radio5.setObjectName(_fromUtf8("radio5"))
        self.gridLayoutMid.addWidget(self.radio5,5,0,1,1)
        self.lblLoc5 = QtGui.QLabel(self.groupBoxMid)
        self.lblLoc5.setText(QtGui.QApplication.translate("P8Rain_GUI", "Location 5", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLoc5.setObjectName(_fromUtf8("lblLoc5"))
        self.gridLayoutMid.addWidget(self.lblLoc5,5,1,1,1)
        self.le_CoordX5 = QtGui.QLineEdit(self.groupBoxMid)
        self.le_CoordX5.setObjectName(_fromUtf8("le_CoordX5"))
        self.gridLayoutMid.addWidget(self.le_CoordX5, 5, 2, 1, 1)
        self.le_CoordY5 = QtGui.QLineEdit(self.groupBoxMid)
        self.le_CoordY5.setObjectName(_fromUtf8("le_CoordY5"))
        self.gridLayoutMid.addWidget(self.le_CoordY5, 5, 3, 1, 1)

        self.radio6 = QtGui.QRadioButton(self.groupBoxMid)
        self.radio6.setObjectName(_fromUtf8("radio6"))
        self.gridLayoutMid.addWidget(self.radio6,6,0,1,1)
        self.lblLoc6 = QtGui.QLabel(self.groupBoxMid)
        self.lblLoc6.setText(QtGui.QApplication.translate("P8Rain_GUI", "Location 6", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLoc6.setObjectName(_fromUtf8("lblLoc6"))
        self.gridLayoutMid.addWidget(self.lblLoc6,6,1,1,1)
        self.le_CoordX6 = QtGui.QLineEdit(self.groupBoxMid)
        self.le_CoordX6.setObjectName(_fromUtf8("le_CoordX6"))
        self.gridLayoutMid.addWidget(self.le_CoordX6, 6, 2, 1, 1)
        self.le_CoordY6 = QtGui.QLineEdit(self.groupBoxMid)
        self.le_CoordY6.setObjectName(_fromUtf8("le_CoordY6"))
        self.gridLayoutMid.addWidget(self.le_CoordY6, 6, 3, 1, 1)

        #Group Box Bot
        self.groupBoxBot = QtGui.QGroupBox(P8Rain_GUI)
        self.groupBoxBot.setTitle(QtGui.QApplication.translate("P8Rain_GUI", "Or import user defined rainfall and evapotransportation data", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxBot.setObjectName(_fromUtf8("groupBoxBot"))
        self.gridLayoutBot = QtGui.QGridLayout(self.groupBoxBot)
        self.gridLayoutBot.setObjectName(_fromUtf8("gridLayoutBot"))

        self.labelcsv = QtGui.QLabel(self.groupBoxBot)
        self.labelcsv.setText(QtGui.QApplication.translate("P8Rain_GUI", "Rain (CSV)", None, QtGui.QApplication.UnicodeUTF8))
        self.labelcsv.setObjectName(_fromUtf8("labelcsv"))
        self.gridLayoutBot.addWidget(self.labelcsv, 0, 0, 1, 1)
        self.le_csv = QtGui.QLineEdit(self.groupBoxBot)
        self.le_csv.setObjectName(_fromUtf8("le_csv"))
        self.gridLayoutBot.addWidget(self.le_csv, 0, 1, 1, 1)
        self.pb_csv = QtGui.QPushButton(self.groupBoxBot)
        self.pb_csv.setText(QtGui.QApplication.translate("P8Rain_GUI", "Import File", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_csv.setObjectName(_fromUtf8("pb_csv"))
        self.gridLayoutBot.addWidget(self.pb_csv, 0, 2, 1, 1)

        self.labelET = QtGui.QLabel(self.groupBoxBot)
        self.labelET.setText(QtGui.QApplication.translate("P8Rain_GUI", "ET file", None, QtGui.QApplication.UnicodeUTF8))
        self.labelET.setObjectName(_fromUtf8("labelET"))
        self.gridLayoutBot.addWidget(self.labelET, 1, 0, 1, 1)
        self.le_ET = QtGui.QLineEdit(self.groupBoxBot)
        self.le_ET.setObjectName(_fromUtf8("le_ET"))
        self.gridLayoutBot.addWidget(self.le_ET, 1, 1, 1, 1)
        self.pb_ET = QtGui.QPushButton(self.groupBoxBot)
        self.pb_ET.setText(QtGui.QApplication.translate("P8Rain_GUI", "Import File", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_ET.setObjectName(_fromUtf8("pb_Et"))
        self.gridLayoutBot.addWidget(self.pb_ET, 1, 2, 1, 1)



        self.verticalLayout.addWidget(self.groupBoxTop)
        self.verticalLayout.addWidget(self.groupBoxMid)
        self.verticalLayout.addWidget(self.groupBoxBot)
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
