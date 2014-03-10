
#ifndef P8REALISATIONS2_H
#define P8REALISATIONS2_H

#include <dmmodule.h>
#include <dm.h>


class DM_HELPER_DLL_EXPORT Current_RealisationModule: public DM::Module
{
    DM_DECLARE_NODE(Current_RealisationModule)
private:
    DM::View Simu;
    DM::View MapAttr;

public:
    Current_RealisationModule();
    void run();
    void init();
    virtual bool createInputDialog();
    std::string RealisationNr;

};

#endif // P8REALISATIONS_H

