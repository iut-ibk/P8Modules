
#include "p8realisations.h"
#include "p8realisation_gui.h"

#include <QWidget>

DM_DECLARE_NODE_NAME(Current_Realisation, )

Current_Realisation::Current_Realisation()
{
    RealisationNr = "";
    this->addParameter("RealisationNr",DM::STRING,&this->RealisationNr);
}

void Current_Realisation::init()
{
    Block = DM::View("Block",DM::FACE,DM::READ);

    Simu = DM::View("SimulationData",DM::COMPONENT,DM::WRITE);
    Simu.addAttribute("MusicFileNo");
    std::vector<DM::View> vdata;
    vdata.push_back(Simu);
    vdata.push_back(Block);
    this->addData("City",vdata);
}

void Current_Realisation::run()
{
    DM::System * sys = this->getData("City");
    DM::Component * cmp = new DM::Component();
    sys->addComponent(cmp,Simu);

    cmp->addAttribute("MusicFileNo",atoi(this->RealisationNr.c_str()));
}

bool Current_Realisation::createInputDialog()
{
    QWidget * w = new p8realisation_gui(this);
    w->show();
    return true;
}


