from PyQt4 import QtCore, QtGui
from pydynamind import *
from Ui_Rain_Dialog import Ui_P8Rain_GUI
import netCDF4
from matplotlib import *
import matplotlib.pyplot as plt
import tempfile
import datetime
import numpy as np

class Rain(Module):
	def __init__(self):
	    Module.__init__(self)
	    self.createParameter("FileName", FILENAME, "")
	    self.FileName = ""
#            self.createParameter("Rain",DOUBLE,"Sample Description")
#            self.Rain = 0
 
            datastream = []
            self.blocks = View("SUPERBLOCK", FACE, READ)
            self.blocks.addAttribute("Rain")

            datastream.append(self.blocks)
            self.addData("Catchment", datastream)



        def run(self):
            dataflow = self.getData("Catchment")
            catchments = dataflow.getUUIDsOfComponentsInView(self.blocks) 

            data = netCDF4.Dataset('/home/csam8457/Documents/P8-WSC/P8Modules/scripts/P8Modules/demo.nc' ,'r',format='NETCDF4')

	    
            #time = data.variables['time']
	    #print "lon: " + str(a.variables['lon'][125])
	    #print "lat: " + str(a.variables['lat'][125])
	    
	    
            '''plt.plot(data)
            filename = "plot"
            filename+= "rain"
            filename+= ".png"
            print tempfile.gettempdir()
            plt.savefig(tempfile.gettempdir()+'/'+filename)
            plt.close()
            '''
	    
	    times = stringvector()

	    # read the time stamps and convert it to a 2012-12-31 23:59:59 format
	    for i in range(0,data.variables['time'].size,1):
		times.append(datetime.datetime.fromtimestamp(int(data.variables['time'][i])).strftime('%Y-%m-%d %H:%M:%S'))
	    #read all blocks and add a rain attribute
	    for catch in catchments:                
                block = dataflow.getComponent(catch)  
                rainattr = Attribute("Rain")
		# the first two parameters have to bet the x and y position of the block
		datas = self.getRainData(151.25,-34.05,data)[:]
		rainattr.addTimeSeries(times,datas)
                block.addAttribute(rainattr)
	    
	
	      
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
	    longs = netCDF.variables['lon'][:]
	    lats = doublevector()
	    lats = netCDF.variables['lat'][:]
	    #looking here in the netCDF vector for the index of our values
	    
	    x = numpy.where(longs==xValue) #use find_nearest func with the real coodinates
	    y = numpy.where(lats==yValue)
	    datas = Attribute().getDoubleVector()
	    for i in range(0,len(netCDF.variables['rain'][:]),1):
	    	datas.append(float(netCDF.variables['rain'][i][int(y[0])][int(x[0])]))
	    return datas






