#ifndef P8SCENARIOGROUP_H
#define P8SCENARIOGROUP_H

#include "dmcompilersettings.h"
#include <dmgroup.h>


class DM_HELPER_DLL_EXPORT P8ScenarioGroup :public DM::Group
{
    DM_DECLARE_GROUP(P8ScenarioGroup)
public:
    P8ScenarioGroup();
    void run();

};

#endif // P8SCENARIOGROUP_H
