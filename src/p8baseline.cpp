#include "p8baseline.h"
#include "p8baseline_gui.h"
#include "dmsimulation.h"
#include "dmporttuple.h"
#include "sstream"
DM_DECLARE_GROUP_NAME(P8BaseLine, CRCP8)


P8BaseLine::P8BaseLine()
{
    this->Steps = 1;

    mux = NULL;}

void P8BaseLine::run() {

    Group::run();
}

void P8BaseLine::init() {
    this->addTuplePort("out", DM::OUTTUPLESYSTEM);
    if (mux==NULL)
    {
        mux=this->getSimulation()->addModule("AppendViewFromSystem");
        mux->setGroup(this);
        mux->init();
        this->getSimulation()->addLink( mux->getOutPort("Combined"),this->getOutPortTuple("out")->getInPort());
    }
}

bool P8BaseLine::createInputDialog() {
    QWidget * w = new P8BaseLine_GUI(this);
    w->show();
    return true;
}

void P8BaseLine::createShape(string name)
{
    DM::Module * m = this->getSimulation()->addModule("ImportShapeFile");
    m->setGroup(this);
    m->setParameterValue("FileName", name);
    DM::Logger(DM::Debug) << name;
    m->setParameterValue("Identifier", "Landuse");
    m->setParameterValue("isEdge", "1");
    m->init();


    //    this->getSimulation()->addLink(m->getOutPort("Vec"), this->getOutPortTuple("out")->getInPort());
    std::string inports = mux->getParameterAsString("Inports");
    std::stringstream ss(inports);
    ss << "*|*" << "Landuse";
    mux->setParameterValue("Inports",ss.str());
    mux->init();
    this->getSimulation()->addLink(m->getOutPort("Vec"), mux->getInPort("Landuse"));

}
