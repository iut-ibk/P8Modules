# -*- coding: utf-8 -*-

from StreamErosionIndex_guic import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pydynamind import *
import math

class StreamErosionIndex(Module):


    def __init__(self):
        Module.__init__(self)

        self.createParameter("Filename",STRING,"")
        self.Filename = ""

        self.simulation = View("SimulationData",COMPONENT,WRITE)
        self.simulation.addAttribute("msfFilename")

        datastream = []
        datastream.append(self.simulation)
        self.addData("City", datastream)

    def run(self):

        city = self.getData("City")
        simu = Component()
        simu.addAttribute("msfFilename",self.Filename)
        city.addComponent(simu,self.simulation)
        print self.Filename

    def createInputDialog(self):
        form = activateStreamErosionIndexGUI(self, QApplication.activeWindow())
        form.show()
        return True 
