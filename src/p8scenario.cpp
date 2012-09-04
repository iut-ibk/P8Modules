#include "p8scenario.h"
#include "p8scenario_gui.h"
#include "dmsimulation.h"
#include "dmporttuple.h"
#include "sstream"

#include <cmath>

DM_DECLARE_GROUP_NAME(P8Scenario, CRCP8)


P8Scenario::P8Scenario()
{
    this->Steps = 1;
}

void P8Scenario::run()
{
    Group::run();
}

void P8Scenario::init() {
    this->addTuplePort("out", DM::OUTTUPLESYSTEM);
    this->addTuplePort("in", DM::INTUPLESYSTEM);
    if (mmap.size()==0)
    {


        //created by netread

        DM::Module *blocDelin;
        blocDelin=this->getSimulation()->addModule("delinblocks");
        blocDelin->setGroup(this);
        blocDelin->init();
        mmap.insert("blocDelin",QString::fromStdString(blocDelin->getUuid()));

        DM::Module *basinDelin;
        basinDelin=this->getSimulation()->addModule("delinbasin");
        basinDelin->setGroup(this);
        basinDelin->init();
        mmap.insert("basinDelin",QString::fromStdString(basinDelin->getUuid()));

        DM::Module *planbbUrban;
        planbbUrban=this->getSimulation()->addModule("urbplanbb");
        planbbUrban->setGroup(this);
        planbbUrban->init();
        mmap.insert("planbbUrban",QString::fromStdString(planbbUrban->getUuid()));

        DM::Module *urbanplanResidential;
        urbanplanResidential=this->getSimulation()->addModule("ubp_residential");
        urbanplanResidential->setGroup(this);
        urbanplanResidential->init();
        mmap.insert("urbanplanResidential",QString::fromStdString(urbanplanResidential->getUuid()));

        DM::Module *urbanplanNonResidential;
        urbanplanNonResidential=this->getSimulation()->addModule("ubp_nonres");
        urbanplanNonResidential->setGroup(this);
        urbanplanNonResidential->init();
        mmap.insert("urbanplanNonResidential",QString::fromStdString(urbanplanNonResidential->getUuid()));

        DM::Module *urbanplanFacilities;
        urbanplanFacilities=this->getSimulation()->addModule("ubp_facilities");
        urbanplanFacilities->setGroup(this);
        urbanplanFacilities->init();
        mmap.insert("urbanplanFacilities",QString::fromStdString(urbanplanFacilities->getUuid()));

        DM::Module *urbanplanSpaces;
        urbanplanSpaces=this->getSimulation()->addModule("ubp_spaces");
        urbanplanSpaces->setGroup(this);
        urbanplanSpaces->init();
        mmap.insert("urbanplanSpaces",QString::fromStdString(urbanplanSpaces->getUuid()));

        DM::Module *mixer1;
        mixer1=this->getSimulation()->addModule("AppendViewFromSystem");
        mixer1->setGroup(this);
        mixer1->init();
        mmap.insert("mixer1",QString::fromStdString(mixer1->getUuid()));

        DM::Module *planSummaryUrban;
        planSummaryUrban=this->getSimulation()->addModule("urbanplansummary");
        planSummaryUrban->setGroup(this);
        planSummaryUrban->init();
        mmap.insert("planSummaryUrban",QString::fromStdString(planSummaryUrban->getUuid()));

        DM::Module *placementTech;
        placementTech=this->getSimulation()->addModule("techplacement");
        placementTech->setGroup(this);
        placementTech->init();
        mmap.insert("placementTech",QString::fromStdString(placementTech->getUuid()));

        DM::Module *lotTechOpp;
        lotTechOpp=this->getSimulation()->addModule("techopp_lot");
        lotTechOpp->setGroup(this);
        lotTechOpp->init();
        mmap.insert("lotTechOpp",QString::fromStdString(lotTechOpp->getUuid()));

        DM::Module *mixer2;
        mixer2=this->getSimulation()->addModule("AppendViewFromSystem");
        mixer2->setGroup(this);
        mixer2->init();
        mmap.insert("mixer2",QString::fromStdString(mixer2->getUuid()));

        DM::Module *evalTechStrategy;
        evalTechStrategy=this->getSimulation()->addModule("techstrategy_eval");
        evalTechStrategy->setGroup(this);
        evalTechStrategy->init();
        mmap.insert("evalTechStrategy",QString::fromStdString(evalTechStrategy->getUuid()));

        DM::Module *streetTechOpp;
        streetTechOpp=this->getSimulation()->addModule("techopp_street");
        streetTechOpp->setGroup(this);
        streetTechOpp->init();
        mmap.insert("streetTechOpp",QString::fromStdString(streetTechOpp->getUuid()));

        DM::Module *neighTechOpp;
        neighTechOpp=this->getSimulation()->addModule("techopp_neigh");
        neighTechOpp->setGroup(this);
        neighTechOpp->init();
        mmap.insert("neighTechOpp",QString::fromStdString(neighTechOpp->getUuid()));

        DM::Module *precTechOpp;
        precTechOpp=this->getSimulation()->addModule("techopp_prec");
        precTechOpp->setGroup(this);
        precTechOpp->init();
        mmap.insert("precTechOpp",QString::fromStdString(precTechOpp->getUuid()));

        DM::ModuleLink *l_START_blocDelin=this->getSimulation()->addLink( this->getInPortTuple("in")->getOutPort(),blocDelin->getInPort("City"));
        DM::ModuleLink *l_blocDelin_basinDelin=this->getSimulation()->addLink( blocDelin->getOutPort("City"),basinDelin->getInPort("City"));
        DM::ModuleLink *l_basinDelin_planbbUrban=this->getSimulation()->addLink( basinDelin->getOutPort("City"),planbbUrban->getInPort("City"));
        DM::ModuleLink *l_planbbUrban_urbanplanResidential=this->getSimulation()->addLink( planbbUrban->getOutPort("City"),urbanplanResidential->getInPort("City"));
        DM::ModuleLink *l_planbbUrban_urbanplanNonResidential=this->getSimulation()->addLink( planbbUrban->getOutPort("City"),urbanplanNonResidential->getInPort("City"));
        DM::ModuleLink *l_planbbUrban_urbanplanFacilities=this->getSimulation()->addLink( planbbUrban->getOutPort("City"),urbanplanFacilities->getInPort("City"));
        DM::ModuleLink *l_planbbUrban_urbanplanSpaces=this->getSimulation()->addLink( planbbUrban->getOutPort("City"),urbanplanSpaces->getInPort("City"));
        DM::ModuleLink *l_urbanplanResidential_mixer1=this->getSimulation()->addLink( urbanplanResidential->getOutPort("City"),mixer1->getInPort("City"));
        DM::ModuleLink *l_mixer1_planSummaryUrban=this->getSimulation()->addLink( mixer1->getOutPort("City"),planSummaryUrban->getInPort("City"));
        DM::ModuleLink *l_planSummaryUrban_placementTech=this->getSimulation()->addLink( planSummaryUrban->getOutPort("City"),placementTech->getInPort("City"));
        DM::ModuleLink *l_urbanplanNonResidential_mixer1=this->getSimulation()->addLink( urbanplanNonResidential->getOutPort("City"),mixer1->getInPort("City"));
        DM::ModuleLink *l_urbanplanFacilities_mixer1=this->getSimulation()->addLink( urbanplanFacilities->getOutPort("City"),mixer1->getInPort("City"));
        DM::ModuleLink *l_urbanplanSpaces_mixer1=this->getSimulation()->addLink( urbanplanSpaces->getOutPort("City"),mixer1->getInPort("City"));
        DM::ModuleLink *l_placementTech_lotTechOpp=this->getSimulation()->addLink( placementTech->getOutPort("City"),lotTechOpp->getInPort("City"));
        DM::ModuleLink *l_lotTechOpp_mixer2=this->getSimulation()->addLink( lotTechOpp->getOutPort("City"),mixer2->getInPort("City"));
        DM::ModuleLink *l_mixer2_evalTechStrategy=this->getSimulation()->addLink( mixer2->getOutPort("City"),evalTechStrategy->getInPort("City"));
        DM::ModuleLink *l_evalTechStrategy_END=this->getSimulation()->addLink( evalTechStrategy->getOutPort("City"),this->getOutPortTuple("out")->getInPort());
        DM::ModuleLink *l_placementTech_streetTechOpp=this->getSimulation()->addLink( placementTech->getOutPort("City"),streetTechOpp->getInPort("City"));
        DM::ModuleLink *l_streetTechOpp_mixer2=this->getSimulation()->addLink( streetTechOpp->getOutPort("City"),mixer2->getInPort("City"));
        DM::ModuleLink *l_placementTech_neighTechOpp=this->getSimulation()->addLink( placementTech->getOutPort("City"),neighTechOpp->getInPort("City"));
        DM::ModuleLink *l_neighTechOpp_mixer2=this->getSimulation()->addLink( neighTechOpp->getOutPort("City"),mixer2->getInPort("City"));
        DM::ModuleLink *l_placementTech_precTechOpp=this->getSimulation()->addLink( placementTech->getOutPort("City"),precTechOpp->getInPort("City"));
        DM::ModuleLink *l_precTechOpp_mixer2=this->getSimulation()->addLink( precTechOpp->getOutPort("City"),mixer2->getInPort("City"));
        // end created by netread

    }
}

void P8Scenario::open_ui_delimblocks()
{
    DM::Module *bd;
    bd=this->getSimulation()->getModuleWithUUID(mmap.value("blocDelin").toStdString());
//   bd->createInputDialog(); ????????????????
}

bool P8Scenario::createInputDialog() {
    QWidget * w = new P8Scenario_GUI(this);
    w->show();
    return true;
}
