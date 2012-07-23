#ifndef APPENDRASTERASATTRIBUTE_H
#define APPENDRASTERASATTRIBUTE_H


#include "dmcompilersettings.h"
#include <dmgroup.h>
#include <dmmodule.h>

class DM_HELPER_DLL_EXPORT AppendRasterAsAttribute : public  DM::Module {
    DM_DECLARE_NODE(P8ScenarioGroup)

    private:
        DM::System * sys_in;
    std::string NameOfExistingView;
    std::string newAttribute;
    std::string newAttribute_old;
    std::vector<DM::View> data;

    std::vector<std::string> nameOfRasterData;

    DM::View readView;

    DM::View superblock;

    std::map<std::string, DM::RasterData*> attribueMaps;


    bool median;

public:
    AppendRasterAsAttribute();
    void run();
    void init();
    bool createInputDialog();
    DM::System * getSystemIn(){return this->sys_in;}
};



#endif // APPENDRASTERASATTRIBUTE_H
