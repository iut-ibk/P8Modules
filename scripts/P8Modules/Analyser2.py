from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pydynamind import *
from Analyser2_Gui import *

class AnalyserModule(Module):
	def __init__(self):
		Module.__init__(self)

		self.simulation = View("SimulationData",COMPONENT,READ)
		self.simulation.getAttribute("SEIurb")
		self.simulation.getAttribute("SEIwsud")	

		datastream = []
		datastream.append(self.simulation)
		self.addData("City",datastream)
	def run(self):
		city = self.getData("City")
		strvec = city.getUUIDsOfComponentsInView(self.simulation)
		tmpvec = []
		self.SEIwsud = 0.0
		self.SEIurb = 0.0
		for value in strvec:
			simuData = city.getComponent(value)
			urb = simuData.getAttribute("SEIurb").getDouble()
			wsud = simuData.getAttribute("SEIwsud").getDouble()
			if (urb != 0):
				self.SEIurb = urb
			if(wsud != 0):
				self.SEIwsud = wsud
	def createInputDialog(self):
		form = Analyser2_Gui(self, QApplication.activeWindow())
		form.show()
		return True 
