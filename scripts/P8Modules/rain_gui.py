from PyQt4 import QtCore, QtGui
from pydynamind import *
from PyQt4.QtCore import QSettings, QFileInfo
from PyQt4.QtGui import QMessageBox
from Ui_Rain_Dialog import Ui_P8Rain_GUI
import netCDF4
from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np
import platform
from shutil import copyfile
import os


class RainGui(QtGui.QDialog):
    def __init__(self, m, parent=None):
        self.module = Module
        self.module = m
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_P8Rain_GUI()
        self.ui.setupUi(self)
        self.ui.le_r.setText(self.module.getParameterAsString("Netfile"))
        self.ui.le_csv.setText(self.module.getParameterAsString("csvFile"))
        self.ui.le_ET.setText(self.module.getParameterAsString("etFile"))
        self.ui.le_CoordX1.setText(self.module.getParameterAsString("Xcoord1"))
        self.ui.le_CoordY1.setText(self.module.getParameterAsString("Ycoord1"))
        self.ui.le_CoordX2.setText(self.module.getParameterAsString("Xcoord2"))
        self.ui.le_CoordY2.setText(self.module.getParameterAsString("Ycoord2"))
        self.ui.le_CoordX3.setText(self.module.getParameterAsString("Xcoord3"))
        self.ui.le_CoordY3.setText(self.module.getParameterAsString("Ycoord3"))
        self.ui.le_CoordX4.setText(self.module.getParameterAsString("Xcoord4"))
        self.ui.le_CoordY4.setText(self.module.getParameterAsString("Ycoord4"))
        self.ui.le_CoordX5.setText(self.module.getParameterAsString("Xcoord5"))
        self.ui.le_CoordY5.setText(self.module.getParameterAsString("Ycoord5"))
        self.ui.le_CoordX6.setText(self.module.getParameterAsString("Xcoord6"))
        self.ui.le_CoordY6.setText(self.module.getParameterAsString("Ycoord6"))
        selectedLocation = int(self.module.getParameterAsString("selectedLocation"))
        if(selectedLocation == 1):
            self.ui.radio1.setChecked(True)
        elif(selectedLocation == 2):
            self.ui.radio2.setChecked(True)
        elif(selectedLocation == 3):
            self.ui.radio3.setChecked(True)
        elif(selectedLocation == 4):
            self.ui.radio4.setChecked(True)
        elif(selectedLocation == 5):
            self.ui.radio5.setChecked(True)
        elif(selectedLocation == 6):
            self.ui.radio6.setChecked(True)
        QtCore.QObject.connect(self.ui.pb_preview, QtCore.SIGNAL("released()"), self.preview)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_values)
        QtCore.QObject.connect(self.ui.pb_r, QtCore.SIGNAL("released()"), self.load)
        QtCore.QObject.connect(self.ui.pb_csv, QtCore.SIGNAL("released()"), self.loadcsv)
        QtCore.QObject.connect(self.ui.pb_ET, QtCore.SIGNAL("released()"), self.loadET)
        
    def preview(self):
        settings = QSettings()
        workpath = settings.value("workPath").toString() + "/"
        if (platform.system() != "Linux"):
            workpath = workpath.replace("/","\\")
        vec = []
        dic = {}
        filename = str(self.ui.le_r.text())
        if (filename != ""):
            a = netCDF4.Dataset(str(workpath) + str(filename),'r',format='NETCDF4')
            variables = a.variables.keys()
            units = a.variables[variables[3]].units
            a.close()
        else:
            units = "mm/6min"
        if(self.module.UserCsv == "csv"):
            f = open(workpath + self.module.csvFile,"r")
        else:
            if(os.path.exists(workpath + "RainData.csv")):
                f = open(workpath + "RainData.csv","r")
            else:
                if(str(self.ui.le_r.text()) == ""):
                    QMessageBox.about(self, "No Rain File found", "Please import a Rain File")
                else:
                    QMessageBox.about(self, "No Rain File found", "To preview the NetCDF file please run the module first")
                return
        for line in f:
            linearr = line.strip('\n').split(',')
            if (linearr[0] == "Date"):
                continue
            tmpbar = round(float(linearr[1]),1)
            if (tmpbar>0.00):
                if (tmpbar in dic):
                    dic[tmpbar]=dic[tmpbar]+1
                else:
                    dic[tmpbar]=1
        f.close()
        for key, value in dic.iteritems():
            temp = [key,value]
            vec.append(temp)
        svec=sorted(vec)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        count = []
        ind  = []
        for i in svec:
            count.append(i[1])
            ind.append(i[0])
        bars = ax.bar(ind,count,.1,color='blue',edgecolor='none')
        ax.set_title('Rainfall frequency')
        ax.set_ylabel('Frequency [-]')
        ax.set_xlabel('Rainfall ['+units+']')
        plt.show()

    def save_values(self):
        Net = False
        Csv = False
        self.module.setParameterValue("Xcoord1",str(self.ui.le_CoordX1.text()))
        self.module.setParameterValue("Ycoord1",str(self.ui.le_CoordY1.text()))
        self.module.setParameterValue("Xcoord2",str(self.ui.le_CoordX2.text()))
        self.module.setParameterValue("Ycoord2",str(self.ui.le_CoordY2.text()))
        self.module.setParameterValue("Xcoord3",str(self.ui.le_CoordX3.text()))
        self.module.setParameterValue("Ycoord3",str(self.ui.le_CoordY3.text()))
        self.module.setParameterValue("Xcoord4",str(self.ui.le_CoordX4.text()))
        self.module.setParameterValue("Ycoord4",str(self.ui.le_CoordY4.text()))
        self.module.setParameterValue("Xcoord5",str(self.ui.le_CoordX5.text()))
        self.module.setParameterValue("Ycoord5",str(self.ui.le_CoordY5.text()))
        self.module.setParameterValue("Xcoord6",str(self.ui.le_CoordX6.text()))
        self.module.setParameterValue("Ycoord6",str(self.ui.le_CoordY6.text()))
        filename = str(self.ui.le_ET.text())
        if(filename != ""):
            self.module.setParameterValue("etFile", filename)
        filename = str(self.ui.le_r.text())
        if (filename != ""):
            Net = True
            self.module.setParameterValue("Netfile", filename)
        filename = str(self.ui.le_csv.text())
        if (filename != ""):
            Csv = True
            self.module.setParameterValue("csvFile",filename)
        if (not(Net or Csv)):
            print "Warning: no File Selected"
        if(Csv):
            self.module.setParameterValue("UserCsv", "csv")
        elif(Net):
            self.module.setParameterValue("UserCsv", "net")

        if(self.ui.radio1.isChecked()):
            self.module.setParameterValue("selectedLocation",str(1))
        elif(self.ui.radio2.isChecked()):
            self.module.setParameterValue("selectedLocation",str(2))
        elif(self.ui.radio3.isChecked()):
            self.module.setParameterValue("selectedLocation",str(3))
        elif(self.ui.radio4.isChecked()):
            self.module.setParameterValue("selectedLocation",str(4))
        elif(self.ui.radio5.isChecked()):
            self.module.setParameterValue("selectedLocation",str(5))
        elif(self.ui.radio6.isChecked()):
            self.module.setParameterValue("selectedLocation",str(6))


    def load(self):
        settings = QSettings()
        workpath = settings.value("workPath").toString() + "/"
        datapath = settings.value("dataPath").toString() + "/"
        if (platform.system() != "Linux"):
            workpath = workpath.replace("/","\\")
            datapath = datapath.replace("/","\\")
        filename = QtGui.QFileDialog.getOpenFileName(self, "Open Rain File", datapath, self.tr("Rain Files (*.nc)"))
        if(filename != ""):
            self.module.setParameterValue("Netfile", str(QFileInfo(filename).fileName()))
            self.ui.le_r.setText(QFileInfo(filename).fileName())
            settings.setValue("dataPath",QFileInfo(filename).absolutePath())
            copyfile(filename,workpath + QFileInfo(filename).fileName())
    def loadcsv(self):
        settings = QSettings()
        workpath = settings.value("workPath").toString() + "/"
        datapath = settings.value("dataPath").toString() + "/"
        if (platform.system() != "Linux"):
            workpath = workpath.replace("/","\\")
            datapath = datapath.replace("/","\\")
        filename = QtGui.QFileDialog.getOpenFileName(self, "Open Rain File", datapath, self.tr("Rain Files (*.csv)"))
        if(filename != ""):
            self.module.setParameterValue("csvFile", str(QFileInfo(filename).fileName()))
            self.ui.le_csv.setText(QFileInfo(filename).fileName())
            settings.setValue("dataPath",QFileInfo(filename).absolutePath())
            copyfile(filename,workpath + QFileInfo(filename).fileName())
            self.module.setParameterValue("UserCsv", "csv")

    def loadET(self):
        settings = QSettings()
        workpath = settings.value("workPath").toString() + "/"
        datapath = settings.value("dataPath").toString() + "/"
        if (platform.system() != "Linux"):
            workpath = workpath.replace("/","\\")
            datapath = datapath.replace("/","\\")
        filename = QtGui.QFileDialog.getOpenFileName(self, "Open ET File", datapath, self.tr("Rain Files (*.txt)"))
        if(filename != ""):
            self.module.setParameterValue("etFile", str(QFileInfo(filename).fileName()))
            self.ui.le_ET.setText(QFileInfo(filename).fileName())
            settings.setValue("dataPath",QFileInfo(filename).absolutePath())
            copyfile(filename,workpath + QFileInfo(filename).fileName())
            self.module.setParameterValue("UserCsv","net")