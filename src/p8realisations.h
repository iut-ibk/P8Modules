
#ifndef P8REALISATIONS_H
#define P8REALISATIONS_H

#include <dmmodule.h>
#include <dm.h>


class DM_HELPER_DLL_EXPORT Realisations : public DM::Module
{
    DM_DECLARE_NODE(Realisations)
private:
    DM::View Simu;
    DM::View Block;

public:
    Realisations();
    void run();
    void init();
    virtual bool createInputDialog();
    std::string RealisationNr;

};

#endif // P8REALISATIONS_H

