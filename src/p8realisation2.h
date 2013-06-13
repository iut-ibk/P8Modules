
#ifndef P8REALISATIONS2_H
#define P8REALISATIONS2_H

#include <dmmodule.h>
#include <dm.h>


class DM_HELPER_DLL_EXPORT Current_Realisation2 : public DM::Module
{
    DM_DECLARE_NODE(Current_Realisation2)
private:
    DM::View Simu;

public:
    Current_Realisation2();
    void run();
    void init();
    virtual bool createInputDialog();
    std::string RealisationNr;

};

#endif // P8REALISATIONS_H

