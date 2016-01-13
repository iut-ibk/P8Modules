from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from pydynamind import *
from rain_gui import *
import netCDF4
from matplotlib import *
import matplotlib.pyplot as plt
import tempfile
import datetime
import time as zeit
from datetime import date
import numpy as np
import os
import osgeo.ogr as ogr
import osgeo.osr as osr
import platform

class RainModule(Module):
	def __init__(self):
		Module.__init__(self)
		self.createParameter("Netfile", STRING, "")
		self.Netfile = ""
		self.createParameter("csvFile", STRING,"")
		self.csvFile = ""
		self.createParameter("UserCsv", STRING, "")
		self.UserCsv = ""
		self.createParameter("etFile", STRING, "")
		self.etFile = ""
		self.createParameter("Xcoord1", DOUBLE , "")
		self.Xcoord1 = 0
		self.createParameter("Ycoord1", DOUBLE ,"")
		self.Ycoord1 = 100
		self.createParameter("Xcoord2", DOUBLE , "")
		self.Xcoord2 = 144.98
		self.createParameter("Ycoord2", DOUBLE ,"")
		self.Ycoord2 = -37.83
		self.createParameter("Xcoord3", DOUBLE , "")
		self.Xcoord3 = 145.22
		self.createParameter("Ycoord3", DOUBLE ,"")
		self.Ycoord3 = -37.98
		self.createParameter("Xcoord4", DOUBLE , "")
		self.Xcoord4 = 144.98
		self.createParameter("Ycoord4", DOUBLE ,"")
		self.Ycoord4 = -37.42
		self.createParameter("Xcoord5", DOUBLE , "")
		self.Xcoord5 = 144.57
		self.createParameter("Ycoord5", DOUBLE ,"")
		self.Ycoord5 = -37.75
		self.createParameter("Xcoord6", DOUBLE , "")
		self.Xcoord6 = 145.55
		self.createParameter("Ycoord6", DOUBLE ,"")
		self.Ycoord6 = -37.64
		self.createParameter("selectedLocation", DOUBLE, "")
		self.selectedLocation = 1
		self.simulation = View("SimulationData",COMPONENT,WRITE)
		self.simulation.addAttribute("UserCsv")
		self.simulation.getAttribute("msfFilename")
		self.simulation.addAttribute("SEIurb")
		self.simulation.addAttribute("SEIwsud")	
		self.simulation.addAttribute("NoY")
		self.simulation.addAttribute("alpha")

		datastream = []
		datastream.append(self.simulation)
		self.addData("City",datastream)


	def run(self):
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		dataflow = self.getData("City")
		strvec = dataflow.getUUIDsOfComponentsInView(self.simulation)
		for value in strvec:
			simuAttr = dataflow.getComponent(value)
			stringname = simuAttr.getAttribute("msfFilename").getString()
			if (stringname != ""):
				realstring = stringname
		self.timestep = 0
		self.startdate = ""
		self.enddate = ""
		if (self.UserCsv == "csv"):
			simu = Component()
			simu.addAttribute("UserCsv",self.UserCsv)
			dataflow.addComponent(simu,self.simulation)
			self.changeMusicFile(realstring,str(workpath + self.csvFile))
			tmp = realstring.split(".")
			simuAttr.changeAttribute("msfFilename", str(tmp[0]) + "NewRain." + str(tmp[1]))
		elif(self.UserCsv == "net"):
			
			data = netCDF4.Dataset(str(workpath + self.Netfile))#'/home/csam8457/Documents/P8-WSC/P8Modules/scripts/P8Modules/demo.nc' ,'r',format='NETCDF4')
			print "Start reading Rain Data"
			time = data.variables["time"][:]
			rain = data.variables["rain"][:]
			for i in range(int(self.Xcoord1), int(self.Ycoord1)):
				self.createRainCSV(time,rain[i],workpath, i)
				self.createMusicFile(realstring, workpath + "stimulation" + str(i+1) + ".csv", i)

			
		else:
			print "nothing"
		'''old code for old rain file
            #time = data.variables['time']
	    #print "lon: " + str(a.variables['lon'][125])
	    #print "lat: " + str(a.variables['lat'][125])
	    
	    

	    
	    times = stringvector()

	    # read the time stamps and convert it to a 2012-12-31 23:59:59 format
	    for i in range(0,data.variables['time'].size,1):
		times.append(datetime.datetime.fromtimestamp(int(data.variables['time'][i])).strftime('%Y-%m-%d %H:%M:%S'))
	    datas = self.getRainData(151.25,-34.05,data)
	    
	    f = open("RainData.txt",'w')
	    for i in range(len(times)):
		f.write(str(times[i])+","+str(datas[i])+"\n")
	    f.close()
	    print "done"
	    #read all blocks and add a rain attribute
	    
	    i = 0
	    
	    for catch in catchments:
                block = dataflow.getFace(catch)
		nodes = block.getNodes()
		n = dataflow.getNode(nodes[0])
		n1 = dataflow.getNode(nodes[1])
		n2 = dataflow.getNode(nodes[2])
		x = (n.getX() + n1.getX())/2
		y = (n1.getY() + n2.getY())/2
		x = x + xoffset
		y = y + yoffset
		wtk = 'POINT(%s %s)' % (x, y)

		#CREATE PROJECTION OBJECTS
		target = osr.SpatialReference()
		target.ImportFromEPSG(32755)

		source = osr.SpatialReference()
		source.ImportFromEPSG(4326)
		
		# CREATE OGR POINT OBJECT, ASSIGN PROJECTION, REPROJECT
		point = ogr.CreateGeometryFromWkt(wtk)
		point.AssignSpatialReference(target)
	    
		point.TransformTo(source)
	    	#print "old: " + str(x) + " " + str(y)
		#print "new: " + str(point.GetX()) + " " + str(point.GetY())
	      
                rainattr = Attribute("Rain")
		# the first two parameters have to bet the x and y position of the block
		datas = self.getRainData(point.GetX(),point.GetY(),data)[:]
		rainattr.addTimeSeries(times,datas)
                block.addAttribute(rainattr)
		i = i + 1
	    	print "Adding Rain to Blocks: " + str(i) + " of " + str(len(catchments))
	    '''

	def createRainCSV(self, time, rain, workpath, count):
		t0 = zeit.time()
		
		self.timestep = (time[101] - time[100]) / 60
		self.startdate = datetime.datetime.fromtimestamp(int(time[100])).strftime('%d/%m/%Y %H:%M:%S')
		self.enddate = datetime.datetime.fromtimestamp(int(time[len(time)-1])).strftime('%d/%m/%Y %H:%M:%S')


		#print "Start writing Rain Data for Location " + str(count+1)
		size = len(time)
		data = ""
		#oldpercent = 0
		#newpercent = 0

		i = 0
		while (i < size):
			#newpercent = float((float(i) /float(size)) * float(100))
			#if(oldpercent < int(newpercent)):
				#oldpercent = int(newpercent)
				#print "Writing Rain-Data for Location " + str(count+1) + " " + str(oldpercent) + "%"
			data += str(datetime.datetime.fromtimestamp(int(time[i])).strftime('%d/%m/%Y %H:%M:%S'))+","+str(rain[i] * self.timestep / 60)+"\n"
			i = i +1
		f = open(workpath + "stimulation" + str(count+1) + ".csv",'w')
		f.write("Date,Rainfall\n")
		f.write(data)
		f.close()
		t1 = zeit.time()
		print "Done Simu " + str(count + 1) + " in " + str(t1-t0) + " secs"
	def createMusicFile(self, musicf, csvf, count):
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		infile = open(musicf,"r")
		tmpfile = musicf.split(".")
		outfile = open(str(tmpfile[0]) + "NewRainWithLocation" + str(count) + "." + tmpfile[1] ,"w")
		csvf = csvf.replace("/","\\")
		if(self.etFile != ""):
			etfile = str(workpath + self.etFile.replace("/","\\"))
		else:
			etfile = "C:\Program Files (x86)\hydro-IT\P8-WSC\ClimateDataTemplates\Melbourne Monthly Areal PET.txt"
		for line in infile:
			linearr = line.strip("\n").split(",")
			if (linearr[0] == "MeteorologicalTemplate"):
				outfile.write("RainfallFile," + csvf +"\n") #todo check if pathes are correct for music
				outfile.write("PETFile," + etfile + "\n")
				outfile.write("StartDate," + self.startdate + "\n")
				outfile.write("EndDate," + self.enddate + "\n")
				outfile.write("Timestep," + str(self.timestep) + "\n")
			else:
				outfile.write(line)
		infile.close()
		outfile.close()

	def changeMusicFile(self, musicf, csvf):
		settings = QSettings()
		workpath = settings.value("workPath").toString() + "/"
		if (platform.system() != "Linux"):
			workpath = workpath.replace("/","\\")
		startdate = ""
		enddate = ""
		timestep = 0
		counter = 0
		f = open(csvf,"r")
		for line in f:
			counter = counter + 1
			linearr = line.strip("\n").split(",")
			if (counter == 2):
				startdate = linearr[0].split(" ")
			if (counter == 3):
				tmp = linearr[0].split(" ")[1].split(":")
				tmp2 = startdate[1].split(":")
				timestep = int(tmp[0]) * 360 - int(tmp2[0]) * 360
				timestep = timestep + (int(tmp[1]) * 60 - int(tmp2[1]) * 60)
				#timestep = timestep + int(tmp[2]) - int(tmp2[2]) 			#not considering seconds into timestep calc
		enddate = linearr[0].split(" ")[0]
		startdate = startdate[0]
		print startdate
		print enddate
		print timestep
		f.close()
		infile = open(musicf,"r")
		tmpfile = musicf.split(".")
		outfile = open(str(tmpfile[0]) + "NewRain." + tmpfile[1] ,"w")
		csvf = csvf.replace("/","\\")
		if(self.etFile != ""):
			etfile = str(workpath + self.etFile.replace("/","\\"))
		else:
			etfile = "C:\Program Files (x86)\hydro-IT\P8-WSC\ClimateDataTemplates\Melbourne Monthly Areal PET.txt"
		for line in infile:
			linearr = line.strip("\n").split(",")
			if (linearr[0] == "MeteorologicalTemplate"):
				outfile.write("RainfallFile," + csvf +"\n") #todo check if pathes are correct for music
				outfile.write("PETFile," + etfile + "\n")
				outfile.write("StartDate," + startdate + "\n")
				outfile.write("EndDate," + enddate + "\n")
				outfile.write("Timestep," + str(timestep) + "\n")
			else:
				outfile.write(line)
		infile.close()
		outfile.close()

	def createInputDialog(self):
		form = RainGui(self, QApplication.activeWindow())
		form.exec_()
		return True 
	def find_nearest(self,array,value):
		idx=(np.abs(array-value)).argmin()
		#print "Index " + str(idx)
		return idx
	def checkCoords(self,netCDF,x,y):
		xWrong = False
		yWrong = False

		longs = doublevector()
		lats = doublevector()
		coords = self.getlonglat(netCDF)
		longs = coords[0]
		lats = coords[1]
		print x
		print str(longs[0]) + " " + str(longs[len(longs)-1])
		print y
		print str(lats[0]) + " " + str(lats[len(lats)-1])

		#check which end of longs has smallest coords
		if(longs[0] < longs[len(longs)-1]):
			if(x < longs[0] or x > longs[len(longs)-1]):
				xWrong = True
		else:
			if(x < longs[len(longs)-1]) or x > longs[0]:
				xWrong = True

		#check which end of lats has smallest coords
		if(lats[0] < lats[len(lats)-1]):
			if(y < lats[0] or y > lats[len(lats)-1]):
				yWrong = True
		else:
			if(y < lats[len(lats)-1] or y > lats[0]):
				yWrong = True
		print xWrong
		print yWrong
		if( yWrong or yWrong):
			#todo show warning messagebox
			#QMessageBox.warning(QApplication.activeWindow(),QString("Warning"),QString("Wrong Coords"), QMessageBox.Ok)
  			return True
		return False


	def getRainData(self,xValue, yValue, netCDF):
		#convert xvalue
		#convert yvalue
		print "netcdf " + str(netCDF)

		variables = netCDF.variables.keys()
		#print "variables " + str(variables)

		longs = doublevector()
		lats = doublevector()
		coords = self.getlonglat(netCDF)
		longs = coords[0]
		lats = coords[1]
		rain = self.getRainFromNetCDF(netCDF)
		#looking here in the netCDF vector for the index of our values
		#print "LONGS"
		#print longs
		#print "LATS"
		#print lats

		x = self.find_nearest(longs,xValue)#numpy.where(longs==xValue) #use find_nearest func with the real coodinates
		y = self.find_nearest(lats,yValue)#numpy.where(lats==yValue)

		print x
		print y


		self.timestep = (netCDF.variables[variables[2]][1] - netCDF.variables[variables[2]][0]) / 60 #get timestep in minutes


		datas = Attribute().getDoubleVector()
		size = netCDF.variables[variables[2]].size #time
		counter = long(0)
		oldpercent = 0
		newpercent = float(0)
		while (counter < size):#for i in range(0,netCDF.variables['precipitation'].size,1):
			
			newpercent = float((float(counter) /float(size)) * float(100))
			if(oldpercent < int(newpercent)):
				oldpercent = int(newpercent)
				print "Reading Rain-Data " + str(oldpercent) + "%"
			datas.append(float(rain[counter,y,x])) #prec
			counter = counter + 1
			#print netCDF.variables['rain'][i][int(lats[y])][int(longs[x])]
		return datas

	# returns long and lats array from a netCDF file
	# searches for "lat" and "lon"
	def getlonglat(self,data):
		ret = []
		variables = data.variables.keys()
		longs = doublevector()
		lats = doublevector()
		for var in variables:
			if(var.find("lat") >= 0):
				lats = data.variables[var][:]
			if(var.find("lon") >= 0):
				longs = data.variables[var][:]
		ret.append(longs)
		ret.append(lats)
		return ret

	# returns rain array from netCDF file
	# searches for "rain" or "prec"
	def getRainFromNetCDF(self, data):
		variables = data.variables.keys()

		for var in variables:
			if(var.find("rain") >= 0):
				return data.variables[var]
			if(var.find("prec") >= 0):
				return data.variables[var]

	def getClassName(self):
		return "Future Rainfall (Test Version)"
	def getFileName(self):
		return "Scenario Definition"