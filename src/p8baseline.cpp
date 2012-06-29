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
        this->getSimulation()->addLink( mix->getOutPort("Combined"),this->getOutPortTuple("out")->getInPort());
        mmap.insert("Mixer",QString::fromStdString(mix->getUuid()));
        cout << "created: " << mix << "("<< mix->getUuid()<< ")"<<endl;
    }
}

void P8BaseLine::initSCB(double width, double height)
{
    cout << "Createing City Blocks"<<endl;
    DM::Module *mix=this->getSimulation()->getModuleWithUUID(mmap.value("Mixer").toStdString());
    cout << "-> 1" << endl;
    QString inports = QString::fromStdString(mix->getParameterAsString("Inports"));
    cout << "-> 2" << endl;
    inports+=QString("*|*CityBlocks");
    cout << "-> 3" << endl;
    mix->setParameterValue("Inports",inports.toStdString());
    cout << "-> 4" << endl;
    mix->init();
    cout << "-> 5" << endl;
    DM::Module *cb;
    cout << "-> 6" << endl;
    cb=this->getSimulation()->addModule("CityBlock");
    cout << "-> 7" << endl;
    cb->setGroup(this);
    cout << "-> 8" << endl;
    cb->setParameterValue("Width",QString("%1").arg(width).toStdString());
    cout << "-> 9" << endl;
    cb->setParameterValue("Height",QString("%1").arg(height).toStdString());
    cout << "-> 10" << endl;
    cb->init();
    cout << "-> 11" << endl;
    this->getSimulation()->addLink( cb->getOutPort("City"),mix->getInPort("CityBlocks"));
    cout << "-> 12" << endl;
    mmap.insert("CityBlock",QString::fromStdString(cb->getUuid()));
    cout << "-> 13" << endl;

    double xmin=0;
    cout << "-> 14" << endl;
    double xmax=1000;
    cout << "-> 15" << endl;
    double ymin=0;
    cout << "-> 16" << endl;
    double ymax=1000;
    cout << "-> 17" << endl;
    DM::Module *catchmentBoundarys=this->getSimulation()->getModuleWithUUID(mmap.value("Catchment Boundarys").toStdString());
    cout << "-> 18" << endl;

    if (catchmentBoundarys!=NULL)
    {
        /*
        cout << "-> 19" << endl;
        xmin=QString::fromStdString(catchmentBoundarys->getParameterAsString("MinX")).toDouble();
        cout << "-> 20" << endl;
        xmax=height=QString::fromStdString(catchmentBoundarys->getParameterAsString("MaxX")).toDouble();
        cout << "-> 21" << endl;
        ymin=QString::fromStdString(catchmentBoundarys->getParameterAsString("MinY")).toDouble();
        cout << "-> 22" << endl;
        ymax=height=QString::fromStdString(catchmentBoundarys->getParameterAsString("MaxY")).toDouble();
        cout << "-> 23" << endl;*/
        xmin=0;
        xmax=1000;
        ymin=0;
        ymax=1000;
    }
    cout << "-> 24" << endl;
    width=fabs(xmax-xmin);
    cout << "-> 25" << endl;
    height=fabs(ymax-ymin);
    cout << "-> 26" << endl;

    cout << "-> 27" << endl;
    DM::Module *sb;
    cout << "-> 28" << endl;
    sb=this->getSimulation()->addModule("SuperBlock");
    cout << "-> 29" << endl;
    sb->setGroup(this);
    cout << "-> 30" << endl;
    sb->setParameterValue("Height",QString("%1").arg(height).toStdString());
    cout << "-> 31" << endl;
    sb->init();
    cout << "-> 32" << endl;
    this->getSimulation()->addLink( sb->getOutPort("City"),cb->getInPort("City"));
    cout << "-> 33" << endl;
    mmap.insert("SuperBlock",QString::fromStdString(sb->getUuid()));
    cout << "-> 34" << endl;
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

