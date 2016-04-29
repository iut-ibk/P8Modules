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
		self.createReuse = False
		realstring = ""
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
		workpath = self.getHelpUrl()
		workpath += "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		#version with musicfile
		realstring = ""
		for value in strvec:
			simuAttr = city.getComponent(value)
			stringname = simuAttr.getAttribute("msfFilename").getString()
			if (stringname != ""):
				realstring = stringname
			musicNo = int(simuAttr.getAttribute("MusicFileNo").getDouble())
			if (musicNo != 0):
				musicnr = musicNo
		if (realstring != ""):
			tmp = realstring.split(".")
			newname = str(tmp[0] + "TP." + str(tmp[1]))
		else:
			realstring = workpath + "ubeatsMUSIC-ID" + str(musicnr) + ".msf"
			newname = workpath + "ubeatsMUSIC-ID" + str(musicnr) + "TP.msf" 
		self.writeBatFile(newname)
		name = self.readMusicFile(realstring,newname)
		self.writeMusicConfigFile(newname,name)

		print "Music running ..."
		if (platform.system() != "Linux"):
			call([str(workpath) + "RunMusicTP.bat", ""])
		print "Music Done."
		self.calc()
	def readMusicFile(self,filename,newname):
		settings = QSettings()
		if (settings.value("Music").toString().contains("MUSIC 5")):
			import ubeats_music_interface_5 as umusic
		else:
			import ubeats_music_interface as umusic

		largestID = 0
		recvcounter = 0
		foundOutBas = 0
		OutBasId = 0
		receivingnodeid = 0		
		receiveBasName = ""
		getIDforReuse = False
		ReuseIDs = []
		fileIn = open(filename,"r")
		fileOut = open(newname,"w")
		for line in fileIn:
			linearr = line.strip("\n").split(",")

			#get receiving node id
			#this goes over two lines because we first read the node type and then two lines later the id
			if (recvcounter == 2):
					receivingnodeid = int(linearr[1])
					recvcounter = 0
			if (recvcounter == 1):
				recvcounter = 2
			if(linearr[0] == "Node Type"):
				if(linearr[1] == "ReceivingNode"):
					recvcounter = 1
				if(linearr[1] == "WetlandNode" or linearr[1] == "PondNode" or linearr[1] == "RainWaterTankNode"):
					self.createReuse = True
					getIDforReuse = True
			if(linearr[0] == "Node ID"):
				if(largestID < int(linearr[1])):
					largestID = int(linearr[1])
				if(foundOutBas):
					OutBasId = linearr[1]
					foundOutBas = 0
				# get wetland pond an rainwatertank ids to link with reuse node
				if(getIDforReuse):
					ReuseIDs.append(int(linearr[1]))
					getIDforReuse = False
			# if in node name "OUT-Bas" save and set foundOutBas
			if(linearr[0] == "Node Name"):
				if(linearr[1].find("OUT_Bas") != -1):
					receiveBasName = linearr[1]
					foundOutBas = 1
			fileOut.write(line)

		# check for reuse
		if(self.createReuse):
			umusic.writeMUSICjunction2(fileOut, "Re-use",largestID+1,0,0)
			for ids in ReuseIDs:
				umusic.writeTankLinkReuse(fileOut,ids,largestID+1)
 		fileOut.close()

		name = ""
		outid = 0
		# check wheter outbas or recnode has been found
		if(OutBasId == 0 and receivingnodeid != 0):
			name =  "Receiving Node"
			outid = receivingnodeid
		if(OutBasId != 0 and receivingnodeid == 0):
			name = receiveBasName
			outid = OutBasId
		#if we found both we take receiving node id
		if(OutBasId != 0 and receivingnodeid != 0):
			name = "Receiving Node"
			outid = receivingnodeid

		infile = open(filename,"r")
		found = False
		techid = 0
		for line in infile:
			linearr = line.strip("\n").split(",")
			if(linearr[0] == "Source Node ID"):
				if(linearr[1] == outid):
					found = True
			if(found):      
				if(linearr[0] == "Target Node ID"):
					techid = linearr[1]
					break
		infile.close()
		# get name of tech
		infile = open(filename,"r")
		for line in infile:
			linearr = line.strip("\n").split(",")
			if(linearr[0] == "Node Name"):
				tmpname = linearr[1]
			if(linearr[0] == "Node ID" and linearr[1] == techid):
				name = tmpname
				break
		infile.close()      
		print "techname: " + name
		return name


	def writeBatFile(self,file):
		settings = QSettings()
		workpath = self.getHelpUrl() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		f = open(workpath + "RunMusicTP.bat",'w')
		if (platform.system() != "Linux"):
			file = file.replace("/","\\")
		f.write("\"" + settings.value("Music").toString() + "\MUSIC.exe\" \"" + file + "\" \"" + workpath + "musicConfigFileTP.mcf\" -light -silent\n")
		f.close()

	def writeBatFileFromNr(self,nr):
		settings = QSettings()
		workpath = self.getHelpUrl() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		f = open(workpath + "RunMusicTP.bat",'w')
		f.write("\"" + settings.value("Music").toString() + "\MUSIC.exe\" \".\MusicFile-1960PC"+str(nr)+".msf\" \"" + workpath + "musicConfigFile"+str(nr)+".mcf\" -light -silent\n")
		f.close()
	def writeMusicConfigFile(self,file,name):
		settings = QSettings()
		workpath = self.getHelpUrl() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		f = open(workpath + "musicConfigFileTP.mcf", 'w')
		f.write("Version = 100\n")
		f.write("Delimiter = #44\n")
		if(self.createReuse):
			f.write("Export_TS (Re-use, Inflow, \"Reuse.TXT\",1d)\n")
		f.write("Export_TTE ("+str(name)+",\"Perf_TTE.txt\")\n")
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
	def getClassName(self):
		return "Treatment and Harvesting Performance"
	def getFileName(self):
		return "Stormwater"
	def readFileToList(self,Filename):
		f = open(Filename,'r')
		t = shlex.shlex(f.read(),posix= True)
		t.whitespace = ','
		t.whitespace += '\n\r'
		t.whitespace_split = True
		liste = list(t)
		f.close()
		ret = []
		for i in range(len(liste)):
			if i <2 or (i+1)%2:
				continue
			ret.append(liste[i])
		return ret
	def SumAllValues(self,vec):
		sum = 0 
		for i in vec:
			sum += float(i)
		return sum
	def calc(self):
		workpath = self.getHelpUrl() +"/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		if(self.createReuse):
			vec = self.readFileToList(workpath + "Re-use.TXT")
			ReuseSum = self.SumAllValues(vec)
			fileOut = open(workpath + "reusetable.txt","w")
			fileOut.write("Reuse Sum: " + str(ReuseSum))
			fileOut.close()