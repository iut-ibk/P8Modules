#include "p8realisations.h"

DM_DECLARE_NODE_NAME(Realisations,P8Modules)

Realisations::Realisations()
{
    RealisationNr = "";
    this->addParameter("RealisationNr",DM::STRING,&this->RealisationNr);
}

void Realisations::init()
{
    this->addPort("in",DM::INPORTS);
    this->addPort("out",DM::OUTPORTS);


    Simu = DM::View("SimulationData",DM::COMPONENT,DM::WRITE);
    Simu.addAttribute("MusicFileNo");
    std::vector<DM::View> vdata;
    vdata.push_back(Simu);
    this->addData("City",vdata);
}

void Realisations::run()
{

}

bool Realisations::createInputDialog()
{
    return true;
}
