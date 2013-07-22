from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from pydynamind import *
from ReadTable_Gui import *
import shlex
from subprocess import call

class TreatmentPerformanceResultsModule(Module):
	def __init__(self):
		Module.__init__(self)

		#Views
		self.simulation = View("SimulationData",COMPONENT,READ)
		#self.simulation.getAttribute("MusicFileNo")
		self.simulation.getAttribute("msfFilename")


		self.TableData = View("Table Data",COMPONENT,WRITE)
		self.TableData.addAttribute("Type")
		self.TableData.addAttribute("Flow")
		self.TableData.addAttribute("TotalSuspendedSolids")
		self.TableData.addAttribute("TotalPhosphorus")
		self.TableData.addAttribute("TotalNitrogen")
		self.TableData.addAttribute("GrossPollutants")

		datastream =[]
		datastream.append(self.TableData)
		datastream.append(self.simulation)
		self.addData("City",datastream)

	def run(self):
		city = self.getData("City")
		strvec = city.getUUIDsOfComponentsInView(self.simulation)
		''' version with musicnr
		for value in strvec:
			simuData = city.getComponent(value)
			musicNo = int(simuData.getAttribute("MusicFileNo").getDouble())
			if (musicNo != 0):
				musicnr = musicNo
		self.writeBatFileFromNr(musicnr)
		self.writeMusicConfigFileFromNr(musicnr)
		'''
		#version with musicfile
		for value in strvec:
			simuAttr = city.getComponent(value)
			stringname = simuAttr.getAttribute("msfFilename").getString()
			if (stringname != ""):
				realstring = stringname
		self.writeBatFile(realstring)
		self.writeMusicConfigFile(realstring)


		print "Music running ..."
		call(["RunMusic.bat", ""])
		print "Music Done."

	def writeBatFileFromFile(self,file):
		f = open("RunMusic.bat",'w')
		f.write("\"C:\Program Files (x86)\eWater\MUSIC 5 5.1.18.172 SL\MUSIC.exe\"" + file + "\".\musicConfigFile.mcf\" -light -silent\n")
		f.close()

	def writeBatFileFromNr(self,nr):
		f = open("RunMusic.bat",'w')
		f.write("\"C:\Program Files (x86)\eWater\MUSIC 5 5.1.18.172 SL\MUSIC.exe\" \".\MusicFile-1960PC"+str(nr)+".msf\" \".\musicConfigFile"+str(nr)+".mcf\" -light -silent\n")
		f.close()
	def writeMusicConfigFileFromFile(self,file):
		f = open("musicConfigFile.mcf", 'w')
		f.write("Version = 100\n")
		f.write("Delimiter = #44\n")
		f.write("Export_TTE (Receiving Node,\"Perf_TTE.txt\")\n")
		f.close()
	def writeMusicConfigFileFromNr(self,nr):
		f = open("musicConfigFile"+str(nr)+".mcf", 'w')
		f.write("Version = 100\n")
		f.write("Delimiter = #44\n")
		f.write("Export_TTE (Receiving Node,\"Perf_TTE"+str(nr)+".txt\")\n")
		f.close()
	def createInputDialog(self):
		form = ReadTable_Gui(self, QApplication.activeWindow())
		form.show()
		return True 
