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


}

P8BaseLine_GUI::~P8BaseLine_GUI()
{
    delete ui;
}

void P8BaseLine_GUI::on_pb_c_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Catchment Boundarys",QDir::currentPath(),"*.shp");
    this->p8baseline->createShape(fname,"Catchment Boundarys","isEdge");
    cout << "Wuuuu" << endl;
    this->p8baseline->initSCB(ui->sb_gs->value(), ui->sb_gs->value());
    ui->le_c->setText(fname);
}

void P8BaseLine_GUI::on_pb_e_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Elevation Map",QDir::currentPath(),"*.*");
    this->p8baseline->createRaster(fname,"Elevation");
    ui->le_e->setText(fname);
}

void P8BaseLine_GUI::on_pb_s_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Soil Map",QDir::currentPath(),"*.*");
    this->p8baseline->createRaster(fname,"Soil");
    ui->le_e->setText(fname);
}

void P8BaseLine_GUI::on_pb_p_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Population Map",QDir::currentPath(),"*.*");
    this->p8baseline->createRaster(fname,"Population");
    ui->le_e->setText(fname);
}

void P8BaseLine_GUI::on_pb_l_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Landuse Map",QDir::currentPath(),"*.*");
    this->p8baseline->createRaster(fname,"Landuse");
    ui->le_e->setText(fname);
}
