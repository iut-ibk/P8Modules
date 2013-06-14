from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pydynamind import *
from Analyser2_Gui import *

class AnalyserModule(Module):
	def __init__(self):
		Module.__init__(self)

		self.simulation = View("SimulationData",COMPONENT,READ)
		self.simulation.addAttribute("MusicFileNo")	

		datastream = []
		datastream.append(self.simulation)
		self.addData("City",datastream)
	def run(self):
		city = self.getData("City")
		strvec = city.getUUIDsOfComponentsInView(self.simulation)
		tmpvec = []
		for value in strvec:
			simuData = city.getComponent(value)
			musicNo = int(simuData.getAttribute("MusicFileNo").getDouble())
			if (musicNo != 0):
				musicnr = musicNo
		self.musicnr = musicnr

	def createInputDialog(self):
		form = Analyser2_Gui(self, QApplication.activeWindow())
		form.show()
		return True 
