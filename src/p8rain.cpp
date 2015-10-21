#include "p8rain.h"
#include "p8rain_gui.h"
#include "dmsimulation.h"
#include "dmporttuple.h"
#include "sstream"

#include <cmath>

DM_DECLARE_GROUP_NAME(P8Rain, )


P8Rain::P8Rain()
{
    this->Steps = 1;
    fileNameR = "";
    this->addParameter("FileNameR", DM::STRING, &this->fileNameR);
}

void P8Rain::run() {

    Group::run();
    /*
    DM::Module *app=this->getSimulation()->getModuleWithUUID("Append");
    foreach (QString uuid, mmap.values())
    {
        DM::Module *rast=this->getSimulation()->getModuleWithUUID(uuid.toStdString());
        if (mod->getClassName()=="ImportRasterData")
        {
            QString rastName=rast->getName();
            ...
            app->setParameterValue();
            app->run();
        }
    }*/
}

void P8Rain::init() {
    this->addTuplePort("out", DM::OUTTUPLESYSTEM);

}




bool P8Rain::createInputDialog() {
    QWidget * w = new P8Rain_GUI(this);
    w->show();
    return true;
}


void P8Rain::createRain(QString filename, QString name, QString typ )
{
}
