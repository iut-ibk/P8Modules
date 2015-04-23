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
        ReadTableSecondary_GUI2.setWindowTitle(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Stream Hydrology and Water quality", None, QtGui.QApplication.UnicodeUTF8))
        ReadTableSecondary_GUI2.setGeometry(QtCore.QRect(400,100,800,600))
        self.verticalLayout = QtGui.QVBoxLayout(ReadTableSecondary_GUI2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.scrollArea = QtGui.QScrollArea(ReadTableSecondary_GUI2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0,0,500,500))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        '''
        self.groupBox = QtGui.QGroupBox(ReadTableSecondary_GUI2)
        self.groupBox.setTitle(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Regional Rainfall Data", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        '''
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        fontB = QtGui.QFont()
        fontB.setBold(True)

        fontI = QtGui.QFont()
        fontI.setItalic(True)

        self.label_head = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_head.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Mean annual rainfall [ mm ]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_head.setObjectName(_fromUtf8("lbl_head"))
        self.label_head.setFont(fontB)
        self.gridLayout.addWidget(self.label_head, 0, 0, 1, 1)

        self.city_combo  = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.city_combo.setGeometry(QtCore.QRect(250, 39, 141, 22))
        self.city_combo.setObjectName(_fromUtf8("city_combo"))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.city_combo, 1,0,1,1)

        self.spb_city = QtGui.QSpinBox(self.scrollAreaWidgetContents)
        self.spb_city.setObjectName(_fromUtf8("city_spin"))
        self.spb_city.setRange(0,2000)
        self.gridLayout.addWidget(self.spb_city, 1, 1, 1, 1)
        '''
        self.label_head3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_head3.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Natural catchement properties", None, QtGui.QApplication.UnicodeUTF8))
        self.label_head3.setObjectName(_fromUtf8("lbl_head3"))
        self.label_head3.setFont(font)
        self.gridLayout.addWidget(self.label_head3, 2, 0, 1, 1)
        '''
        self.label_base = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_base.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Baseflow allowed in the WSUD catchement[m³/day] (Leave zero for default value.)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_base.setObjectName(_fromUtf8("lbl_base"))
        self.label_base.setFont(fontB)
        self.label_base.setToolTip("Leave zero for default equal to\n3 times the median of the baseflow\n in the natural catchement.")
        self.gridLayout.addWidget(self.label_base, 3, 0, 1, 1)

        self.spb_base = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.spb_base.setObjectName(_fromUtf8("city_base"))
        self.spb_base.setRange(0,2000)
        self.spb_base.setDecimals(10)
        self.gridLayout.addWidget(self.spb_base, 3, 1, 1, 1)


        self.label_head4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_head4.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Natural catchement properties", None, QtGui.QApplication.UnicodeUTF8))
        self.label_head4.setObjectName(_fromUtf8("lbl_head4"))
        self.label_head4.setFont(fontB)
        self.gridLayout.addWidget(self.label_head4, 4, 0, 1, 1)

        self.label_rainthres = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_rainthres.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall Threshold [mm/day]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rainthres.setObjectName(_fromUtf8("lbl_rainthres"))
        self.gridLayout.addWidget(self.label_rainthres, 5, 0, 1, 1)

        self.le_rainthres = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_rainthres.setObjectName(_fromUtf8("le_rainthres"))
        self.gridLayout.addWidget(self.le_rainthres, 5, 1, 1, 1)

        self.label_rainsoil = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_rainsoil.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall-Runoff - Pervious Area - Soil Storage Capacity [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rainsoil.setObjectName(_fromUtf8("lbl_rainsoil"))
        self.gridLayout.addWidget(self.label_rainsoil, 6, 0, 1, 1)

        self.le_rainsoil = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_rainsoil.setObjectName(_fromUtf8("le_rainsoil"))
        self.gridLayout.addWidget(self.le_rainsoil, 6, 1, 1, 1)

        self.label_raininitial = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_raininitial.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall-Runoff - Pervious Area - Initial Storage [% of Capacity]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_raininitial.setObjectName(_fromUtf8("lbl_raininitial"))
        self.gridLayout.addWidget(self.label_raininitial, 7, 0, 1, 1)

        self.le_raininitial = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_raininitial.setObjectName(_fromUtf8("le_raininitial"))
        self.gridLayout.addWidget(self.le_raininitial, 7, 1, 1, 1)

        self.label_rainfield = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_rainfield.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall-Runoff - Pervious Area - Field Capacity [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rainfield.setObjectName(_fromUtf8("lbl_rainfield"))
        self.gridLayout.addWidget(self.label_rainfield, 8, 0, 1, 1)

        self.le_rainfield = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_rainfield.setObjectName(_fromUtf8("le_rainfield"))
        self.gridLayout.addWidget(self.le_rainfield, 8, 1, 1, 1)

        self.label_raininfil = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_raininfil.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall-Runoff - Pervious Area - Infiltration Capacity Coefficient", None, QtGui.QApplication.UnicodeUTF8))
        self.label_raininfil.setObjectName(_fromUtf8("lbl_raininfil"))
        self.gridLayout.addWidget(self.label_raininfil, 9, 0, 1, 1)

        self.le_raininfil = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_raininfil.setObjectName(_fromUtf8("le_raininfil"))
        self.gridLayout.addWidget(self.le_raininfil, 9, 1, 1, 1)

        self.label_raininfil2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_raininfil2.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall-Runoff - Pervious Area - Infiltration Capacity Exponent", None, QtGui.QApplication.UnicodeUTF8))
        self.label_raininfil2.setObjectName(_fromUtf8("lbl_raininfil2"))
        self.gridLayout.addWidget(self.label_raininfil2, 10, 0, 1, 1)

        self.le_raininfil2 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_raininfil2.setObjectName(_fromUtf8("le_raininfil2"))
        self.gridLayout.addWidget(self.le_raininfil2, 10, 1, 1, 1)

        self.label_raindepth = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_raindepth.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall-Runoff - Groundwater Properties - Initial Depth [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_raindepth.setObjectName(_fromUtf8("lbl_raindepth"))
        self.gridLayout.addWidget(self.label_raindepth, 11, 0, 1, 1)

        self.le_raindepth = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_raindepth.setObjectName(_fromUtf8("le_raindepth"))
        self.gridLayout.addWidget(self.le_raindepth, 11, 1, 1, 1)

        self.label_rainrecharge = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_rainrecharge.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall-Runoff - Groundwater Properties - Daily Recharge Rate [%]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rainrecharge.setObjectName(_fromUtf8("lbl_rainrecharge"))
        self.gridLayout.addWidget(self.label_rainrecharge, 12, 0, 1, 1)

        self.le_rainrecharge = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_rainrecharge.setObjectName(_fromUtf8("le_rainrecharge"))
        self.gridLayout.addWidget(self.le_rainrecharge, 12, 1, 1, 1)

        self.label_rainbaseflow = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_rainbaseflow.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall-Runoff - Groundwater Properties - Daily Baseflow Rate [%]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rainbaseflow.setObjectName(_fromUtf8("lbl_rainbaseflow"))
        self.gridLayout.addWidget(self.label_rainbaseflow, 13, 0, 1, 1)

        self.le_rainbaseflow = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_rainbaseflow.setObjectName(_fromUtf8("le_rainbaseflow"))
        self.gridLayout.addWidget(self.le_rainbaseflow, 13, 1, 1, 1)

        self.label_raindeep = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_raindeep.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall-Runoff - Groundwater Properties - Daily Deep Seepage Rate [%]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_raindeep.setObjectName(_fromUtf8("lbl_raindeep"))
        self.gridLayout.addWidget(self.label_raindeep, 14, 0, 1, 1)

        self.le_raindeep = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_raindeep.setObjectName(_fromUtf8("le_raindeep"))
        self.gridLayout.addWidget(self.le_raindeep, 14, 1, 1, 1)
        
        self.label_head2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_head2.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Targets - hydrology and water quality", None, QtGui.QApplication.UnicodeUTF8))
        self.label_head2.setObjectName(_fromUtf8("lbl_head2"))
        self.label_head2.setFont(fontB)
        self.gridLayout.addWidget(self.label_head2, 15, 0, 1, 1)

        self.label_vol = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_vol.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Total volume reduction [%]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_vol.setObjectName(_fromUtf8("lbl_vol"))
        self.label_vol.setFont(fontI)
        self.gridLayout.addWidget(self.label_vol, 16, 0, 1, 1)

        self.label_flux = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_flux.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "       Consider infiltration fluxes?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_flux.setObjectName(_fromUtf8("lbl_flux"))
        self.gridLayout.addWidget(self.label_flux, 17, 0, 1, 1)

        self.chkb_flux = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.chkb_flux.setObjectName(_fromUtf8("chkb_flux"))
        self.gridLayout.addWidget(self.chkb_flux, 17, 1, 1, 1)

        self.vol_combo = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.vol_combo.setGeometry(QtCore.QRect(250, 39, 141, 22))
        self.vol_combo.setObjectName(_fromUtf8("vol_combo"))
        self.vol_combo.addItem(_fromUtf8(""))
        self.vol_combo.addItem(_fromUtf8(""))
        self.vol_combo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.vol_combo, 18,0,1,1)

        self.spb_vol = QtGui.QSpinBox(self.scrollAreaWidgetContents)
        self.spb_vol.setObjectName(_fromUtf8("vol_spin"))
        self.gridLayout.addWidget(self.spb_vol, 18, 1, 1, 1)
        
        self.label_vol = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_vol.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Frequency of runoff days [days/year]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_vol.setObjectName(_fromUtf8("lbl_vol"))
        self.label_vol.setFont(fontI)
        self.gridLayout.addWidget(self.label_vol, 19, 0, 1, 1)

        self.spb_freq = QtGui.QSpinBox(self.scrollAreaWidgetContents)
        self.spb_freq.setObjectName(_fromUtf8("freq_spin"))
        self.gridLayout.addWidget(self.spb_freq, 19, 1, 1, 1)


        self.label_pol = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_pol.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Pollutant concentration [mg/l]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pol.setObjectName(_fromUtf8("lbl_pol"))
        self.label_pol.setFont(fontI)
        self.gridLayout.addWidget(self.label_pol, 20, 0, 1, 1)

        self.label_tss = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_tss.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "          TSS concentration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tss.setObjectName(_fromUtf8("lbl_tss"))
        self.gridLayout.addWidget(self.label_tss, 21, 0, 1, 1)
        self.le_tss = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.le_tss.setObjectName(_fromUtf8("le_tss"))
        self.gridLayout.addWidget(self.le_tss, 21, 1, 1, 1)

        self.label_tp = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_tp.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "           TP concentration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tp.setObjectName(_fromUtf8("lbl_tp"))
        self.gridLayout.addWidget(self.label_tp, 22, 0, 1, 1)
        self.le_tp = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.le_tp.setObjectName(_fromUtf8("le_tp"))
        self.gridLayout.addWidget(self.le_tp, 22, 1, 1, 1)

        self.label_tn = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_tn.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "           TN concentration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tn.setObjectName(_fromUtf8("lbl_tn"))
        self.gridLayout.addWidget(self.label_tn, 23, 0, 1, 1)
        self.le_tn = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.le_tn.setObjectName(_fromUtf8("le_tn"))
        self.gridLayout.addWidget(self.le_tn, 23, 1, 1, 1)
        

        self.pb_load = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pb_load.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Load results", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_load.setObjectName(_fromUtf8("pb_load"))
        self.gridLayout.addWidget(self.pb_load, 24, 0, 1, 1)

        self.label_ub = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_ub.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Inputs from UrbanBeats?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ub.setObjectName(_fromUtf8("lbl_ub"))
        self.gridLayout.addWidget(self.label_ub, 25, 0, 1, 1)

        self.chkb_ub = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.chkb_ub.setObjectName(_fromUtf8("chkb_ub"))
        self.gridLayout.addWidget(self.chkb_ub, 25, 1, 1, 1)

        self.label_ub = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_ub.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Start Date Rainfall Data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ub.setObjectName(_fromUtf8("lbl_ub"))
        self.gridLayout.addWidget(self.label_ub, 26, 0, 1, 1)

        self.te_rainstart = QtGui.QDateTimeEdit(self.scrollAreaWidgetContents)
        self.te_rainstart.setObjectName(_fromUtf8("te_rainstart"))
        self.te_rainstart.setDisplayFormat("yyyy.MM.dd")
        self.gridLayout.addWidget(self.te_rainstart, 26, 1, 1, 1)

        self.label_ub = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_ub.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "End Date Rainfall Data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ub.setObjectName(_fromUtf8("lbl_ub"))
        self.gridLayout.addWidget(self.label_ub, 27, 0, 1, 1)

        self.te_rainend = QtGui.QDateTimeEdit(self.scrollAreaWidgetContents)
        self.te_rainend.setObjectName(_fromUtf8("te_rainend"))
        self.te_rainend.setDisplayFormat("yyyy.MM.dd")
        self.gridLayout.addWidget(self.te_rainend, 27, 1, 1, 1)

        self.verticalLayout.addWidget(self.scrollArea)
        self.table = QtGui.QTableWidget(ReadTableSecondary_GUI2)
        self.table.setRowCount(10)
        self.table.setColumnCount(4)
        self.table.setColumnWidth(0,210)
        self.verticalLayout.addWidget(self.table)
        self.pb_export = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pb_export.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Export csv file", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_export.setObjectName(_fromUtf8("pb_export"))
        self.verticalLayout.addWidget(self.pb_export)
        self.pb_clipboard = QtGui.QPushButton(self.scrollAreaWidgetContents)
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
        
        self.city_combo.setItemText(0,"Brisbane")
        self.city_combo.setItemText(1,"Sydney")   
        self.city_combo.setItemText(2,"Canberra")
        self.city_combo.setItemText(3,"Melbourne")
        self.city_combo.setItemText(4,"Hobart")
        self.city_combo.setItemText(5,"Adelaide")
        self.city_combo.setItemText(6,"Perth")
        self.city_combo.setItemText(7,"User Defined")

        self.vol_combo.setItemText(0,"Limited potential for recovery")
        self.vol_combo.setItemText(1,"Considerable potential for recovery")
        self.vol_combo.setItemText(2,"User defined")
        
        pass
