#include "p8baseline.h"
#include "p8baseline_gui.h"
#include "dmsimulation.h"
#include "dmporttuple.h"
#include "sstream"

#include <cmath>

DM_DECLARE_GROUP_NAME(P8BaseLine, CRCP8)


P8BaseLine::P8BaseLine()
{
    this->Steps = 1;

}

void P8BaseLine::run() {

    Group::run();

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
    }
}

void P8BaseLine::init() {
    this->addTuplePort("out", DM::OUTTUPLESYSTEM);
    if (mmap.size()==0)
    {
        cout << "Createing Mixer"<<endl;
        DM::Module *mix;
        mix=this->getSimulation()->addModule("AppendViewFromSystem");
        mix->setGroup(this);
        mix->init();
        mmap.insert("Mixer",QString::fromStdString(mix->getUuid()));
        cout << "created: " << mix << "("<< mix->getUuid()<< ")"<<endl;

        cout << "Createing Append"<<endl;
        DM::Module *app;
        app=this->getSimulation()->addModule("AppendAttributes");
        app->setGroup(this);
        app->init();
        mmap.insert("Append",QString::fromStdString(app->getUuid()));
        cout << "created: " << app << "("<< app->getUuid()<< ")"<<endl;

        cout << "Createing Links"<<endl;
        this->getSimulation()->addLink( mix->getOutPort("Combined"),app->getInPort("Data"));
        this->getSimulation()->addLink( app->getOutPort("Data"),this->getOutPortTuple("out")->getInPort());
        cout << "created"<<endl;
    }
}

void P8BaseLine::initSCB(double width, double height)
{
    cout << "Createing City Blocks"<<endl;
    DM::Module *mix=this->getSimulation()->getModuleWithUUID(mmap.value("Mixer").toStdString());
    QString inports = QString::fromStdString(mix->getParameterAsString("Inports"));
    inports+=QString("*|*CityBlocks");
    mix->setParameterValue("Inports",inports.toStdString());
    mix->init();
    DM::Module *cb;
    cb=this->getSimulation()->addModule("CityBlock");
    cb->setGroup(this);
    cb->setParameterValue("Width",QString("%1").arg(width).toStdString());
    cb->setParameterValue("Height",QString("%1").arg(height).toStdString());
    cb->init();
    this->getSimulation()->addLink( cb->getOutPort("City"),mix->getInPort("CityBlocks"));
    mmap.insert("CityBlock",QString::fromStdString(cb->getUuid()));

    double xmin=0;
    double xmax=1000;
    double ymin=0;
    double ymax=1000;
    DM::Module *catchmentBoundarys=this->getSimulation()->getModuleWithUUID(mmap.value("Catchment Boundarys").toStdString());

    if (catchmentBoundarys!=NULL)
    {
        /*
        xmin=QString::fromStdString(catchmentBoundarys->getParameterAsString("MinX")).toDouble();
        xmax=height=QString::fromStdString(catchmentBoundarys->getParameterAsString("MaxX")).toDouble();
        ymin=QString::fromStdString(catchmentBoundarys->getParameterAsString("MinY")).toDouble();
        ymax=height=QString::fromStdString(catchmentBoundarys->getParameterAsString("MaxY")).toDouble();
        */
    }
    width=fabs(xmax-xmin);
    height=fabs(ymax-ymin);

    DM::Module *sb;
    sb=this->getSimulation()->addModule("SuperBlock");
    sb->setGroup(this);
    sb->setParameterValue("Height",QString("%1").arg(height).toStdString());
    sb->init();
    this->getSimulation()->addLink( sb->getOutPort("City"),cb->getInPort("City"));
    mmap.insert("SuperBlock",QString::fromStdString(sb->getUuid()));
}

bool P8BaseLine::createInputDialog() {
    QWidget * w = new P8BaseLine_GUI(this);
    w->show();
    return true;
}


void P8BaseLine::createShape(QString filename, QString name, QString typ )
{
    DM::Module *m = this->getSimulation()->addModule("ImportShapeFile");
    if (m!=NULL)
    {
        //        DM::Logger(DM::Debug) << "1";
        mmap.insert(name,QString::fromStdString(m->getUuid()));
        m->setGroup(this);
        m->setParameterValue("FileName", filename.toStdString());
        DM::Logger(DM::Debug) << filename;
        m->setParameterValue("Identifier", name.toStdString()); //"Landuse"
        m->setParameterValue(typ.toStdString(), "1"); //"isEdge"
        m->init();
        DM::Module *mix=this->getSimulation()->getModuleWithUUID(mmap.value("Mixer").toStdString());
        std::string inports = mix->getParameterAsString("Inports");
        std::stringstream ss(inports);
        ss << "*|*" << name.toStdString();
        mix->setParameterValue("Inports",ss.str());
        mix->init();
        this->getSimulation()->addLink(m->getOutPort("Vec"), mix->getInPort(name.toStdString()));
    }
}

void P8BaseLine::createRaster(QString filename, QString name)
{
    DM::Module * m = this->getSimulation()->addModule("ImportRasterData");
    cout << "Raster: " << m << endl;
    if (m!=NULL)
    {
        mmap.insert(name,QString::fromStdString(m->getUuid()));
        m->setGroup(this);
        m->setParameterValue("Filename", filename.toStdString());
        DM::Logger(DM::Debug) << filename;
        m->setParameterValue("DataName", name.toStdString()); //"Landuse"
        m->init();

        DM::Module *mix=this->getSimulation()->getModuleWithUUID(mmap.value("Mixer").toStdString());
        std::string inports = mix->getParameterAsString("Inports");
        std::stringstream ss(inports);
        ss << "*|*" << name.toStdString();
        mix->setParameterValue("Inports",ss.str());
        mix->init();
        this->getSimulation()->addLink(m->getOutPort("Data"), mix->getInPort(name.toStdString()));
    }
}

