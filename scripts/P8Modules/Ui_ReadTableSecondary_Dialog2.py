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
        self.groupBox.setTitle(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Stream Hydrology and Water quality", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pb_load = QtGui.QPushButton(self.groupBox)
        self.pb_load.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Load results", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_load.setObjectName(_fromUtf8("pb_load"))
        self.gridLayout.addWidget(self.pb_load, 0, 0, 1, 1)
        self.pb_export = QtGui.QPushButton(self.groupBox)
        self.pb_export.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Export csv file", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_export.setObjectName(_fromUtf8("pb_export"))
        self.gridLayout.addWidget(self.pb_export, 0, 1, 1, 1)
        '''
        self.pb_plot = QtGui.QPushButton(self.groupBox)
        self.pb_plot.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_plot.setObjectName(_fromUtf8("pb_plot"))
        self.gridLayout.addWidget(self.pb_plot, 0, 3, 1, 1)
        '''
        self.pb_clipboard = QtGui.QPushButton(self.groupBox)
        self.pb_clipboard.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Copy to clipboard", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_clipboard.setObjectName(_fromUtf8("pb_clipboard"))
        self.gridLayout.addWidget(self.pb_clipboard, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.table = QtGui.QTableWidget(ReadTableSecondary_GUI2)
        self.table.setRowCount(5)
        self.table.setColumnCount(4)
        self.table.setColumnWidth(0,210)
        self.verticalLayout.addWidget(self.table)
        self.city_combo = QtGui.QComboBox(self.groupBox)
        self.city_combo.setGeometry(QtCore.QRect(250, 39, 141, 22))
        self.city_combo.setObjectName(_fromUtf8("city_combo"))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.city_combo, 1,0,1,1)
        self.le_u = QtGui.QLineEdit(self.groupBox)
        self.le_u.setObjectName(_fromUtf8("le_u"))
        self.gridLayout.addWidget(self.le_u, 1, 1, 1, 1)


        self.label_tss = QtGui.QLabel(self.groupBox)
        self.label_tss.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "          TSS Target:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tss.setObjectName(_fromUtf8("lbl_tss"))
        self.gridLayout.addWidget(self.label_tss, 1, 2, 1, 1)
        self.le_tss = QtGui.QLineEdit(self.groupBox)
        self.le_tss.setObjectName(_fromUtf8("le_tss"))
        self.gridLayout.addWidget(self.le_tss, 1, 3, 1, 1)

        self.label_tp = QtGui.QLabel(self.groupBox)
        self.label_tp.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "           TP Target:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tp.setObjectName(_fromUtf8("lbl_tp"))
        self.gridLayout.addWidget(self.label_tp, 2, 2, 1, 1)
        self.le_tp = QtGui.QLineEdit(self.groupBox)
        self.le_tp.setObjectName(_fromUtf8("le_tp"))
        self.gridLayout.addWidget(self.le_tp, 2, 3, 1, 1)

        self.label_tn = QtGui.QLabel(self.groupBox)
        self.label_tn.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "           TN Target:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tn.setObjectName(_fromUtf8("lbl_tn"))
        self.gridLayout.addWidget(self.label_tn, 3, 2, 1, 1)
        self.le_tn = QtGui.QLineEdit(self.groupBox)
        self.le_tn.setObjectName(_fromUtf8("le_tn"))
        self.gridLayout.addWidget(self.le_tn, 3, 3, 1, 1)

        self.label_chk = QtGui.QLabel(self.groupBox)
        self.label_chk.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "           Use:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_chk.setObjectName(_fromUtf8("lbl_chk"))
        self.gridLayout.addWidget(self.label_tn, 4, 2, 1, 1)
        self.chkbox = QtGui.QCheckBox(self.groupBox)
        self.chkbox.setObjectName(_fromUtf8("chkbox"))
        self.gridLayout.addWidget(self.chkbox,  4, 3, 1, 1)

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
        self.le_u.setText("User Value")
        pass
