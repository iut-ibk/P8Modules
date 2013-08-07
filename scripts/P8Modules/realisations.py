# -*- coding: utf-8 -*-

from realisationsguic import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pydynamind import *
import math

class RealisationsSettings(Module):


    def __init__(self):
        Module.__init__(self)  

        self.createParameter("Runs",DOUBLE,"")
        self.Runs = 3

        self.simulation = View("SimulationData",COMPONENT,WRITE)
        self.simulation.addAttribute("Runs")
        self.topology = View("Topology", RASTERDATA, READ)

        datastream = []
        datastream.append(self.simulation)
        datastream.append(self.topology)
        self.addData("City", datastream)

    def run(self):

        city = self.getData("City")
        cs = self.BlockSize
        
    	simu = Component()
    	simu.addAttribute("Runs",int(self.Runs))
    	city.addComponent(simu,self.simulation)
        print "realisations runs" + str(self.Runs)
        f = open("runs.txt",'w')
        f.write(str(self.Runs))
        f.close()

    def createInputDialog(self):
        form = activaterealisationsGUI(self, QApplication.activeWindow())
        form.exec_()
        return True 
