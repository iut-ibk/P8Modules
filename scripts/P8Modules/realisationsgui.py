# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_RealisationsDialog(object):
    def setupUi(self, realisationsguic):
        realisationsguic.setObjectName(_fromUtf8("Realisations Dialog"))
        realisationsguic.resize(500, 110)
        realisationsguic.setWindowTitle(QtGui.QApplication.translate("realisationsguic", "Realisations Dialog", None, QtGui.QApplication.UnicodeUTF8))        
        self.verticalLayout = QtGui.QVBoxLayout(realisationsguic)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(realisationsguic)
        self.groupBox.setTitle(QtGui.QApplication.translate("realisationsguic", "Realisations Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("realisationsguic", "Select the number of top ranked realisation you want to evaluate", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.le_r = QtGui.QLineEdit(self.groupBox)
        self.le_r.setObjectName(_fromUtf8("le_r"))
        self.gridLayout.addWidget(self.le_r, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(realisationsguic)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(realisationsguic)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), realisationsguic.accept)
        QtCore.QMetaObject.connectSlotsByName(realisationsguic)


    def retranslateUi(self, realisationsguic):
        pass