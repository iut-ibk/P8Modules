# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_StreamErosionIndexDialog(object):
    def setupUi(self, StreamErosionIndexguic):
        StreamErosionIndexguic.setObjectName(_fromUtf8("StreamErosionIndex Dialog"))
        StreamErosionIndexguic.setWindowTitle(QtGui.QApplication.translate("StreamErosionIndexguic", "Stream Erosion Index", None, QtGui.QApplication.UnicodeUTF8))        
        StreamErosionIndexguic.setGeometry(QtCore.QRect(400,100,800,600))

        self.verticalLayout = QtGui.QVBoxLayout(StreamErosionIndexguic)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.scrollArea = QtGui.QScrollArea(StreamErosionIndexguic)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0,0,500,500))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        '''
        self.groupBox = QtGui.QGroupBox(StreamErosionIndexguic)
        self.groupBox.setTitle(QtGui.QApplication.translate("StreamErosionIndexguic", "Regional climate data", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        '''

        fontBold = QtGui.QFont()
        fontBold.setBold(True)
        fontBigHeader = QtGui.QFont()
        fontBigHeader.setBold(True)
        fontBigHeader.setPointSize(14)

        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.bigheader = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.bigheader.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "Climate data", None, QtGui.QApplication.UnicodeUTF8))
        self.bigheader.setObjectName(_fromUtf8("label"))
        self.bigheader.setFont(fontBigHeader)
        self.gridLayout.addWidget(self.bigheader, 0, 0, 1, 1)  
        
        self.header = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.header.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "Rainfall series", None, QtGui.QApplication.UnicodeUTF8))
        self.header.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.header, 1, 0, 1, 1)  

        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "      Select Csv Rain ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.le_r = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_r.setObjectName(_fromUtf8("le_r"))
        self.gridLayout.addWidget(self.le_r, 2, 2, 1, 1)
        self.pb_r = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pb_r.setText(QtGui.QApplication.translate("StreamErosionIndex_GUI", "Import File", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_r.setObjectName(_fromUtf8("pb_r"))
        self.gridLayout.addWidget(self.pb_r, 2, 3, 1, 1)
        
        self.header2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.header2.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "PET series", None, QtGui.QApplication.UnicodeUTF8))
        self.header2.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.header2, 3, 0, 1, 1)  

        self.label2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label2.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "      Select ET File ", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setObjectName(_fromUtf8("label2"))
        self.gridLayout.addWidget(self.label2, 4, 0, 1, 1)
        self.le_r2 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_r2.setObjectName(_fromUtf8("le_r2"))
        self.gridLayout.addWidget(self.le_r2, 4, 2, 1, 1)
        self.pb_r2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pb_r2.setText(QtGui.QApplication.translate("StreamErosionIndex_GUI", "Import File", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_r2.setObjectName(_fromUtf8("pb_r"))
        self.gridLayout.addWidget(self.pb_r2, 4, 3, 1, 1)

        self.header3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.header3.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "or use MUSIC template file             Use:", None, QtGui.QApplication.UnicodeUTF8))
        self.header3.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.header3, 5, 0, 1, 1) 
        self.chkb_music = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.chkb_music.setObjectName(_fromUtf8("chkb_music"))
        self.gridLayout.addWidget(self.chkb_music, 5, 1, 1, 1)

        self.label3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label3.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "      Select climate mlb", None, QtGui.QApplication.UnicodeUTF8))
        self.label3.setObjectName(_fromUtf8("label3"))
        self.gridLayout.addWidget(self.label3, 6, 0, 1, 1)
        self.le_r3 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_r3.setObjectName(_fromUtf8("le_r3"))
        self.gridLayout.addWidget(self.le_r3, 6, 2, 1, 1)
        self.pb_r3 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pb_r3.setText(QtGui.QApplication.translate("StreamErosionIndex_GUI", "Import File", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_r3.setObjectName(_fromUtf8("pb_r3"))
        self.gridLayout.addWidget(self.pb_r3, 6, 3, 1, 1)

        self.header4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.header4.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "or use Templates                    Use:", None, QtGui.QApplication.UnicodeUTF8))
        self.header4.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.header4, 7, 0, 1, 1) 
        self.chkb_defaults = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.chkb_defaults.setObjectName(_fromUtf8("chkb_defaults"))
        self.gridLayout.addWidget(self.chkb_defaults, 7, 1, 1, 1)

        self.city_combo = QtGui.QComboBox(self.scrollAreaWidgetContents)
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
        self.gridLayout.addWidget(self.city_combo, 9,2,1,1)


        self.label_head3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_head3.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Natural catchment properties", None, QtGui.QApplication.UnicodeUTF8))
        self.label_head3.setObjectName(_fromUtf8("lbl_head3"))
        self.label_head3.setFont(fontBold)
        self.gridLayout.addWidget(self.label_head3, 9, 0, 1, 1)


        self.label_head4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_head4.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "Catchment parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_head4.setObjectName(_fromUtf8("lbl_head4"))
        self.gridLayout.addWidget(self.label_head4, 10, 0, 1, 1)

        self.label_rainthres = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_rainthres.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall Threshold [mm/day]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rainthres.setObjectName(_fromUtf8("lbl_rainthres"))
        self.gridLayout.addWidget(self.label_rainthres, 11, 0, 1, 1)

        self.le_rainthres = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_rainthres.setObjectName(_fromUtf8("le_rainthres"))
        self.gridLayout.addWidget(self.le_rainthres, 11, 2, 1, 1)

        self.label_rainsoil = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_rainsoil.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall-Runoff - Pervious Area - Soil Storage Capacity [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rainsoil.setObjectName(_fromUtf8("lbl_rainsoil"))
        self.gridLayout.addWidget(self.label_rainsoil, 12, 0, 1, 1)

        self.le_rainsoil = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_rainsoil.setObjectName(_fromUtf8("le_rainsoil"))
        self.gridLayout.addWidget(self.le_rainsoil, 12, 2, 1, 1)

        self.label_raininitial = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_raininitial.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall-Runoff - Pervious Area - Initial Storage [% of Capacity]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_raininitial.setObjectName(_fromUtf8("lbl_raininitial"))
        self.gridLayout.addWidget(self.label_raininitial, 13, 0, 1, 1)

        self.le_raininitial = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_raininitial.setObjectName(_fromUtf8("le_raininitial"))
        self.gridLayout.addWidget(self.le_raininitial, 13, 2, 1, 1)

        self.label_rainfield = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_rainfield.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall-Runoff - Pervious Area - Field Capacity [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rainfield.setObjectName(_fromUtf8("lbl_rainfield"))
        self.gridLayout.addWidget(self.label_rainfield, 14, 0, 1, 1)

        self.le_rainfield = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_rainfield.setObjectName(_fromUtf8("le_rainfield"))
        self.gridLayout.addWidget(self.le_rainfield, 14, 2, 1, 1)

        self.label_raininfil = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_raininfil.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall-Runoff - Pervious Area - Infiltration Capacity Coefficient", None, QtGui.QApplication.UnicodeUTF8))
        self.label_raininfil.setObjectName(_fromUtf8("lbl_raininfil"))
        self.gridLayout.addWidget(self.label_raininfil, 15, 0, 1, 1)

        self.le_raininfil = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_raininfil.setObjectName(_fromUtf8("le_raininfil"))
        self.gridLayout.addWidget(self.le_raininfil, 15, 2, 1, 1)

        self.label_raininfil2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_raininfil2.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall-Runoff - Pervious Area - Infiltration Capacity Exponent", None, QtGui.QApplication.UnicodeUTF8))
        self.label_raininfil2.setObjectName(_fromUtf8("lbl_raininfil2"))
        self.gridLayout.addWidget(self.label_raininfil2, 16, 0, 1, 1)

        self.le_raininfil2 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_raininfil2.setObjectName(_fromUtf8("le_raininfil2"))
        self.gridLayout.addWidget(self.le_raininfil2, 16, 2, 1, 1)

        self.label_raindepth = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_raindepth.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall-Runoff - Groundwater Properties - Initial Depth [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_raindepth.setObjectName(_fromUtf8("lbl_raindepth"))
        self.gridLayout.addWidget(self.label_raindepth, 17, 0, 1, 1)

        self.le_raindepth = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_raindepth.setObjectName(_fromUtf8("le_raindepth"))
        self.gridLayout.addWidget(self.le_raindepth, 17, 2, 1, 1)

        self.label_rainrecharge = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_rainrecharge.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall-Runoff - Groundwater Properties - Daily Recharge Rate [%]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rainrecharge.setObjectName(_fromUtf8("lbl_rainrecharge"))
        self.gridLayout.addWidget(self.label_rainrecharge, 18, 0, 1, 1)

        self.le_rainrecharge = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_rainrecharge.setObjectName(_fromUtf8("le_rainrecharge"))
        self.gridLayout.addWidget(self.le_rainrecharge, 18, 2, 1, 1)

        self.label_rainbaseflow = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_rainbaseflow.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall-Runoff - Groundwater Properties - Daily Baseflow Rate [%]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rainbaseflow.setObjectName(_fromUtf8("lbl_rainbaseflow"))
        self.gridLayout.addWidget(self.label_rainbaseflow, 19, 0, 1, 1)

        self.le_rainbaseflow = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_rainbaseflow.setObjectName(_fromUtf8("le_rainbaseflow"))
        self.gridLayout.addWidget(self.le_rainbaseflow, 19, 2, 1, 1)

        self.label_raindeep = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_raindeep.setText(QtGui.QApplication.translate("ReadTableSecondary_GUI2", "    Rainfall-Runoff - Groundwater Properties - Daily Deep Seepage Rate [%]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_raindeep.setObjectName(_fromUtf8("lbl_raindeep"))
        self.gridLayout.addWidget(self.label_raindeep, 20, 0, 1, 1)

        self.le_raindeep = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.le_raindeep.setObjectName(_fromUtf8("le_raindeep"))
        self.gridLayout.addWidget(self.le_raindeep, 20, 2, 1, 1)


        self.header5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.header5.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "Partial frequency analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.header5.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.header5, 21, 0, 1, 1) 

        self.labelNoY = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.labelNoY.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "      Number of Years: ", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNoY.setObjectName(_fromUtf8("labelNoY"))
        self.gridLayout.addWidget(self.labelNoY, 22, 0, 1, 1)
        self.le_NoY = QtGui.QSpinBox(self.scrollAreaWidgetContents)
        self.le_NoY.setObjectName(_fromUtf8("le_NoY"))
        self.gridLayout.addWidget(self.le_NoY, 22, 2, 1, 1)

        self.labelA = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.labelA.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "      Alpha: ", None, QtGui.QApplication.UnicodeUTF8))
        self.labelA.setObjectName(_fromUtf8("labelA"))
        self.gridLayout.addWidget(self.labelA, 23, 0, 1, 1)
        self.le_A = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.le_A.setObjectName(_fromUtf8("le_A"))
        self.gridLayout.addWidget(self.le_A, 23, 2, 1, 1)

        self.labelUB = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.labelUB.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "Inputs from UrbanBeats?", None, QtGui.QApplication.UnicodeUTF8))
        self.labelUB.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.labelUB, 24, 0, 1, 1) 
        self.chkb_UB = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.chkb_UB.setObjectName(_fromUtf8("chkb_UB"))
        self.gridLayout.addWidget(self.chkb_UB, 24, 2, 1, 1)

        
        self.buttonBox = QtGui.QDialogButtonBox(StreamErosionIndexguic)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(StreamErosionIndexguic)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), StreamErosionIndexguic.accept)
        QtCore.QMetaObject.connectSlotsByName(StreamErosionIndexguic)


    def retranslateUi(self, StreamErosionIndexguic):
        
        self.city_combo.setItemText(0,"Brisbane")
        self.city_combo.setItemText(1,"Sydney")   
        self.city_combo.setItemText(2,"Canberra")
        self.city_combo.setItemText(3,"Melbourne")
        self.city_combo.setItemText(4,"Hobart")
        self.city_combo.setItemText(5,"Adelaide")
        self.city_combo.setItemText(6,"Perth")
        self.city_combo.setItemText(7,"User defined")
