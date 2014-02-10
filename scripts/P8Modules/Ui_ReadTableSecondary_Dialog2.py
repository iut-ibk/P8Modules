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

class Ui_ReadTableSecondary_GUI2(object):
    def setupUi(self, ReadTableSecondary_GUI2):
        ReadTableSecondary_GUI2.setObjectName(_fromUtf8("ReadTableSecondary_GUI2"))
        ReadTableSecondary_GUI2.resize(500, 310)
        ReadTableSecondary_GUI2.setWindowTitle(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Stream Hydrology and Water quality", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(ReadTableSecondary_GUI2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(ReadTableSecondary_GUI2)
        self.groupBox.setTitle(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Regional Rainfall Data", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.label_head = QtGui.QLabel(self.groupBox)
        self.label_head.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Mean annual rainfall [ mm ]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_head.setObjectName(_fromUtf8("lbl_head"))
        self.gridLayout.addWidget(self.label_head, 0, 0, 1, 1)

        self.city_combo  = QtGui.QComboBox(self.groupBox)
        self.city_combo.setGeometry(QtCore.QRect(250, 39, 141, 22))
        self.city_combo.setObjectName(_fromUtf8("city_combo"))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.city_combo, 1,0,1,1)

        self.spb_city = QtGui.QSpinBox(self.groupBox)
        self.spb_city.setObjectName(_fromUtf8("city_spin"))
        self.spb_city.setRange(0,2000)
        self.gridLayout.addWidget(self.spb_city, 1, 1, 1, 1)

        self.label_head2 = QtGui.QLabel(self.groupBox)
        self.label_head2.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Targets - hydrology and water quality", None, QtGui.QApplication.UnicodeUTF8))
        self.label_head2.setObjectName(_fromUtf8("lbl_head2"))
        self.gridLayout.addWidget(self.label_head2, 2, 0, 1, 1)

        self.label_vol = QtGui.QLabel(self.groupBox)
        self.label_vol.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Total volume reduction [%]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_vol.setObjectName(_fromUtf8("lbl_vol"))
        self.gridLayout.addWidget(self.label_vol, 3, 0, 1, 1)

        self.vol_combo = QtGui.QComboBox(self.groupBox)
        self.vol_combo.setGeometry(QtCore.QRect(250, 39, 141, 22))
        self.vol_combo.setObjectName(_fromUtf8("vol_combo"))
        self.vol_combo.addItem(_fromUtf8(""))
        self.vol_combo.addItem(_fromUtf8(""))
        self.vol_combo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.vol_combo, 4,0,1,1)

        self.spb_vol = QtGui.QSpinBox(self.groupBox)
        self.spb_vol.setObjectName(_fromUtf8("vol_spin"))
        self.gridLayout.addWidget(self.spb_vol, 4, 1, 1, 1)
        
        self.label_vol = QtGui.QLabel(self.groupBox)
        self.label_vol.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Frequency of runoff days [days/year]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_vol.setObjectName(_fromUtf8("lbl_vol"))
        self.gridLayout.addWidget(self.label_vol, 5, 0, 1, 1)

        self.spb_freq = QtGui.QSpinBox(self.groupBox)
        self.spb_freq.setObjectName(_fromUtf8("freq_spin"))
        self.gridLayout.addWidget(self.spb_freq, 5, 1, 1, 1)


        self.label_pol = QtGui.QLabel(self.groupBox)
        self.label_pol.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Pollutant concentration [mg/l]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pol.setObjectName(_fromUtf8("lbl_pol"))
        self.gridLayout.addWidget(self.label_pol, 6, 0, 1, 1)

        self.label_tss = QtGui.QLabel(self.groupBox)
        self.label_tss.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "          TSS concentration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tss.setObjectName(_fromUtf8("lbl_tss"))
        self.gridLayout.addWidget(self.label_tss, 7, 0, 1, 1)
        self.le_tss = QtGui.QDoubleSpinBox(self.groupBox)
        self.le_tss.setObjectName(_fromUtf8("le_tss"))
        self.gridLayout.addWidget(self.le_tss, 7, 1, 1, 1)

        self.label_tp = QtGui.QLabel(self.groupBox)
        self.label_tp.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "           TP concentration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tp.setObjectName(_fromUtf8("lbl_tp"))
        self.gridLayout.addWidget(self.label_tp, 8, 0, 1, 1)
        self.le_tp = QtGui.QDoubleSpinBox(self.groupBox)
        self.le_tp.setObjectName(_fromUtf8("le_tp"))
        self.gridLayout.addWidget(self.le_tp, 8, 1, 1, 1)

        self.label_tn = QtGui.QLabel(self.groupBox)
        self.label_tn.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "           TN concentration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tn.setObjectName(_fromUtf8("lbl_tn"))
        self.gridLayout.addWidget(self.label_tn, 9, 0, 1, 1)
        self.le_tn = QtGui.QDoubleSpinBox(self.groupBox)
        self.le_tn.setObjectName(_fromUtf8("le_tn"))
        self.gridLayout.addWidget(self.le_tn, 9, 1, 1, 1)


        self.pb_load = QtGui.QPushButton(self.groupBox)
        self.pb_load.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Load results", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_load.setObjectName(_fromUtf8("pb_load"))
        self.gridLayout.addWidget(self.pb_load, 10, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)
        self.table = QtGui.QTableWidget(ReadTableSecondary_GUI2)
        self.table.setRowCount(5)
        self.table.setColumnCount(4)
        self.table.setColumnWidth(0,210)
        self.verticalLayout.addWidget(self.table)
        self.pb_export = QtGui.QPushButton(self.groupBox)
        self.pb_export.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Export csv file", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_export.setObjectName(_fromUtf8("pb_export"))
        self.verticalLayout.addWidget(self.pb_export)
        self.pb_clipboard = QtGui.QPushButton(self.groupBox)
        self.pb_clipboard.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Copy to clipboard", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_clipboard.setObjectName(_fromUtf8("pb_clipboard"))
        self.verticalLayout.addWidget(self.pb_clipboard)
  
        

        
        self.buttonBox = QtGui.QDialogButtonBox(ReadTableSecondary_GUI2)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ReadTableSecondary_GUI2)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ReadTableSecondary_GUI2.accept)
        QtCore.QMetaObject.connectSlotsByName(ReadTableSecondary_GUI2)

    def retranslateUi(self, ReadTableSecondary_GUI2):
        self.city_combo.setItemText(0,"Adelaide")
        self.city_combo.setItemText(1,"Brisbane")   
        self.city_combo.setItemText(2,"Melbourne")
        self.city_combo.setItemText(3,"Perth")
        self.city_combo.setItemText(4,"Sydney")
        self.city_combo.setItemText(5,"User Value")

        self.vol_combo.setItemText(0,"Limited potential for recovery")
        self.vol_combo.setItemText(1,"Considerable potential for recovery")
        self.vol_combo.setItemText(2,"User defined")

        pass
