from PyQt4 import QtCore, QtGui
from pydynamind import *
from Ui_Rain_Dialog import Ui_P8Rain_GUI
import netCDF4
from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np
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
        self.ui.le_CoordX.setText(self.module.getParameterAsString("Xcoord"))
        self.ui.le_CoordY.setText(self.module.getParameterAsString("Ycoord"))
        QtCore.QObject.connect(self.ui.pb_preview, QtCore.SIGNAL("released()"), self.preview)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_values)
        QtCore.QObject.connect(self.ui.pb_r, QtCore.SIGNAL("released()"), self.load)
        QtCore.QObject.connect(self.ui.pb_csv, QtCore.SIGNAL("released()"), self.loadcsv)
        QtCore.QObject.connect(self.ui.pb_ET, QtCore.SIGNAL("released()"), self.loadET)
        
    def preview(self):
        vec = []
        dic = {}
        filename = str(self.ui.le_r.text())
        if (filename != ""):
            a = netCDF4.Dataset(filename,'r',format='NETCDF4')
            units = a.variables['precipitation'].units
            a.close()
        else:
            units = "mm/6min"
        if(self.module.UserCsv == "csv"):
            f = open(self.module.csvFile,"r")
        else:
            f = open("RainData.csv","r")
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
        self.module.setParameterValue("Xcoord",str(self.ui.le_CoordX.text()))
        self.module.setParameterValue("Ycoord",str(self.ui.le_CoordY.text()))
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

    def load(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, "Open Rain File", "Open new file", self.tr("Rain Files (*.nc)"))
        self.ui.le_r.setText(filename)
    def loadcsv(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, "Open Rain File", "Open new file", self.tr("CSV Files (*.csv)"))
        self.ui.le_csv.setText(filename)
    def loadET(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, "Open ET File", "Open new file", self.tr("Text Files (*.txt)"))
        self.ui.le_ET.setText(filename)