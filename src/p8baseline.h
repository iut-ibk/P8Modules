#ifndef P8BASELINE_H
#define P8BASELINE_H

#include "dmcompilersettings.h"
#include <dmgroup.h>
#include <iostream>
#include <QMap>
#include <QString>

class DM_HELPER_DLL_EXPORT P8BaseLine :public DM::Group
{
    DM_DECLARE_GROUP(P8BaseLine)
public:
    P8BaseLine();
    void run();
    virtual bool createInputDialog();
    void createShape(QString filename, QString name, QString typ );
    void createRaster(QString filename, QString name);
    void init();
//    void initSCB(double w, double h);
    void createCityBlocksFromShape(double width, double height);
    QMap<QString,QString> mmap;

    std::string fileNameC;
    std::string fileNameE;
    std::string fileNameS;
    std::string fileNameP;
    std::string fileNameL;
};

#endif // P8BASELINE_H
