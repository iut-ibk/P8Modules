#include "p8realisation2.h"
#include "p8realisation2_gui.h"

#include <QWidget>

DM_DECLARE_NODE_NAME(Current_RealisationModule,P8Modules)

Current_RealisationModule::Current_RealisationModule()
{
    RealisationNr = "";
    this->addParameter("RealisationNr",DM::STRING,&this->RealisationNr);
}

void Current_RealisationModule::init()
{

    Simu = DM::View("SimulationData",DM::COMPONENT,DM::WRITE);
    Simu.addAttribute("MusicFileNo");
    std::vector<DM::View> vdata;
    vdata.push_back(Simu);
    this->addData("City",vdata);
}
void Current_RealisationModule::run()
{
    DM::System * sys = this->getData("City");
    DM::Component * cmp = new DM::Component();
    sys->addComponent(cmp,Simu);

    cmp->addAttribute("MusicFileNo",atoi(this->RealisationNr.c_str()));
}
bool Current_RealisationModule::createInputDialog()
{
    QWidget * w = new p8realisationModule_gui(this);
    w->show();
    return true;
}
