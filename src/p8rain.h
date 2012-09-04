#ifndef P8RAIN_H
#define P8RAIN_H

#include "dmcompilersettings.h"
#include <dmgroup.h>
#include <iostream>
#include <QMap>
#include <QString>

class DM_HELPER_DLL_EXPORT P8Rain :public DM::Group
{
    DM_DECLARE_GROUP(P8Rain)
public:
    P8Rain();
    void run();
    virtual bool createInputDialog();
    void createRain(QString filename, QString name, QString typ );
    void init();
    QMap<QString,QString> mmap;

    std::string fileNameR;
};

#endif // P8RAIN_H
