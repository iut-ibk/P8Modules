#include "p8scenario.h"
#include "p8scenario_gui.h"
#include "dmsimulation.h"
#include "dmporttuple.h"
#include "sstream"
#include "QSettings"
#include "dmsystem.h"
#include "dmview.h"

#include <cmath>

//DM_DECLARE_GROUP_NAME(SCENARIO, CRCP8)
DM_DECLARE_CUSTOM_GROUP_NAME(SCENARIO,"Scenario Setup","Scenario Generation")

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
    QSettings settings;
    string installDir = settings.value("installPath").toString().toStdString();
    this->addTuplePort("out", DM::OUTTUPLESYSTEM);
    this->addTuplePort("in", DM::INTUPLESYSTEM);

    if (!modulesHaveBeenCreated)
    {

        DM::Module *blocDelin;
        blocDelin=this->getSimulation()->addModule("Spatial Delineation of Building Blocks");
        blocDelin->setGroup(this);
        blocDelin->setName("blocDelin");
        blocDelin->init();
        cout << "2=====================" << endl;

        DM::Module *getPrevBlock;
        getPrevBlock=this->getSimulation()->addModule("GetPreviousBlocks");
        getPrevBlock->setGroup(this);
        getPrevBlock->setParameterValue("block_path_name",installDir + "/emptyblockmap.shp");
        getPrevBlock->setParameterValue("patch_path_name",installDir + "/emptyblockmap.shp");
        getPrevBlock->init();

        DM::Module *mix1=this->getSimulation()->addModule("AppendViewFromSystem");
        mix1->setGroup(this);
        QString inports1 = QString::fromStdString(mix1->getParameterAsString("Inports"));
        inports1 += "*|*" + QString("Spatial Delineation of Building Blocks") + "*|*" + "GetPreviousBlocks";
        mix1->setParameterValue("Inports",inports1.toStdString());
        mix1->init();

        DM::Module *planbbUrban;
        planbbUrban=this->getSimulation()->addModule("Urban Planning Customization");
        planbbUrban->setGroup(this);
        planbbUrban->setName("planbbUrban");
        planbbUrban->init();

        DM::Module *getPrevSys;
        getPrevSys=this->getSimulation()->addModule("GetSystems");
        getPrevSys->setGroup(this);
        getPrevSys->setParameterValue("path_name",installDir + "/emptysystemsmap.shp");
        getPrevSys->init();

        DM::Module *mix2=this->getSimulation()->addModule("AppendViewFromSystem");
        mix2->setGroup(this);
        QString inports2 = QString::fromStdString(mix2->getParameterAsString("Inports"));
        inports2 += "*|*" + QString("Urban Planning Customization") + "*|*" + "GetSystems";
        mix2->setParameterValue("Inports",inports2.toStdString());
        mix2->init();

        DM::Module *placementTech;
        placementTech=this->getSimulation()->addModule("Decentralised Technology Design and Implementation");
        placementTech->setGroup(this);
        placementTech->setName("placementTech");
        placementTech->init();


        DM::Module *writeMusic;
        writeMusic=this->getSimulation()->addModule("WriteResults2MUSIC");
        writeMusic->setGroup(this);
        writeMusic->init();
        cout << "5=====================" << endl;






        DM::ModuleLink *l_START_blocDelin=this->getSimulation()->addLink( this->getInPortTuple("in")->getOutPort(),blocDelin->getInPort("City"));
        DM::ModuleLink *l_blocDelin_mix1 = this->getSimulation()->addLink(blocDelin->getOutPort("City"), mix1->getInPort("Delinblocks"));
        DM::ModuleLink *l_getblock_mix1 = this->getSimulation()->addLink(getPrevBlock->getOutPort("City"), mix1->getInPort("GetPreviousBlocks"));
        DM::ModuleLink *l_mix1_plannurb = this->getSimulation()->addLink(mix1->getOutPort("Combined"), planbbUrban->getInPort("City"));
        DM::ModuleLink *l_plannurb_mix2 = this->getSimulation()->addLink(planbbUrban->getOutPort("City"), mix2->getInPort("Urbplanbb"));
        DM::ModuleLink *l_getsys_mix2 = this->getSimulation()->addLink(getPrevSys->getOutPort("City"), mix2->getInPort("GetSystems"));
        DM::ModuleLink *l_mix2_techplace = this->getSimulation()->addLink(mix2->getOutPort("Combined"), placementTech->getInPort("City"));
        DM::ModuleLink *l_placement_WriteMusic = this->getSimulation()->addLink(placementTech->getOutPort("City"), writeMusic->getInPort("City"));
        DM::ModuleLink * l_WriteMusic_END=this->getSimulation()->addLink(writeMusic->getOutPort("City"),this->getOutPortTuple("out")->getInPort());


        /*
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
*/
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
