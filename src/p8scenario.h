#ifndef P8SCENARIO_H
#define P8SCENARIO_H

#include "dmcompilersettings.h"
#include <dmgroup.h>
#include <iostream>
#include <QMap>
#include <QString>

class DM_HELPER_DLL_EXPORT P8Scenario :public DM::Group
{
    DM_DECLARE_GROUP(P8Scenario)
public:

    P8Scenario();
    void run();
    virtual bool createInputDialog();
    void init();
    void open_ui_delinblocks();
    void open_ui_urbplanbb();
    void open_ui_techplacement();
    QMap<QString,QString> mmap;
};

#endif // P8BASELINE_H
