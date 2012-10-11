#ifndef P8SCENARIO_H
#define P8SCENARIO_H

#include "dmcompilersettings.h"
#include <dmgroup.h>
#include <iostream>
#include <QMap>
#include <QString>

class DM_HELPER_DLL_EXPORT SCENARIO :public DM::Group
{
    DM_DECLARE_GROUP(SCENARIO)

    private:
        bool modulesHaveBeenCreated;
public:

    SCENARIO();
    void run();
    virtual bool createInputDialog();
    void init();
    void open_ui_delinblocks();
    void open_ui_urbplanbb();
    void open_ui_techplacement();
};

#endif // P8BASELINE_H
