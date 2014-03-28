#include "p8baseline.h"
#include "p8baseline_gui.h"
#include "dmsimulation.h"
#include "dmporttuple.h"
#include "sstream"
#include "QSettings"
#include <cmath>

DM_DECLARE_GROUP_NAME(URBAN_FORM, CRCP8)


URBAN_FORM::URBAN_FORM()
{
    this->Steps = 1;
    fileNameC = "";
    fileNameS = "";
    fileNameT = "";
    fileNameP = "";
    fileNameD = "";
    fileNameL = "";

    rasterSize=200;
    this->addParameter("FileNameC", DM::STRING, &this->fileNameC);
    this->addParameter("FileNameS", DM::STRING, &this->fileNameS);
    this->addParameter("FileNameT", DM::STRING, &this->fileNameT);
    this->addParameter("FileNameP", DM::STRING, &this->fileNameP);
    this->addParameter("FileNameD", DM::STRING, &this->fileNameD);
    this->addParameter("FileNameL", DM::STRING, &this->fileNameL);
    this->addParameter("RasterSize", DM::DOUBLE, &this->rasterSize);
    this->setName("URBAN_FORM");
}

void URBAN_FORM::run()
{
    Group::run();
}

void URBAN_FORM::init()
{
    QSettings settings;
    QString installDir = settings.value("installPath").toString();
    this->addTuplePort("out", DM::OUTTUPLESYSTEM);
    if (this->getSimulation()->getModuleByName("Mixer")==NULL)
    {
        cout << "Creating Mixer"<<endl;
        DM::Module *mix;
        mix=this->getSimulation()->addModule("AppendViewFromSystem");
        mix->setGroup(this);
        mix->init();
        mix->setName("Mixer");
        cout << "created: " << mix << "("<< mix->getUuid()<< ")"<<endl;

        cout << "Createing Links"<<endl;
        DM::ModuleLink * l1=this->getSimulation()->addLink( mix->getOutPort("Combined"),this->getOutPortTuple("out")->getInPort());
        cout << "created"<<endl;

        //making and linking default rasters

        createRaster(installDir+"/elevation.txt",QString("Employment"));
        createRaster(installDir+"/elevation.txt",QString("Groundwater"));
        createRaster(installDir+"/elevation.txt",QString("SocialParam1"));
        createRaster(installDir+"/elevation.txt",QString("SocialParam2"));

    }
}

bool URBAN_FORM::createInputDialog()
{
    QWidget * w = new URBAN_FORM_GUI(this);
    w->show();
    return true;
}


void URBAN_FORM::createShape(QString filename, QString name, QString typ )
{
    if(this->getSimulation()->getModuleByName(name.toStdString())!=0)
        return;
    DM::Module *m = this->getSimulation()->addModule("ImportShapeFile");
    if (m!=NULL)
    {
        //        DM::Logger(DM::Debug) << "1";
//        mmap.insert(name,QString::fromStdString(m->getUuid()));
        m->setGroup(this);
        m->setParameterValue("FileName", filename.toStdString());
        DM::Logger(DM::Debug) << filename;
        m->setParameterValue("Identifier", "SUPERBLOCK");    //);name.toStdString()); //"Landuse"
        m->setParameterValue(typ.toStdString(), "1"); //"isEdge"
        m->setName(name.toStdString()); //"Landuse"
        m->init();
        DM::Module *mix=this->getSimulation()->getModuleByName("Mixer");
        QString inports = QString::fromStdString(mix->getParameterAsString("Inports"));
        inports += "*|*" + name;
        mix->setParameterValue("Inports",inports.toStdString());
        mix->init();
        this->getSimulation()->addLink(m->getOutPort("Vec"), mix->getInPort(name.toStdString()));
    }
}

void URBAN_FORM::createRaster(QString filename, QString name)
{
    if(this->getSimulation()->getModuleByName(name.toStdString())!=0)
        return;
    DM::Module * m = this->getSimulation()->addModule("ImportRasterData2");
    cout << "Raster: " << m << endl;
    if (m!=NULL)
    {
//        mmap.insert(name,QString::fromStdString(m->getUuid()));
        m->setGroup(this);
        m->setParameterValue("Filename", filename.toStdString());
        DM::Logger(DM::Debug) << filename;
        m->setParameterValue("DataName", name.toStdString()); //"Landuse"
        m->setName(name.toStdString()); //"Landuse"
        m->init();

        DM::Module *mix=this->getSimulation()->getModuleByName("Mixer");
        QString inports = QString::fromStdString(mix->getParameterAsString("Inports"));
        inports += "*|*" + name;
        mix->setParameterValue("Inports",inports.toStdString());
        mix->init();
        DM::ModuleLink * l = this->getSimulation()->addLink(m->getOutPort("Data"), mix->getInPort(name.toStdString()));
    }
}
