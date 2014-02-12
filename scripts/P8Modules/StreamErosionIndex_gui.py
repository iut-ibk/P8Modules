# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_StreamErosionIndexDialog(object):
    def setupUi(self, StreamErosionIndexguic):
        StreamErosionIndexguic.setObjectName(_fromUtf8("StreamErosionIndex Dialog"))
        StreamErosionIndexguic.resize(500, 110)
        StreamErosionIndexguic.setWindowTitle(QtGui.QApplication.translate("StreamErosionIndexguic", "Stream Erosion Index", None, QtGui.QApplication.UnicodeUTF8))        
        self.verticalLayout = QtGui.QVBoxLayout(StreamErosionIndexguic)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(StreamErosionIndexguic)
        self.groupBox.setTitle(QtGui.QApplication.translate("StreamErosionIndexguic", "Regional climate data", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        
        self.header = QtGui.QLabel(self.groupBox)
        self.header.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "Rainfall series", None, QtGui.QApplication.UnicodeUTF8))
        self.header.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.header, 0, 0, 1, 1)  

        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "      Select Csv Rain ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.le_r = QtGui.QLineEdit(self.groupBox)
        self.le_r.setObjectName(_fromUtf8("le_r"))
        self.gridLayout.addWidget(self.le_r, 1, 2, 1, 1)
        self.pb_r = QtGui.QPushButton(self.groupBox)
        self.pb_r.setText(QtGui.QApplication.translate("StreamErosionIndex_GUI", "Import File", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_r.setObjectName(_fromUtf8("pb_r"))
        self.gridLayout.addWidget(self.pb_r, 1, 3, 1, 1)
        
        self.header2 = QtGui.QLabel(self.groupBox)
        self.header2.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "PET series", None, QtGui.QApplication.UnicodeUTF8))
        self.header2.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.header2, 2, 0, 1, 1)  

        self.label2 = QtGui.QLabel(self.groupBox)
        self.label2.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "      Select ET File ", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setObjectName(_fromUtf8("label2"))
        self.gridLayout.addWidget(self.label2, 3, 0, 1, 1)
        self.le_r2 = QtGui.QLineEdit(self.groupBox)
        self.le_r2.setObjectName(_fromUtf8("le_r2"))
        self.gridLayout.addWidget(self.le_r2, 3, 2, 1, 1)
        self.pb_r2 = QtGui.QPushButton(self.groupBox)
        self.pb_r2.setText(QtGui.QApplication.translate("StreamErosionIndex_GUI", "Import File", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_r2.setObjectName(_fromUtf8("pb_r"))
        self.gridLayout.addWidget(self.pb_r2, 3, 3, 1, 1)

        self.header3 = QtGui.QLabel(self.groupBox)
        self.header3.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "or use MUSIC template file             Use:", None, QtGui.QApplication.UnicodeUTF8))
        self.header3.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.header3, 4, 0, 1, 1) 
        self.chkb_music = QtGui.QCheckBox(self.groupBox)
        self.chkb_music.setObjectName(_fromUtf8("chkb_music"))
        self.gridLayout.addWidget(self.chkb_music, 4, 1, 1, 1)

        self.label3 = QtGui.QLabel(self.groupBox)
        self.label3.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "      Select climate mlb", None, QtGui.QApplication.UnicodeUTF8))
        self.label3.setObjectName(_fromUtf8("label3"))
        self.gridLayout.addWidget(self.label3, 5, 0, 1, 1)
        self.le_r3 = QtGui.QLineEdit(self.groupBox)
        self.le_r3.setObjectName(_fromUtf8("le_r3"))
        self.gridLayout.addWidget(self.le_r3, 5, 2, 1, 1)
        self.pb_r3 = QtGui.QPushButton(self.groupBox)
        self.pb_r3.setText(QtGui.QApplication.translate("StreamErosionIndex_GUI", "Import File", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_r3.setObjectName(_fromUtf8("pb_r3"))
        self.gridLayout.addWidget(self.pb_r3, 5, 3, 1, 1)

        self.header4 = QtGui.QLabel(self.groupBox)
        self.header4.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "or use the WSC model defaults       Use:", None, QtGui.QApplication.UnicodeUTF8))
        self.header4.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.header4, 6, 0, 1, 1) 
        self.chkb_defaults = QtGui.QCheckBox(self.groupBox)
        self.chkb_defaults.setObjectName(_fromUtf8("chkb_defaults"))
        self.gridLayout.addWidget(self.chkb_defaults, 6, 1, 1, 1)

        self.city_combo = QtGui.QComboBox(self.groupBox)
        self.city_combo.setGeometry(QtCore.QRect(250, 39, 141, 22))
        self.city_combo.setObjectName(_fromUtf8("city_combo"))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.city_combo, 7,2,1,1)

        self.header5 = QtGui.QLabel(self.groupBox)
        self.header5.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "Partial frequency analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.header5.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.header5, 8, 0, 1, 1) 

        self.labelNoY = QtGui.QLabel(self.groupBox)
        self.labelNoY.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "      Number of Years: ", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNoY.setObjectName(_fromUtf8("labelNoY"))
        self.gridLayout.addWidget(self.labelNoY, 9, 0, 1, 1)
        self.le_NoY = QtGui.QSpinBox(self.groupBox)
        self.le_NoY.setObjectName(_fromUtf8("le_NoY"))
        self.gridLayout.addWidget(self.le_NoY, 9, 2, 1, 1)

        self.labelA = QtGui.QLabel(self.groupBox)
        self.labelA.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "      Alpha: ", None, QtGui.QApplication.UnicodeUTF8))
        self.labelA.setObjectName(_fromUtf8("labelA"))
        self.gridLayout.addWidget(self.labelA, 10, 0, 1, 1)
        self.le_A = QtGui.QDoubleSpinBox(self.groupBox)
        self.le_A.setObjectName(_fromUtf8("le_A"))
        self.gridLayout.addWidget(self.le_A, 10, 2, 1, 1)

        
        self.buttonBox = QtGui.QDialogButtonBox(StreamErosionIndexguic)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(StreamErosionIndexguic)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), StreamErosionIndexguic.accept)
        QtCore.QMetaObject.connectSlotsByName(StreamErosionIndexguic)


    def retranslateUi(self, StreamErosionIndexguic):
        self.city_combo.setItemText(0,"Adelaide")
        self.city_combo.setItemText(1,"Brisbane")   
        self.city_combo.setItemText(2,"Melbourne")
        self.city_combo.setItemText(3,"Perth")
        self.city_combo.setItemText(4,"Sydney")
        pass