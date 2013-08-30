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

    ui->cmb_perc->setCurrentIndex(this->p8microclimate->percentile);
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

void p8microclimate_gui::on_bBox_accepted()
{
    std::ostringstream tmp;
    int index = ui->cmb_perc->currentIndex();
    tmp << index;
    this->p8microclimate->setParameterValue("Gridsize",ui->le_gridsize->text().toStdString());
    this->p8microclimate->setParameterValue("Percentile",tmp.str());
}
