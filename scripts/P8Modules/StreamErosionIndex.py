# -*- coding: utf-8 -*-

from StreamErosionIndex_guic import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pydynamind import *
import math
import ubeats_music_interface as umusic
from operator import itemgetter
import numpy as np
import os
import platform
from subprocess import call

class StreamErosionIndex(Module):


    def __init__(self):
        Module.__init__(self)

        self.createParameter("Csvfile",STRING,"")
        self.Csvfile = ""
        self.createParameter("ETfile",STRING,"")
        self.ETfile = ""
        self.createParameter("alpha",DOUBLE,"")
        self.alpha = 0.4
        self.createParameter("NoY",DOUBLE,"")
        self.NoY = 10
        self.createParameter("SimulationCity",DOUBLE,"")
        self.SimulationCity = 2

        self.simulation = View("SimulationData",COMPONENT,WRITE)
        self.simulation.getAttribute("msfFilename")
        self.simulation.addAttribute("SEIurb")
        self.simulation.addAttribute("SEIwsud")
        self.simulation.addAttribute("NoY")
        self.simulation.addAttribute("alpha")


        datastream = []
        datastream.append(self.simulation)
        self.addData("City", datastream)

    def run(self):
        city = self.getData("City")
        strvec = city.getUUIDsOfComponentsInView(self.simulation)
        for value in strvec:
            simuAttr = city.getComponent(value)
            stringname = simuAttr.getAttribute("msfFilename").getString()
            if (stringname != ""):
                Filename = stringname
        
        self.changeMusicFile(Filename) #running music in function
        '''if(platform.system() == "Linux"):
            Pre = self.readTimeSeries("Pre-developedCatchment.csv")
            Urb = self.readTimeSeries("Pre-developedCatchment.csv")
            PostWSUD = self.readTimeSeries("Pre-developedCatchment.csv")
        else:
        '''
        Pre = self.readTimeSeries("Pre-developedCatchment.csv")
        Urb = self.readTimeSeries("UrbanisedCatchment.csv")
        PostWSUD = self.readTimeSeries("PostWSUD.csv")
        idx =  self.findNearest(Pre,2)
        upper = []
        lower = []
        upper.append(float(Pre[idx][1]))
        upper.append(float(Pre[idx][3]))
        lower.append(float(Pre[idx+1][1]))
        lower.append(float(Pre[idx+1][3]))
        m = (upper[0] - lower[0]) / (upper[1] - lower[1])
        Q2 = lower[0] + m * (2 -lower[1])
        #write tables for analyzer
        f = open("pretable.csv","w")
        for line in Pre:
            f.write(str(line[1]) + "," + str(line[3]) + "\n")
        f.close()
        f = open("urbtable.csv","w")
        for line in Urb:
            f.write(str(line[1]) + "," + str(line[3]) + "\n")
        f.close()
        f = open("wsudtable.csv","w")
        for line in PostWSUD:
            f.write(str(line[1]) + "," + str(line[3]) + "\n")
        f.close()

        #read csv new long time serie
        Pre = self.readLongTimeSeries("Pre-developedCatchment.csv")
        Urb = self.readLongTimeSeries("UrbanisedCatchment.csv")
        PostWSUD = self.readLongTimeSeries("PostWSUD.csv")
        #then do the calculation
        print "Q2: " + str(Q2)
        sumFlowPre = 0.0
        sumFlowUrb = 0.0
        sumFlowWSUD = 0.0
        for line in Pre:
            if(float(line[1])<(Q2/2)):
                line[1] = 0
            else:
                line[1] = float(line[1]) - (Q2/2)
                sumFlowPre = sumFlowPre + float(line[1])
        for line in Urb:
            if(float(line[1])<(Q2/2)):
                line[1] = 0
            else:
                line[1] = float(line[1])- (Q2/2)
                sumFlowUrb = sumFlowUrb + line[1]
        for line in PostWSUD:
            if(float(line[1])<(Q2/2)):
                line[1] = 0
            else:
                line[1] = float(line[1])- (Q2/2)
                sumFlowWSUD = sumFlowWSUD + line[1]
        SEIurb = sumFlowUrb / sumFlowPre
        SEIwsud = sumFlowWSUD / sumFlowPre

        simu = Component()
        simu.addAttribute("SEIurb", SEIurb)
        simu.addAttribute("SEIwsud", SEIwsud)
        simu.addAttribute("NoY", self.NoY)
        simu.addAttribute("alpha", self.alpha)
        city.addComponent(simu,self.simulation)
    def readLongTimeSeries(self,filename):
        #only reads timeserie and puts it into a vector without changing any of the data inside
        arr = []
        first = True
        f = open(filename,"r")
        date = ""
        value = 0.0
        for line in f:
            linearr = line.strip("\n").split(",")
            if(first):
                first = False
                continue
            if(date == ""):#set values first time
                date = linearr[0]
                value = linearr[1]
            new = []
            new.append(date)
            new.append(value)
            new.append(0)
            new.append(0.0)
            arr.append(new)
            date = linearr[0]
            value = linearr[1]
        f.close()
        arr.sort(key = itemgetter(1), reverse = True) #sort by value and biggest to highest
        i = 0
        for line in arr:
            i = i + 1
            line[2] = i
            line[3] = (int(self.NoY) + 1 - 2 * float(self.alpha)) / (i - float(self.alpha))
        return arr

    def readTimeSeries(self,filename):
        # reads time series and also calculates the biggest value of each day
        arr = []
        first = True
        f = open(filename,"r")
        date = ""
        value = 0.0
        for line in f:
            linearr = line.strip("\n").split(",")
            if(first):
                first = False
                continue
            if(date == ""):#set values first time
                date = linearr[0]
                value = linearr[1]
            if(date.split(" ")[0] == linearr[0].split(" ")[0]):#if date same as last line
                if(value < linearr[1]):#if value bigger than last saved line
                    date = linearr[0]
                    value = linearr[1]
            else:#new day save value and date in array
                new = []
                new.append(date)
                new.append(value)
                new.append(0)
                new.append(0.0)
                arr.append(new)
                date = linearr[0]
                value = linearr[1]
        f.close()
        new = []#last day saved in array
        new.append(date)
        new.append(value)
        new.append(0)
        new.append(0.0)
        arr.append(new)
        arr.sort(key = itemgetter(1), reverse = True) #sort by value and biggest to highest
        i = 0
        for line in arr:
            i = i + 1
            line[2] = i
            line[3] = (int(self.NoY) + 1 - 2 * float(self.alpha)) / (i - float(self.alpha))
        return arr
    def findNearest(self, array, value):
        tmp = []
        for line in array:
            tmp.append(line[3] - value)
        idx = (np.abs(tmp)).argmin()
        if(array[idx][3] > value): #return index of bigger value than "value"
            return idx
        else:
            return idx -1
    def writeBatFileFromFile(self,file):
        f = open("RunMusicSEI.bat",'w')
        filearr = file.split(".")
        f.write("\"C:\Program Files (x86)\eWater\MUSIC 5 5.1.18.172 SL\MUSIC.exe\" \""+ filearr[0] + "SEI." + filearr[1] +"\" \".\musicConfigFileSEI.mcf\" -light -silent\n")
        f.close()
    def writeMusicConfigFile(self):
        f = open("musicConfigFileSEI.mcf", 'w')
        f.write("Version = 100\n")
        f.write("Delimiter = #44\n")
        f.write("Export_TS (Pre-developed Catchment, Outflow, \"Pre-developedCatchment.csv\")\n")
        f.write("Export_TS (Urbanised Catchment, Outflow, \"UrbanisedCatchment.csv\")\n")
        f.write("Export_TS (Receiving Node, Inflow, \"PostWSUD.csv\")\n")
        f.close()
    def changeMusicFile(self,filename):
        self.writeBatFileFromFile(filename)
        self.writeMusicConfigFile()

        #read start- , enddate and timestep from csv
        startdate = ""
        enddate = ""
        timestep = 0
        counter = 0
        files = self.getRainEtFile()
        f = open(files[0],"r")
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
                #timestep = timestep + int(tmp[2]) - int(tmp2[2])
        enddate = linearr[0].split(" ")[0]
        startdate = startdate[0]
        f.close()
        infile = open(filename,"r")
        filearr = filename.split(".")
        outfile = open(filearr[0] + "SEI." + filearr[1] ,"w")
        urbansourcenode = False
        calcarea = False
        readcatchmentlist = False
        impArea = 0.0
        perArea = 0.0
        area = 0.0
        imp = 0.0
        per = 0.0
        ID = 0
        catchment_paramter_list = []#[1,120,30,20,200,1,10,25,5,0] old static parameter list
        for line in infile:
            linearr = line.strip("\n").split(",")
            if(linearr[0] == "Node Type"):
                if (linearr[1] == "UrbanSourceNode"):
                    urbansourcenode = True
            if(urbansourcenode):
                if(linearr[0] == "Areas - Total Area (ha)"):
                    area = float(linearr[1])
                    print "area: " + str(area)
                if(linearr[0] == "Areas - Impervious (%)"):
                    imp = float(linearr[1])
                    print "imp: " + str(imp)
                if(linearr[0] == "Areas - Pervious (%)"):
                    per = float(linearr[1])
                    print "per: " + str(per)
                    calcarea = True
                #first line of parameter list
                if(linearr[0] == "Rainfall-Runoff - Impervious Area - Rainfall Threshold (mm/day)"):
                    readcatchmentlist = True
                if(readcatchmentlist):
                    catchment_paramter_list.append(linearr[1])
                #last line of parameter list
                if(linearr[0] == "Rainfall-Runoff - Groundwater Properties - Daily Deep Seepage Rate (%)"):
                    readcatchmentlist = False

            if(calcarea):  
                impArea = impArea + (area * imp / 100)
                perArea = perArea + area
                print "perArea: " + str(perArea)
                print "impArea: " + str(impArea)
                calcarea = False
                UrbanSourceNode = False

            if(linearr[0] == "Node ID"):
                if(linearr[1] >= ID):
                    ID = int(linearr[1]) + 1
            if (linearr[0] == "MeteorologicalTemplate"):
                outfile.write("RainfallFile," + files[0] +"\n")
                outfile.write("PETFile," + files[1] + "\n")
                outfile.write("StartDate," + startdate + "\n")
                outfile.write("EndDate," + enddate + "\n")
                outfile.write("Timestep," + str(timestep) + "\n")
            else:
                outfile.write(line)
        umusic.writeMUSICcatchmentnodeEro(outfile,"Pre-developed Catchment",ID,perArea,False,catchment_paramter_list) #pervious
        umusic.writeMUSICcatchmentnodeEro(outfile,"Urbanised Catchment",ID + 1,impArea,True,catchment_paramter_list) #impervious
        infile.close()
        outfile.close()
        print "Impervious Area: " + str(impArea)
        print "Pervious Area: " + str(perArea)
        #Run music
        print "Music is running ... "
        if (platform.system() != "Linux"):
            call(["RunMusicSEI.bat", ""])
        print "Music Done."
    def getRainEtFile(self):
        #checks wether the user chose a rain file or a city
        #return an array with the path of rainfile and the ET file in it
        files = []
        if(self.Csvfile == ""):
            files.append("C:/Program Files (x86)/hydro-IT/P8-WSC/Data2Store4ErosionIndex/Melbourne Rainfall 1985_1995 6min.csv")
        else:
            files.append(self.Csvfile)
        if(self.ETfile == ""):
            if(self.SimulationCity == 0):
                files.append("C:\Program Files (x86)\hydro-IT\P8-WSC\Data2Store4ErosionIndex\Adelaide Monthly Areal PET.txt")
            elif(self.SimulationCity == 1):
                files.append("C:\Program Files (x86)\hydro-IT\P8-WSC\Data2Store4ErosionIndex\Brisbane Monthly Areal PET.txt")
            elif(self.SimulationCity == 2):
                files.append("C:\Program Files (x86)\hydro-IT\P8-WSC\Data2Store4ErosionIndex\Melbourne Monthly Areal PET.txt")
            elif(self.SimulationCity == 3):
                files.append("C:\Program Files (x86)\hydro-IT\P8-WSC\Data2Store4ErosionIndex\Perth Monthly Areal PET.txt")
            elif(self.SimulationCity == 4):
                files.append("C:\Program Files (x86)\hydro-IT\P8-WSC\Data2Store4ErosionIndex\Sydney Monthly Areal PET.txt")
        else:
            files.append(self.ETfile)
        if (platform.system() != "Linux"): #dynamics path slashes depeding on os
            files[0] = files[0].replace("/","\\")
            files[1] = files[1].replace("/","\\")
        return files
    def createInputDialog(self):
        form = activateStreamErosionIndexGUI(self, QApplication.activeWindow())
        form.exec_()
        return True 
