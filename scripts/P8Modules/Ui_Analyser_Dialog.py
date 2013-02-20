from PyQt4 import QtCore, QtGui
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Analyser_GUI(object):
    def setupUi(self, Analyser_GUI):
	Analyser_GUI.setObjectName(_fromUtf8("Anaylser_GUI"))
	#Analyser_GUI.resize(565, 310)
	Analyser_GUI.setWindowTitle(QtGui.QApplication.translate("Analyser_GUI", "Data Table", None, QtGui.QApplication.UnicodeUTF8))
	self.verticalLayout = QtGui.QVBoxLayout(Analyser_GUI)
	self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Analyser_GUI)
        self.groupBox.setTitle(QtGui.QApplication.translate("Analyser_GUI", "Analyser", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
	self.pb_plotEBR = QtGui.QPushButton(self.groupBox)
	self.pb_plotEBR.setText(QtGui.QApplication.translate("Analyser_GUI", "Plot EBR Data", None, QtGui.QApplication.UnicodeUTF8))
	self.pb_plotEBR.setObjectName(_fromUtf8("pb_plotEBR"))
	self.gridLayout.addWidget(self.pb_plotEBR)
	self.pb_plotTPR = QtGui.QPushButton(self.groupBox)
	self.pb_plotTPR.setText(QtGui.QApplication.translate("Analyser_GUI", "Plot TPR Data", None, QtGui.QApplication.UnicodeUTF8))
	self.pb_plotTPR.setObjectName(_fromUtf8("pb_plotTPR"))
	self.gridLayout.addWidget(self.pb_plotTPR)
	self.verticalLayout.addWidget(self.groupBox)
	self.buttonBox = QtGui.QDialogButtonBox(Analyser_GUI)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

	self.retranslateUi(Analyser_GUI)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Analyser_GUI.accept)
	QtCore.QMetaObject.connectSlotsByName(Analyser_GUI)
    def retranslateUi(self, Analyser_GUI):
        pass
