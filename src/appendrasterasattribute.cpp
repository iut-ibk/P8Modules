#include "appendrasterasattribute.h"
#include <rasterdatahelper.h>
#include <tbvectordata.h>
#include <rasterdatahelper.h>
#include <dm.h>

DM_DECLARE_NODE_NAME( AppendRasterAsAttribute ,CRCP8 )


AppendRasterAsAttribute::AppendRasterAsAttribute() {
    sys_in = 0;
    this->NameOfExistingView = "";
    this->newAttribute = "";

    superblock = DM::View("SUPERBLOCK", DM::FACE, DM::READ);
    superblock.getAttribute("MinX");
    superblock.getAttribute("MinY");

    data.push_back(  DM::View ("CITYBLOCK", DM::FACE, DM::MODIFY) );
    data.push_back(superblock);
    this->addData("Data", data);
}


void AppendRasterAsAttribute::run() {

    DM::System * sys = this->getData("Data");

    std::string sb_uuid = sys->getUUIDsOfComponentsInView(superblock)[0];

    DM::Component * sb = sys->getComponent(sb_uuid);

    if (!sb) {
        DM::Logger(DM::Error) << "No Superblock";
        return;
    }


    double offsetX  = -sb->getAttribute("MinX")->getDouble();
    double offsetY = -sb->getAttribute("MinY")->getDouble();

    DM::Node * offset = new DM::Node(offsetX, offsetY, 0);
    foreach (std::string rName, nameOfRasterData) {
        DM::RasterData * r = this->getRasterData("Data", DM::View(rName, DM::READ, DM::RASTERDATA));

        foreach (std::string s, sys->getUUIDsOfComponentsInView(data[0])) {
            DM::Face * f = sys->getFace(s);
            std::vector<DM::Node*> nl = TBVectorData::getNodeListFromFace(sys, f);
            double dattr = 0;
            median = true;
            if (median) {
                dattr = RasterDataHelper::meanOverArea(r,nl, offset);
            } else {
                dattr = RasterDataHelper::sumOverArea(r,nl, 0, offset);
            }
            f->changeAttribute(rName, dattr);
        }
    }

    delete offset;

}

bool AppendRasterAsAttribute::createInputDialog() {
    //QWidget * w = new GUIAppendRasterAsAttribute(this);
    //w->show();
    return false;
}

void AppendRasterAsAttribute::init()
{

    sys_in = this->getData("Data");

    if (!sys_in)
        return;

    std::vector<std::string> views = sys_in->getNamesOfViews();

    nameOfRasterData.clear();
    foreach (std::string s, views) {
        DM::Logger(DM::Debug) << s;
        DM::View * v = this->sys_in->getViewDefinition(s);
        if (v->getType() == DM::RASTERDATA) {
            nameOfRasterData.push_back(v->getName());
        }
    }

    DM::View * v = sys_in->getViewDefinition("CITYBLOCK");
    DM::View v_new = DM::View(v->getName(), v->getType(), DM::READ);
    foreach (std::string s, nameOfRasterData) {
        v_new.addAttribute(s);
    }
    data.clear();
    data.push_back(v_new);
    data.push_back(superblock);
    this->addData("Data", data);

}
