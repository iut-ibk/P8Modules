from PyQt4 import QtCore, QtGui
try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_Analyser2_GUI(object):
	def setupUi(self, Analyser2_GUI):
		Analyser2_GUI.setObjectName(_fromUtf8("Anaylser2_GUI"))
		#Analyser_GUI.resize(565, 310)
		Analyser2_GUI.setWindowTitle(QtGui.QApplication.translate("Analyser2_GUI", "Bar Charts", None, QtGui.QApplication.UnicodeUTF8))
		self.verticalLayout = QtGui.QVBoxLayout(Analyser2_GUI)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.groupBox = QtGui.QGroupBox(Analyser2_GUI)
		self.groupBox.setTitle(QtGui.QApplication.translate("Analyser2_GUI", "Analyser", None, QtGui.QApplication.UnicodeUTF8))
		self.groupBox.setObjectName(_fromUtf8("groupBox"))
		self.gridLayout = QtGui.QGridLayout(self.groupBox)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.pb_plotSEI = QtGui.QPushButton(self.groupBox)
		self.pb_plotSEI.setText(QtGui.QApplication.translate("Analyser2_GUI", "View SEI", None, QtGui.QApplication.UnicodeUTF8))
		self.pb_plotSEI.setObjectName(_fromUtf8("pb_plotUtil"))
		self.gridLayout.addWidget(self.pb_plotSEI)
		self.pb_plotUtil = QtGui.QPushButton(self.groupBox)
		self.pb_plotUtil.setText(QtGui.QApplication.translate("Analyser2_GUI", "View Utilisation", None, QtGui.QApplication.UnicodeUTF8))
		self.pb_plotUtil.setObjectName(_fromUtf8("pb_plotUtil"))
		self.gridLayout.addWidget(self.pb_plotUtil)
		self.pb_plotTPR = QtGui.QPushButton(self.groupBox)
		self.pb_plotTPR.setText(QtGui.QApplication.translate("Analyser2_GUI", "View Treatment Performance", None, QtGui.QApplication.UnicodeUTF8))
		self.pb_plotTPR.setObjectName(_fromUtf8("pb_plotTPR"))
		self.gridLayout.addWidget(self.pb_plotTPR)
		self.pb_plotEBR = QtGui.QPushButton(self.groupBox)
		self.pb_plotEBR.setText(QtGui.QApplication.translate("Analyser2_GUI", "View Enviromental Benefit", None, QtGui.QApplication.UnicodeUTF8))
		self.pb_plotEBR.setObjectName(_fromUtf8("pb_plotEBR"))
		self.gridLayout.addWidget(self.pb_plotEBR)
		self.pb_plotMicroB = QtGui.QPushButton(self.groupBox)
		self.pb_plotMicroB.setText(QtGui.QApplication.translate("Analyser2_GUI", "View Microclimate Benefit", None, QtGui.QApplication.UnicodeUTF8))
		self.pb_plotMicroB.setObjectName(_fromUtf8("pb_plotMicroB"))
		self.gridLayout.addWidget(self.pb_plotMicroB)
		self.pb_plotEcoV = QtGui.QPushButton(self.groupBox)
		self.pb_plotEcoV.setText(QtGui.QApplication.translate("Analyser2_GUI", "View Economic Valuation", None, QtGui.QApplication.UnicodeUTF8))
		self.pb_plotEcoV.setObjectName(_fromUtf8("pb_plotEcoV"))
		self.gridLayout.addWidget(self.pb_plotEcoV)
		self.pb_delete = QtGui.QPushButton(self.groupBox)
		self.pb_delete.setText(QtGui.QApplication.translate("Analyser2_GUI", "delete tmp data", None, QtGui.QApplication.UnicodeUTF8))
		self.pb_delete.setObjectName(_fromUtf8("pb_delete"))
		self.gridLayout.addWidget(self.pb_delete)
		self.verticalLayout.addWidget(self.groupBox)
		self.buttonBox = QtGui.QDialogButtonBox(Analyser2_GUI)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(Analyser2_GUI)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Analyser2_GUI.accept)
		QtCore.QMetaObject.connectSlotsByName(Analyser2_GUI)

	def retranslateUi(self, Analyser2_GUI):
		pass
