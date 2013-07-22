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
        self.groupBox.setTitle(QtGui.QApplication.translate("StreamErosionIndexguic", "Stream Erosion Index", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "Select Csv Rain ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.le_r = QtGui.QLineEdit(self.groupBox)
        self.le_r.setObjectName(_fromUtf8("le_r"))
        self.gridLayout.addWidget(self.le_r, 0, 1, 1, 1)
        self.pb_r = QtGui.QPushButton(self.groupBox)
        self.pb_r.setText(QtGui.QApplication.translate("StreamErosionIndex_GUI", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_r.setObjectName(_fromUtf8("pb_r"))
        self.gridLayout.addWidget(self.pb_r, 0, 2, 1, 1)
        self.label2 = QtGui.QLabel(self.groupBox)
        self.label2.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "Select ET File ", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setObjectName(_fromUtf8("label2"))
        self.gridLayout.addWidget(self.label2, 1, 0, 1, 1)
        self.le_r2 = QtGui.QLineEdit(self.groupBox)
        self.le_r2.setObjectName(_fromUtf8("le_r2"))
        self.gridLayout.addWidget(self.le_r2, 1, 1, 1, 1)
        self.pb_r2 = QtGui.QPushButton(self.groupBox)
        self.pb_r2.setText(QtGui.QApplication.translate("StreamErosionIndex_GUI", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_r2.setObjectName(_fromUtf8("pb_r"))
        self.gridLayout.addWidget(self.pb_r2, 1, 2, 1, 1)

        self.labelNoY = QtGui.QLabel(self.groupBox)
        self.labelNoY.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "Number of Years: ", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNoY.setObjectName(_fromUtf8("labelNoY"))
        self.gridLayout.addWidget(self.labelNoY, 2, 0, 1, 1)
        self.le_NoY = QtGui.QLineEdit(self.groupBox)
        self.le_NoY.setObjectName(_fromUtf8("le_NoY"))
        self.gridLayout.addWidget(self.le_NoY, 2, 1, 1, 1)

        self.labelA = QtGui.QLabel(self.groupBox)
        self.labelA.setText(QtGui.QApplication.translate("StreamErosionIndexguic", "Alpha: ", None, QtGui.QApplication.UnicodeUTF8))
        self.labelA.setObjectName(_fromUtf8("labelA"))
        self.gridLayout.addWidget(self.labelA, 3, 0, 1, 1)
        self.le_A = QtGui.QLineEdit(self.groupBox)
        self.le_A.setObjectName(_fromUtf8("le_A"))
        self.gridLayout.addWidget(self.le_A, 3, 1, 1, 1)

        self.city_combo = QtGui.QComboBox(self.groupBox)
        self.city_combo.setGeometry(QtCore.QRect(250, 39, 141, 22))
        self.city_combo.setObjectName(_fromUtf8("city_combo"))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.city_combo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.city_combo, 4,0,1,1)
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