from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from pydynamind import *
from ReadTable_Gui import *
import shlex

class ReadTable(Module):
	def __init__(self):
	    Module.__init__(self)
	    
	    self.createParameter("FileName", FILENAME,"")
	    self.Filename = ""
	    #Views
	    self.blocks = View("Block", FACE, READ)
	    

	    self.TableData = View("Table Data",COMPONENT,WRITE)
	    self.TableData.addAttribute("Type")
	    self.TableData.addAttribute("Flow")
	    self.TableData.addAttribute("TotalSuspendedSolids")
	    self.TableData.addAttribute("TotalPhosphorus")
	    self.TableData.addAttribute("TotalNitrogen")
	    self.TableData.addAttribute("GrossPollutants")

	    datastream =[]
	    datastream.append(self.TableData)
	    datastream.append(self.blocks)
	    self.addData("City",datastream)

        def run(self):
	    city = self.getData("City")
	    f = open('Perf_TTE.txt','r')
	    text = shlex.shlex(f.read(),posix= True)
	    text.whitespace = ','
	    text.whitespace += '\n'
	    text.whitespace_split = True
	    liste = list(text)
	    for i in [0,1,2]:
		    listData = Component()
		    city.addComponent(listData,self.TableData)
		    listData.addAttribute("Type",liste[1+i])
		    listData.addAttribute("Flow",float(liste[5+i]))
		    listData.addAttribute("TotalSuspendedSolids",float(liste[13+i]))
		    listData.addAttribute("TotalPhosphorus",float(liste[17+i]))
		    listData.addAttribute("TotalNitrogen",float(liste[21+i]))
		    listData.addAttribute("GrossPollutants",float(liste[25+i]))
		    #self.readComp(listData)
		
	'''
	def readComp(self,comp):
	    print comp.getAttribute("Type").getString()
	    print comp.getAttribute("Flow").getDouble()
	    print comp.getAttribute("TotalSuspendedSolids").getDouble()
	    print comp.getAttribute("TotalPhosphorus").getDouble()
	    print comp.getAttribute("TotalNitrogen").getDouble()
	    print comp.getAttribute("GrossPollutants").getDouble()
	'''	    

	def createInputDialog(self):
            form = ReadTable_Gui(self, QApplication.activeWindow())
            form.show()
            return True 
