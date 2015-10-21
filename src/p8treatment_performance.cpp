#include "p8treatment_performance.h"
#include "dmsimulation.h"
#include "dmporttuple.h"
#include "sstream"

#include "dmsystem.h"
#include "dmview.h"

#include <cmath>

DM_DECLARE_GROUP_NAME(Treatment_Performance, )


Treatment_Performance::Treatment_Performance()
{

    this->Steps = 1;
    modulesHaveBeenCreated = false;

    this->addParameter("ModulesCreated", DM::BOOL, & modulesHaveBeenCreated);

}

void Treatment_Performance::run()
{
    Group::run();
}

void Treatment_Performance::init()
{
    this->addTuplePort("out", DM::OUTTUPLESYSTEM);
    this->addTuplePort("in", DM::INTUPLESYSTEM);
    if (!modulesHaveBeenCreated)
    {
        DM::Module *musicWrite;
        musicWrite=this->getSimulation()->addModule("TreatmentPerformance");
        musicWrite->setGroup(this);
        musicWrite->init();

        DM::Module *tableRead;
        tableRead=this->getSimulation()->addModule("TreatmentPerformanceResults");
        tableRead->setGroup(this);
        tableRead->setName("tableRead");
        tableRead->init();


        DM::ModuleLink *l_START_musicWrite=this->getSimulation()->addLink( this->getInPortTuple("in")->getOutPort(),musicWrite->getInPort("City"));
        DM::ModuleLink *l_musicWrite_tableRead=this->getSimulation()->addLink( musicWrite->getOutPort("City"),tableRead->getInPort("City"));
        DM::ModuleLink * l_tableRead_END=this->getSimulation()->addLink( tableRead->getOutPort("City"),this->getOutPortTuple("out")->getInPort());

        modulesHaveBeenCreated = true;
    }

}
bool Treatment_Performance::createInputDialog() {
    DM::Module *bd;
    bd=this->getSimulation()->getModuleByName("tableRead");
    bd->createInputDialog();
    return true;
}
