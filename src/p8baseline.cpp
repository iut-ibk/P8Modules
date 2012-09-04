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

}

void P8BaseLine::run() {

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

void P8BaseLine::init() {
    this->addTuplePort("out", DM::OUTTUPLESYSTEM);
    if (mmap.size()==0)
    {
        cout << "Creating Mixer"<<endl;
        DM::Module *mix;
        mix=this->getSimulation()->addModule("AppendViewFromSystem");
        mix->setGroup(this);
        mix->init();
        mmap.insert("Mixer",QString::fromStdString(mix->getUuid()));
        cout << "created: " << mix << "("<< mix->getUuid()<< ")"<<endl;
/*
        cout << "Creating CityBlocks"<<endl;
        DM::Module *cb;
        cb=this->getSimulation()->addModule("CityBlock");
        cb->setGroup(this);
        cb->init();
        mmap.insert("CityBlock",QString::fromStdString(cb->getUuid()));
        createCityBlocksFromShape(100,100);
        cout << "created: " << cb << "("<< cb->getUuid()<< ")"<<endl;

        cout << "Creating Append"<<endl;
        DM::Module *app;
        app=this->getSimulation()->addModule("AppendRasterAsAttribute");
        app->setGroup(this);
        app->init();
        mmap.insert("Append",QString::fromStdString(app->getUuid()));
        cout << "created: " << app << "("<< app->getUuid()<< ")"<<endl;

        cout << "Creating CalculateCentroid"<<endl;
        DM::Module *cc;
        cc=this->getSimulation()->addModule("CalculateCentroid");
        cc->setGroup(this);
        cc->setParameterValue("NameOfExistingView","SUPERBLOCK");
        cc->init();
        mmap.insert("CalculateCentroid",QString::fromStdString(cc->getUuid()));
        cout << "created: " << cc << "("<< cc->getUuid()<< ")"<<endl;
*/
        cout << "Createing Links"<<endl;
  /*      DM::ModuleLink * l1=this->getSimulation()->addLink( mix->getOutPort("Combined"),cb->getInPort("City"));
        DM::ModuleLink * l2=this->getSimulation()->addLink( cb->getOutPort("City"),app->getInPort("Data"));
        DM::ModuleLink * l3=this->getSimulation()->addLink( app->getOutPort("Data"),cc->getInPort("Data"));
        DM::ModuleLink * l4=this->getSimulation()->addLink( cc->getOutPort("Data"),this->getOutPortTuple("out")->getInPort());
        //DM::ModuleLink * l1=this->getSimulation()->addLink( mix->getOutPort("Combined"),this->getOutPortTuple("out")->getInPort());
        */
        DM::ModuleLink * l1=this->getSimulation()->addLink( mix->getOutPort("Combined"),this->getOutPortTuple("out")->getInPort());
        cout << "created"<<endl;


        /*
        cout << "Creating City Blocks"<<endl;
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
*/

















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
        DM::ModuleLink *l_placementTech_streetTechOpp=this->getSimulation()->addLink( placementTech->getOutPort("City"),streetTechOpp->getInPort("City"));
        DM::ModuleLink *l_streetTechOpp_mixer2=this->getSimulation()->addLink( streetTechOpp->getOutPort("City"),mixer2->getInPort("City"));
        DM::ModuleLink *l_placementTech_neighTechOpp=this->getSimulation()->addLink( placementTech->getOutPort("City"),neighTechOpp->getInPort("City"));
        DM::ModuleLink *l_neighTechOpp_mixer2=this->getSimulation()->addLink( neighTechOpp->getOutPort("City"),mixer2->getInPort("City"));
        DM::ModuleLink *l_placementTech_precTechOpp=this->getSimulation()->addLink( placementTech->getOutPort("City"),precTechOpp->getInPort("City"));
        DM::ModuleLink *l_precTechOpp_mixer2=this->getSimulation()->addLink( precTechOpp->getOutPort("City"),mixer2->getInPort("City"));
        // end created by netread








    }
}

void P8BaseLine::createCityBlocksFromShape(double width, double height)
{
/*
    DM::Module *cb;
    cb=this->getSimulation()->getModuleWithUUID(mmap.value("CityBlock").toStdString());
    cb->setParameterValue("Width",QString("%1").arg(width).toStdString());
    cb->setParameterValue("Height",QString("%1").arg(height).toStdString());
    cb->init();
*/
}


/*
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
          //    xmin=QString::fromStdString(catchmentBoundarys->getParameterAsString("MinX")).toDouble();
    //    xmax=height=QString::fromStdString(catchmentBoundarys->getParameterAsString("MaxX")).toDouble();
    //    ymin=QString::fromStdString(catchmentBoundarys->getParameterAsString("MinY")).toDouble();
    //    ymax=height=QString::fromStdString(catchmentBoundarys->getParameterAsString("MaxY")).toDouble();

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
*/


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
        m->setParameterValue("Identifier", "SUPERBLOCK");    //);name.toStdString()); //"Landuse"
        m->setParameterValue(typ.toStdString(), "1"); //"isEdge"
        m->init();
        DM::Module *mix=this->getSimulation()->getModuleWithUUID(mmap.value("Mixer").toStdString());    
        QString inports = QString::fromStdString(mix->getParameterAsString("Inports"));
        inports += "*|*" + name;
        mix->setParameterValue("Inports",inports.toStdString());
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
        QString inports = QString::fromStdString(mix->getParameterAsString("Inports"));
        inports += "*|*" + name;
        mix->setParameterValue("Inports",inports.toStdString());
        mix->init();
        DM::ModuleLink * l = this->getSimulation()->addLink(m->getOutPort("Data"), mix->getInPort(name.toStdString()));
    }
}
