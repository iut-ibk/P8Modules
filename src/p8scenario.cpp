#include "p8scenario.h"
#include "p8scenario_gui.h"
#include "dmsimulation.h"
#include "dmporttuple.h"
#include "sstream"

#include "dmsystem.h"
#include "dmview.h"

#include <cmath>

DM_DECLARE_GROUP_NAME(SCENARIO, CRCP8)


SCENARIO::SCENARIO()
{
    cout << "1=====================" << endl;

    this->Steps = 1;
    modulesHaveBeenCreated = false;

    this->addParameter("ModulesCreated", DM::BOOL, & modulesHaveBeenCreated);
}

void SCENARIO::run()
{
    Group::run();
}

void SCENARIO::init() {
    this->addTuplePort("out", DM::OUTTUPLESYSTEM);
    this->addTuplePort("in", DM::INTUPLESYSTEM);

    if (!modulesHaveBeenCreated)
    {
 //new serialized version
        //created by netread
        cout << "2=====================" << endl;
        DM::Module *blocDelin;
        blocDelin=this->getSimulation()->addModule("delinblocks");
        blocDelin->setGroup(this);
        blocDelin->setName("blocDelin");
        blocDelin->init();
        //mmap.insert("blocDelin",QString::fromStdString(blocDelin->getUuid()));

        DM::Module *basinDelin;
        basinDelin=this->getSimulation()->addModule("delinbasin");
        basinDelin->setGroup(this);
        basinDelin->init();
        //mmap.insert("basinDelin",QString::fromStdString(basinDelin->getUuid()));

        DM::Module *planbbUrban;
        planbbUrban=this->getSimulation()->addModule("urbplanbb");
        planbbUrban->setGroup(this);
        planbbUrban->setName("planbbUrban");
        planbbUrban->init();
        //mmap.insert("planbbUrban",QString::fromStdString(planbbUrban->getUuid()));

       DM::Module *urbplanResidential;
        urbplanResidential=this->getSimulation()->addModule("ubp_residential");
        urbplanResidential->setGroup(this);
        urbplanResidential->init();
       // mmap.insert("urbplanResidential",QString::fromStdString(urbplanResidential->getUuid()));

        cout << "3=====================" << endl;
         DM::Module *urbplanNonResidential;
        urbplanNonResidential=this->getSimulation()->addModule("ubp_nonres");
        urbplanNonResidential->setGroup(this);
        urbplanNonResidential->init();
        //mmap.insert("urbplanNonResidential",QString::fromStdString(urbplanNonResidential->getUuid()));

        DM::Module *urbplanFacilities;
        urbplanFacilities=this->getSimulation()->addModule("ubp_facilities");
        urbplanFacilities->setGroup(this);
        urbplanFacilities->init();
        //mmap.insert("urbplanFacilities",QString::fromStdString(urbplanFacilities->getUuid()));

        DM::Module *urbplanSpaces;
        urbplanSpaces=this->getSimulation()->addModule("ubp_spaces");
        urbplanSpaces->setGroup(this);
        urbplanSpaces->init();
        //mmap.insert("urbplanSpaces",QString::fromStdString(urbplanSpaces->getUuid()));
        cout << "4=====================" << endl;

        DM::Module *planSummaryUrban;
        planSummaryUrban=this->getSimulation()->addModule("urbplansummary");
        planSummaryUrban->setGroup(this);
        planSummaryUrban->init();
        //mmap.insert("planSummaryUrban",QString::fromStdString(planSummaryUrban->getUuid()));


        DM::Module *placementTech;
        placementTech=this->getSimulation()->addModule("techplacement");
        placementTech->setGroup(this);
        placementTech->setName("placementTech");
        placementTech->init();
        //mmap.insert("placementTech",QString::fromStdString(placementTech->getUuid()));

        DM::Module *lotTechOpp;
        lotTechOpp=this->getSimulation()->addModule("techopp_lot");
        lotTechOpp->setGroup(this);
        lotTechOpp->init();
        //mmap.insert("lotTechOpp",QString::fromStdString(lotTechOpp->getUuid()));

        DM::Module *streetTechOpp;
        streetTechOpp=this->getSimulation()->addModule("techopp_street");
        streetTechOpp->setGroup(this);
        streetTechOpp->init();
        //mmap.insert("streetTechOpp",QString::fromStdString(streetTechOpp->getUuid()));

        DM::Module *neighTechOpp;
        neighTechOpp=this->getSimulation()->addModule("techopp_neigh");
        neighTechOpp->setGroup(this);
        neighTechOpp->init();
        //mmap.insert("neighTechOpp",QString::fromStdString(neighTechOpp->getUuid()));
        cout << "4b====================" << endl;

        DM::Module *precTechOpp;
        precTechOpp=this->getSimulation()->addModule("techopp_precinct");
        precTechOpp->setGroup(this);
        precTechOpp->init();
       // mmap.insert("precTechOpp",QString::fromStdString(precTechOpp->getUuid()));

        DM::Module *evalTechStrategy;
        evalTechStrategy=this->getSimulation()->addModule("techstrategy_eval");
        evalTechStrategy->setGroup(this);
        evalTechStrategy->init();
        //mmap.insert("evalTechStrategy",QString::fromStdString(evalTechStrategy->getUuid()));
        cout << "5=====================" << endl;

        DM::ModuleLink *l_START_blocDelin=this->getSimulation()->addLink( this->getInPortTuple("in")->getOutPort(),blocDelin->getInPort("City"));
        DM::ModuleLink *l_blocDelin_basinDelin=this->getSimulation()->addLink( blocDelin->getOutPort("City"),basinDelin->getInPort("City"));
        DM::ModuleLink *l_basinDelin_planbbUrban=this->getSimulation()->addLink( basinDelin->getOutPort("City"),planbbUrban->getInPort("City"));
        DM::ModuleLink *l_planbbUrban_urbplanResidential=this->getSimulation()->addLink( planbbUrban->getOutPort("City"),urbplanResidential->getInPort("City"));
        DM::ModuleLink *l_urbplanResidential_urbplanNonResidential=this->getSimulation()->addLink( urbplanResidential->getOutPort("City"),urbplanNonResidential->getInPort("City"));
        DM::ModuleLink *l_urbplanNonResidential_urbplanFacilities=this->getSimulation()->addLink( urbplanNonResidential->getOutPort("City"),urbplanFacilities->getInPort("City"));
        DM::ModuleLink *l_urbplanFacilities_urbplanSpaces=this->getSimulation()->addLink( urbplanFacilities->getOutPort("City"),urbplanSpaces->getInPort("City"));
        DM::ModuleLink *l_urbplanSpaces_planSummaryUrban=this->getSimulation()->addLink( urbplanSpaces->getOutPort("City"),planSummaryUrban->getInPort("City"));

        DM::ModuleLink *l_planSummaryUrban_placementTech=this->getSimulation()->addLink( planSummaryUrban->getOutPort("City"),placementTech->getInPort("City"));
        DM::ModuleLink *l_placementTech_lotTechOpp=this->getSimulation()->addLink( placementTech->getOutPort("City"),lotTechOpp->getInPort("City"));
        DM::ModuleLink *l_lotTechOpp_streetTechOpp=this->getSimulation()->addLink( lotTechOpp->getOutPort("City"),streetTechOpp->getInPort("City"));
        DM::ModuleLink *l_streetTechOpp_neighTechOpp=this->getSimulation()->addLink( streetTechOpp->getOutPort("City"),neighTechOpp->getInPort("City"));
        DM::ModuleLink *l_neighTechOpp_precTechOpp=this->getSimulation()->addLink( neighTechOpp->getOutPort("City"),precTechOpp->getInPort("City"));
        DM::ModuleLink *l_precTechOpp_evalTechStrategy=this->getSimulation()->addLink( precTechOpp->getOutPort("City"),evalTechStrategy->getInPort("City"));
        DM::ModuleLink * l_evalTechStrategy_END=this->getSimulation()->addLink( evalTechStrategy->getOutPort("City"),this->getOutPortTuple("out")->getInPort());
        // end created by netread

        modulesHaveBeenCreated = true;
        cout << "6=====================" << endl;

    }
}

void SCENARIO::open_ui_delinblocks()
{
    DM::Module *bd;
    bd=this->getSimulation()->getModuleByName("blocDelin");
    bd->createInputDialog();
}
void SCENARIO::open_ui_urbplanbb()
{
    DM::Module *bd;
    bd=this->getSimulation()->getModuleByName("planbbUrban");
    bd->createInputDialog();
}
void SCENARIO::open_ui_techplacement()
{
    DM::Module *bd;
    bd=this->getSimulation()->getModuleByName("placementTech");
    bd->createInputDialog();
}

bool SCENARIO::createInputDialog() {
    QWidget * w = new SCENARIO_GUI(this);
    w->show();
    return true;
}
