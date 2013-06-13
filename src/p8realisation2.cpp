#include "p8realisation2.h"
#include "p8realisation2_gui.h"

#include <QWidget>

DM_DECLARE_NODE_NAME(Current_Realisation2,P8Modules)

Current_Realisation2::Current_Realisation2()
{
    RealisationNr = "";
    this->addParameter("RealisationNr",DM::STRING,&this->RealisationNr);
}

void Current_Realisation2::init()
{

    Simu = DM::View("SimulationData",DM::COMPONENT,DM::WRITE);
    Simu.addAttribute("MusicFileNo");
    std::vector<DM::View> vdata;
    vdata.push_back(Simu);
    this->addData("City",vdata);
}
void Current_Realisation2::run()
{
    DM::System * sys = this->getData("City");
    DM::Component * cmp = new DM::Component();
    sys->addComponent(cmp,Simu);

    cmp->addAttribute("MusicFileNo",atoi(this->RealisationNr.c_str()));
}
bool Current_Realisation2::createInputDialog()
{
    QWidget * w = new p8realisation2_gui(this);
    w->show();
    return true;
}
