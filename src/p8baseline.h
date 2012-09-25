#ifndef P8BASELINE_H
#define P8BASELINE_H

#include "dmcompilersettings.h"
#include <dmgroup.h>
#include <iostream>
#include <QMap>
#include <QString>

class DM_HELPER_DLL_EXPORT URBAN_FORM :public DM::Group
{
    DM_DECLARE_GROUP(URBAN_FORM)
public:
    URBAN_FORM();
    void run();
    virtual bool createInputDialog();
    void createShape(QString filename, QString name, QString typ );
    void createRaster(QString filename, QString name);
    void init();

    //QMap<QString,QString> mmap;

    std::string fileNameC;
    std::string fileNameS;
    std::string fileNameT;
    std::string fileNameP;
    std::string fileNameD;
    std::string fileNameL;
    double rasterSize;
};

#endif // P8BASELINE_H
