from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from pydynamind import *
from rain_gui import *
import netCDF4
from matplotlib import *
import matplotlib.pyplot as plt
import tempfile
import datetime
import numpy as np
import os
import osgeo.ogr as ogr
import osgeo.osr as osr

class RainModule(Module):
	def __init__(self):
		Module.__init__(self)
		self.createParameter("FileName", FILENAME, "")
		self.FileName = ""
		self.createParameter("csvFile",FILENAME,"")
		self.csvFile = ""
		self.createParameter("UserCsv", DOUBLE, "")
		self.UserCsv = 0
		self.simulation = View("SimulationData",COMPONENT,WRITE)
		self.simulation.addAttribute("UserCsv")

		datastream = []
		datastream.append(self.simulation)
		self.addData("City",datastream)


	def run(self):
		dataflow = self.getData("City")
		if (self.UserCsv):
			simu = Component()
			simu.addAttribute("UserCsv",int(self.UserCsv))
			dataflow.addComponent(simu,self.simulation)
		else:
			dataflow = self.getData("City")

			data = netCDF4.Dataset(self.FileName)#'/home/csam8457/Documents/P8-WSC/P8Modules/scripts/P8Modules/demo.nc' ,'r',format='NETCDF4')
			print "Start reading Rain Data"
			datas = self.getRainData(151.25,-34.05,data)
			f = open("RainData.csv",'w')
			f.write(str(data.variables['time'][1]-data.variables['time'][0])+"\n")
			print "Start writing Rain Data"
			size = float(data.variables['time'].size)
			oldpercent = 0
			newpercent = float(0)
			i = 0
			while (i < size):
				newpercent = float((float(i) /float(size)) * float(100))
				if(oldpercent < int(newpercent)):
					oldpercent = int(newpercent)
					print "Writing Rain-Data " + str(oldpercent) + "%"
				f.write(str(datetime.datetime.fromtimestamp(int(data.variables['time'][i])).strftime('%d/%m/%Y %H:%M:%S'))+","+str(datas[i])+"\n")
				i = i +1
			f.close()
			print "Done"
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
	def createInputDialog(self):
            form = RainGui(self, QApplication.activeWindow())
            form.show()
            return True 
	def find_nearest(self,array,value):
    	    idx=(np.abs(array-value)).argmin()
    	    return array[idx]	
	def getRainData(self,xValue, yValue, netCDF):

	    #convert xvalue
	    #convert yvalue

	    longs = doublevector()
	    longs = netCDF.variables['longitude'][:]
	    lats = doublevector()
	    lats = netCDF.variables['latitude'][:]
	    #looking here in the netCDF vector for the index of our values
	    
	    x = self.find_nearest(longs,xValue)#numpy.where(longs==xValue) #use find_nearest func with the real coodinates
	    y = self.find_nearest(lats,yValue)#numpy.where(lats==yValue)
	    datas = Attribute().getDoubleVector()
	    size = netCDF.variables['time'].size
	    counter = long(0)
	    oldpercent = 0
	    newpercent = float(0)
	    while (counter < size):#for i in range(0,netCDF.variables['precipitation'].size,1):
	    	
	    	newpercent = float((float(counter) /float(size)) * float(100))
	    	if(oldpercent < int(newpercent)):
	    		oldpercent = int(newpercent)
	    		print "Reading Rain-Data " + str(oldpercent) + "%"
	    	datas.append(float(netCDF.variables['precipitation'][counter][int(lats[y])][int(longs[x])]))
	    	counter = counter + 1
	    	#print netCDF.variables['rain'][i][int(lats[y])][int(longs[x])]
	    return datas






