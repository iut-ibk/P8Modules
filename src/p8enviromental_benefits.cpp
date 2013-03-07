#include "p8enviromental_benefits.h"
#include "dmsimulation.h"
#include "dmporttuple.h"
#include "sstream"

#include "dmsystem.h"
#include "dmview.h"

#include <cmath>

DM_DECLARE_GROUP_NAME(Enviromental_Benefits, P8Modules)


Enviromental_Benefits::Enviromental_Benefits()
{
    this->Steps = 1;
    modulesHaveBeenCreated = false;

    this->addParameter("ModulesCreated", DM::BOOL, & modulesHaveBeenCreated);
}

void Enviromental_Benefits::run()
{
    Group::run();
}

void Enviromental_Benefits::init()
{
    this->addTuplePort("out", DM::OUTTUPLESYSTEM);
    this->addTuplePort("in", DM::INTUPLESYSTEM);
    if (!modulesHaveBeenCreated)
    {

        DM::Module *musicWrite2;
        musicWrite2=this->getSimulation()->addModule("WriteResults2MUSICsecondary");
        musicWrite2->setGroup(this);
        musicWrite2->init();

        DM::Module *tableRead2;
        tableRead2=this->getSimulation()->addModule("EnviromentalBenefitsResults");
        tableRead2->setGroup(this);
        tableRead2->setName("tableRead2");
        tableRead2->init();


        DM::ModuleLink *l_START_musicWrite=this->getSimulation()->addLink( this->getInPortTuple("in")->getOutPort(),musicWrite2->getInPort("City"));
        DM::ModuleLink *l_musicWrite_tableRead=this->getSimulation()->addLink( musicWrite2->getOutPort("City"),tableRead2->getInPort("City"));
        DM::ModuleLink * l_tableRead_END=this->getSimulation()->addLink( tableRead2->getOutPort("City"),this->getOutPortTuple("out")->getInPort());

        modulesHaveBeenCreated = true;
    }

}
bool Enviromental_Benefits::createInputDialog() {
    DM::Module *bd;
    bd=this->getSimulation()->getModuleByName("tableRead2");
    bd->createInputDialog();
    return true;
}
