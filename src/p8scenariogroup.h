#ifndef P8SCENARIOGROUP_H
#define P8SCENARIOGROUP_H

#include "dmcompilersettings.h"
#include <dmgroup.h>
#include <dmmodule.h>

class DM_HELPER_DLL_EXPORT P8ScenarioGroup : public  DM::Module {
    DM_DECLARE_NODE(P8ScenarioGroup)

    private:
        DM::System * sys_in;
    std::string NameOfExistingView;
    std::string newAttribute;
    std::string newAttribute_old;
    std::string NameOfRasterData;
    std::vector<DM::View> data;

    DM::View readView;

    std::map<std::string, DM::RasterData*> attribueMaps;


    bool median;
    double multiplier;

public:
    P8ScenarioGroup();
    void run();
    void init();
    bool createInputDialog();
    DM::System * getSystemIn(){return this->sys_in;}
};

#endif // P8ScenarioGroup_H
