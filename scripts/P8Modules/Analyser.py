from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pydynamind import *
from Analyser_Gui import *

class Analyser(Module):
	def __init__(self):
	    Module.__init__(self)

	    self.blocks = View("Block",FACE,READ)
	    self.TableData = View("Table Data",COMPONENT,WRITE)
	    datastream = []
	    datastream.append(self.blocks)
	    datastream.append(self.TableData)
	    self.addData("City",datastream)
	def run(self):
	    city = self.getData("City")
	def createInputDialog(self):
            form = Analyser_Gui(self, QApplication.activeWindow())
            form.show()
            return True 
