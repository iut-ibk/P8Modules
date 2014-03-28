#include "p8baseline_gui.h"
#include "ui_p8baseline_gui.h"
#include "p8baseline.h"
#include <QFileDialog>

URBAN_FORM_GUI::URBAN_FORM_GUI(URBAN_FORM * p8, QWidget *parent) :
    QDialog(parent),
    ui(new Ui::URBAN_FORM_GUI)
{
    ui->setupUi(this);
    this->p8baseline = p8;



    ui->le_c->setText(QString::fromStdString(p8->getParameterAsString("FileNameC")));
    ui->le_s->setText(QString::fromStdString(p8->getParameterAsString("FileNameS")));
    ui->le_t->setText(QString::fromStdString(p8->getParameterAsString("FileNameT")));
    ui->le_p->setText(QString::fromStdString(p8->getParameterAsString("FileNameP")));
    ui->le_d->setText(QString::fromStdString(p8->getParameterAsString("FileNameD")));
    ui->le_l->setText(QString::fromStdString(p8->getParameterAsString("FileNameL")));
    //ui->sb_gs->setValue(QString::fromStdString(p8->getParameterAsString("RasterSize")).toDouble());
}

URBAN_FORM_GUI::~URBAN_FORM_GUI()
{
    delete ui;
}

void URBAN_FORM_GUI::on_pb_c_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Catchment Boundarys",QDir::currentPath(),"*.shp");
    if (fname == "")
        return;
    this->p8baseline->createShape(fname,"Catchment Boundarys","isFace");
    p8baseline->setParameterValue("FileNameC",fname.toStdString());
    ui->le_c->setText(fname);
}

void URBAN_FORM_GUI::on_pb_s_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Soil Map",QDir::currentPath(),"*.*");
    this->p8baseline->createRaster(fname,"Soil");
    p8baseline->setParameterValue("FileNameS",fname.toStdString());
    ui->le_s->setText(fname);
}

void URBAN_FORM_GUI::on_pb_t_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Topology",QDir::currentPath(),"*.*");
    this->p8baseline->createRaster(fname,"Elevation");
    p8baseline->setParameterValue("FileNameT",fname.toStdString());
    ui->le_t->setText(fname);
}

void URBAN_FORM_GUI::on_pb_p_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Plan Map",QDir::currentPath(),"*.*");
    this->p8baseline->createRaster(fname,"PlanMap");
    p8baseline->setParameterValue("FileNameP",fname.toStdString());
    ui->le_p->setText(fname);
}

void URBAN_FORM_GUI::on_pb_d_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Population Map",QDir::currentPath(),"*.*");
    this->p8baseline->createRaster(fname,"Population");
    p8baseline->setParameterValue("FileNameD",fname.toStdString());
    ui->le_d->setText(fname);
}

void URBAN_FORM_GUI::on_pb_l_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Landuse Map",QDir::currentPath(),"*.*");
    this->p8baseline->createRaster(fname,"LandUse");
    p8baseline->setParameterValue("FileNameL",fname.toStdString());
    ui->le_l->setText(fname);
}

void URBAN_FORM_GUI::on_sb_gs_editingFinished()
{
    //QString rs=QString("%1").arg(ui->sb_gs->value());
    //p8baseline->setParameterValue("RasterSize",rs.toStdString());
}

void URBAN_FORM_GUI::on_buttonBox_accepted()
{
//    this->p8baseline->createCityBlocksFromShape(ui->sb_gs->value(), ui->sb_gs->value());
}
