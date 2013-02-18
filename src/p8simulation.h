#ifndef P8SIMULATION_H
#define P8SIMULATION_H

#include "dmcompilersettings.h"
#include <dmgroup.h>
#include <iostream>
#include <QMap>
#include <QString>

class DM_HELPER_DLL_EXPORT P8Simulation :public DM::Group
{
    DM_DECLARE_GROUP(P8Simulation)
public:

    P8Simulation();
    void run();
    virtual bool createInputDialog();
    void init();
    void open_ui_delinblocks();
    void open_ui_urbplanbb();
    void open_ui_techplacement();
    QMap<QString,QString> mmap;
};

#endif // P8BASELINE_H
