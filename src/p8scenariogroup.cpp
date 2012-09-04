#include "p8scenariogroup.h"
#include <rasterdatahelper.h>
#include <tbvectordata.h>
#include <rasterdatahelper.h>
#include <dm.h>

DM_DECLARE_NODE_NAME( P8ScenarioGroup ,CRCP8 )


P8ScenarioGroup::P8ScenarioGroup() {
    this->median = false;
    this->multiplier = 1;

    this->addParameter("Multiplier", DM::DOUBLE, &this->multiplier);
    this->addParameter("Median", DM::BOOL, &this->median);
    this->addParameter("NameOfRasterData", DM::STRING, &this->NameOfRasterData);
    this->addParameter("NameOfExistingView", DM::STRING, &this->NameOfExistingView);
    this->addParameter("newAttribute", DM::STRING, &this->newAttribute);

    sys_in = 0;
    this->NameOfRasterData = "";
    this->NameOfExistingView = "";
    this->newAttribute = "";

    data.push_back(  DM::View ("dummy", DM::SUBSYSTEM, DM::MODIFY) );

    this->addData("Data", data);
}


void P8ScenarioGroup::run() {

    DM::System * sys = this->getData("Data");
    DM::View * v_existing= sys->getViewDefinition(NameOfExistingView);


    // foreach raster
//{
// newAttributeName=
    DM::RasterData * r = this->getRasterData("Data", DM::View(NameOfRasterData, DM::READ, DM::RASTERDATA));
    foreach (std::string s, sys->getUUIDsOfComponentsInView(*v_existing)) {
        DM::Face * f = sys->getFace(s);
        std::vector<DM::Node*> nl = TBVectorData::getNodeListFromFace(sys, f);
        double dattr = 0;
        if (median) {
            dattr = RasterDataHelper::meanOverArea(r,nl) * multiplier;
        } else {
            dattr = RasterDataHelper::sumOverArea(r,nl,0) * multiplier;
        }
        f->changeAttribute(newAttribute, dattr);
        // }
    }
}

bool P8ScenarioGroup::createInputDialog() {
    //QWidget * w = new GUIP8ScenarioGroup(this);
    //w->show();
    return false;
}

void P8ScenarioGroup::init()
{

    DM::System *  sys_in = this->getData("Data");
    //if ()

    std::vector<std::string> name_views = sys_in->getNamesOfViews();
    std::vector<DM::View> NameOfRasterData;
    foreach (std::string idView, name_views) {
        DM::View * v = sys_in->getViewDefinition(idView);

    }

    if (sys_in == 0)
        return;
    std::vector<std::string> views = sys_in->getNamesOfViews();


    foreach (std::string s, views)
        DM::Logger(DM::Debug) << s;

    if (this->NameOfExistingView.empty())
        return;
    if (this->newAttribute.empty())
        return;
    if (newAttribute_old.compare(newAttribute) == 0)
        return;


    DM::View * v = sys_in->getViewDefinition(NameOfExistingView);
    readView = DM::View(v->getName(), v->getType(), DM::READ);
    readView.addAttribute(newAttribute);

    data.push_back(readView);
    this->addData("Data", data);


    newAttribute_old = newAttribute;


}
