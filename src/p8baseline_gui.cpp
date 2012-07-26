#include "p8baseline_gui.h"
#include "ui_p8baseline_gui.h"
#include "p8baseline.h"
#include <QFileDialog>

P8BaseLine_GUI::P8BaseLine_GUI(P8BaseLine * p8, QWidget *parent) :
    QDialog(parent),
    ui(new Ui::P8BaseLine_GUI)
{
    ui->setupUi(this);
    this->p8baseline = p8;

    ui->le_c->setText(QString::fromStdString(p8->getParameterAsString("FileNameC")));
    ui->le_e->setText(QString::fromStdString(p8->getParameterAsString("FileNameE")));
    ui->le_s->setText(QString::fromStdString(p8->getParameterAsString("FileNameS")));
    ui->le_p->setText(QString::fromStdString(p8->getParameterAsString("FileNameP")));
    ui->le_l->setText(QString::fromStdString(p8->getParameterAsString("FileNameL")));
}

P8BaseLine_GUI::~P8BaseLine_GUI()
{
    this->p8baseline->createCityBlocksFromShape(ui->sb_gs->value(), ui->sb_gs->value());
    delete ui;
}

void P8BaseLine_GUI::on_pb_c_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Catchment Boundarys",QDir::currentPath(),"*.shp");
    this->p8baseline->createShape(fname,"Catchment Boundarys","isFace");
    p8baseline->setParameterValue("FileNameC",fname.toStdString());
    ui->le_c->setText(fname);
}

void P8BaseLine_GUI::on_pb_e_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Elevation Map",QDir::currentPath(),"*.*");
    this->p8baseline->createRaster(fname,"Elevation");
    p8baseline->setParameterValue("FileNameE",fname.toStdString());
    ui->le_e->setText(fname);
}

void P8BaseLine_GUI::on_pb_s_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Soil Map",QDir::currentPath(),"*.*");
    this->p8baseline->createRaster(fname,"Soil");
    p8baseline->setParameterValue("FileNameS",fname.toStdString());
    ui->le_s->setText(fname);
}

void P8BaseLine_GUI::on_pb_p_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Population Map",QDir::currentPath(),"*.*");
    this->p8baseline->createRaster(fname,"Population");
    p8baseline->setParameterValue("FileNameP",fname.toStdString());
    ui->le_p->setText(fname);
}

void P8BaseLine_GUI::on_pb_l_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Landuse Map",QDir::currentPath(),"*.*");
    this->p8baseline->createRaster(fname,"Landuse");
    p8baseline->setParameterValue("FileNameL",fname.toStdString());
    ui->le_l->setText(fname);
}
