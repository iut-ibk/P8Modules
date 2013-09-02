#include "p8microclimate_gui.h"
#include "p8microclimate.h"
#include <QFileDialog>
#include "ui_p8microclimate_gui.h"
#include "string"
#include "sstream"

p8microclimate_gui::p8microclimate_gui(Microclimate * p8, QWidget *parent) :
    QDialog(parent),
    ui(new Ui::p8microclimate_gui)
{
    ui->setupUi(this);
    this->p8microclimate = p8;

    if(p8microclimate->percentile == 20)
    {
        ui->cmb_perc->setCurrentIndex(0);
    }
    if(p8microclimate->percentile == 50)
    {
        ui->cmb_perc->setCurrentIndex(1);
    }
    if(p8microclimate->percentile == 80)
    {
        ui->cmb_perc->setCurrentIndex(2);
    }
    ostringstream tmp;
    tmp << p8microclimate->gridsize;
    ui->le_gridsize->setText(tmp.str().c_str());
    ui->le_landuse->setText(p8microclimate->landuse.c_str());
    ui->le_map->setText(p8microclimate->mapPic.c_str());
    ui->le_shape->setText(p8microclimate->shapefile.c_str());
    ui->le_WSUDtech->setText(p8microclimate->wsudTech.c_str());

}

p8microclimate_gui::~p8microclimate_gui()
{
    delete ui;
}

void p8microclimate_gui::on_pb_map_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Map jpeg",QDir::currentPath(),"*.jpeg");
    if (fname == "")
        return;
    ui->le_map->setText(fname);
    this->p8microclimate->setParameterValue("MapPic",fname.toStdString());
    //todo set jpeg to background of at the moment not existing gui :-P
}

void p8microclimate_gui::on_pb_shape_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Shape File", QDir::currentPath(), "*.sh");
    if (fname == "")
        return;
    ui->le_shape->setText(fname);
    this->p8microclimate->setParameterValue("Shapefile",fname.toStdString());
}

void p8microclimate_gui::on_pb_landuse_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Landuse File",QDir::currentPath(),"*.txt");
    if(fname == "")
        return;
    ui->le_landuse->setText(fname);
    this->p8microclimate->setParameterValue("Landuse",fname.toStdString());
}

void p8microclimate_gui::on_pb_wsud_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"WSUD Tech File",QDir::currentPath(),"*.csv");
    if(fname == "")
        return;
    ui->le_WSUDtech->setText(fname);
    this->p8microclimate->setParameterValue("WSUDtech",fname.toStdString());
}

void p8microclimate_gui::on_bBox_accepted()
{
    int index = ui->cmb_perc->currentIndex();
    this->p8microclimate->setParameterValue("Gridsize",ui->le_gridsize->text().toStdString());
    if(index == 0)
    {
        this->p8microclimate->setParameterValue("Percentile","20");
    }
    if(index == 1)
    {
        this->p8microclimate->setParameterValue("Percentile","50");
    }
    if(index == 2)
    {
        this->p8microclimate->setParameterValue("Percentile","80");
    }
}
