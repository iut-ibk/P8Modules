from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pydynamind import *
from Analyser_Gui import *

class Analyser(Module):
	def __init__(self):
	    Module.__init__(self)

	    self.simulation = View("SimulationData",COMPONENT,READ)
	    self.simulation.getAttribute("Utilisations")
	    self.simulation.getAttribute("Runs")

	    self.TableData = View("Table Data",COMPONENT,WRITE)
	    datastream = []
	    datastream.append(self.simulation)
	    datastream.append(self.TableData)
	    self.addData("City",datastream)
	def run(self):
		city = self.getData("City")
		strvec = city.getUUIDsOfComponentsInView(self.simulation)
		self.Utilvec = []
		runvec = []
		for value in strvec:
			simuAttr = city.getComponent(value)
			tmpvec = simuAttr.getAttribute("Utilisations").getDoubleVector()
			run = simuAttr.getAttribute("Runs").getDouble()
			if (run != 0):
				runvec.append(int(run))
			for zahl in tmpvec:
				self.Utilvec.append(int(zahl))
		self.runs = runvec[0]
		print self.Utilvec
		print self.runs

	def createInputDialog(self):
		form = Analyser_Gui(self, QApplication.activeWindow())
		form.exec_()
		return True 
	def getClassName(self):
		return "blabal"