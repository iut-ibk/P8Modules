from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from pydynamind import *
from ReadTable_Gui import *
import shlex
from subprocess import call
import platform
import shutil

class TreatmentPerformanceResultsModule(Module):
	def __init__(self):
		Module.__init__(self)

		#Views
		self.simulation = View("SimulationData",COMPONENT,READ)
		#self.simulation.getAttribute("MusicFileNo")
		self.simulation.getAttribute("msfFilename")
		self.simulation.addAttribute("SEIurb")
		self.simulation.addAttribute("SEIwsud")	
		self.simulation.addAttribute("NoY")
		self.simulation.addAttribute("alpha")


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
		tmp = realstring.split(".")
		newname = str(tmp[0] + "TP." + str(tmp[1]))
		shutil.copyfile(realstring,newname)
		self.writeBatFile(newname)
		self.writeMusicConfigFile(newname)


		print "Music running ..."
		if (platform.system() != "Linux"):
			call(["RunMusicTP.bat", ""])
		print "Music Done."

	def writeBatFile(self,file):
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		f = open(workpath + "RunMusicTP.bat",'w')
		if (platform.system() != "Linux"):
			file = file.replace("/","\\")
		f.write("\"" + settings.value("Music").toString() + "\MUSIC.exe\" \"" + file + "\" \"" + workpath + "musicConfigFileTP.mcf\" -light -silent\n")
		f.close()

	def writeBatFileFromNr(self,nr):
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		f = open(workpath + "RunMusicTP.bat",'w')
		f.write("\"" + settings.value("Music").toString() + "\MUSIC.exe\" \".\MusicFile-1960PC"+str(nr)+".msf\" \"" + workpath + "musicConfigFile"+str(nr)+".mcf\" -light -silent\n")
		f.close()
	def writeMusicConfigFile(self,file):
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		f = open(workpath + "musicConfigFileTP.mcf", 'w')
		f.write("Version = 100\n")
		f.write("Delimiter = #44\n")
		f.write("Export_TTE (Receiving Node,\"Perf_TTE.txt\")\n")
		f.close()
	def writeMusicConfigFileFromNr(self,nr):
		f = open("musicConfigFileTP"+str(nr)+".mcf", 'w')
		f.write("Version = 100\n")
		f.write("Delimiter = #44\n")
		f.write("Export_TTE (Receiving Node,\"Perf_TTE"+str(nr)+".txt\")\n")
		f.close()
	def createInputDialog(self):
		form = ReadTable_Gui(self, QApplication.activeWindow())
		form.exec_()
		return True 
