# -*- coding: utf-8 -*-

from importMSFguic import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pydynamind import *
import math

class ImportMSF(Module):


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
        workpath = self.getHelpUrl() + "/"
        if (platform.system() != "Linux"):
            workpath = workpath.replace("/","\\")
        city = self.getData("City")
        simu = Component()
        simu.addAttribute("msfFilename",str(workpath + self.Filename))
        simu.addAttribute("MusicFileNo","-1")
        city.addComponent(simu,self.simulation)

    def createInputDialog(self):
        form = activateimportMSFGUI(self, QApplication.activeWindow())
        form.exec_()
        return True 
    def getClassName(self):
        return "Import WSUD Layout (.msf)"
    def getFileName(self):
        return "Scenario Definition"