#include "p8microclimate_gui.h"
#include "p8microclimate.h"
#include <QFileDialog>
#include "ui_p8microclimate_gui.h"
#include "string"
#include "sstream"
#include <QTextStream>
#include <QMessageBox>
#include <QSettings>
#include "mcedit/mcedit.h"


p8microclimate_gui::p8microclimate_gui(Microclimate * p8, QWidget *parent) :
    QDialog(parent),
    ui(new Ui::p8microclimate_gui)
{
    ui->setupUi(this);

    this->p8microclimate = p8;

    QSettings settings;
    this->p8microclimate->workingDir = settings.value("workPath").toString().toStdString();

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
    //ui->le_WSUDtech->setText(p8microclimate->wsudTech.c_str());

}

QList<QList<double> > p8microclimate_gui::getTec()
{
    QList<QList<double> > tec;
    //tec=
    return tec;
}

void p8microclimate_gui::setTec(QList<QList<double> > tec)
{
//    p8microclimate->setTec(tec);
}

p8microclimate_gui::~p8microclimate_gui()
{
    delete ui;
}

void p8microclimate_gui::on_pb_map_released()
{
    QSettings settings;
    this->p8microclimate->workingDir = settings.value("workPath").toString().toStdString();
    QString fname = QFileDialog::getOpenFileName(this,"Map png",QString(this->p8microclimate->workingDir.c_str()),"*.png");
    if (fname == "")
        return;
    ui->le_map->setText(fname);
    this->p8microclimate->setParameterValue("MapPic",fname.toStdString());
}

void p8microclimate_gui::on_pb_shape_released()
{
    QSettings settings;
    this->p8microclimate->workingDir = settings.value("workPath").toString().toStdString();
    QString fname = QFileDialog::getOpenFileName(this,"Shape File", QString(this->p8microclimate->workingDir.c_str()), "*.sh");
    if (fname == "")
        return;
    ui->le_shape->setText(fname);
    this->p8microclimate->setParameterValue("Shapefile",fname.toStdString());
}

void p8microclimate_gui::on_pb_landuse_released()
{
    QSettings settings;
    this->p8microclimate->workingDir = settings.value("workPath").toString().toStdString();
    QString fname = QFileDialog::getOpenFileName(this,"Landuse File",QString(this->p8microclimate->workingDir.c_str()),"*.txt");
    if(fname == "")
        return;
    ui->le_landuse->setText(fname);
    this->p8microclimate->setParameterValue("Landuse",fname.toStdString());
}

void p8microclimate_gui::on_pb_wsud_released()
{
    QSettings settings;
    this->p8microclimate->workingDir = settings.value("workPath").toString().toStdString();
    QString fname = QFileDialog::getOpenFileName(this,"WSUD Tech File",QString(this->p8microclimate->workingDir.c_str()),"*.csv");
    if(fname == "")
        return;
    //ui->le_WSUDtech->setText(fname);
    this->p8microclimate->setParameterValue("WSUDtech",fname.toStdString());
}

void p8microclimate_gui::on_bBox_accepted()
{
    this->p8microclimate->setParameterValue("mapPic",ui->le_map->text().toStdString());
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

void p8microclimate_gui::on_pb_placeTech_released()
{
    QSettings settings;
    this->p8microclimate->workingDir = settings.value("workPath").toString().toStdString();
    int cols;
    int rows;
    double cellsize,newcols,newrows;
    QString input;
    QFile file(QString(QDir::currentPath()+"/impfile.txt"));

    if (file.open(QIODevice::Text|QIODevice::ReadOnly))
    {
        QTextStream stream;
        stream.setDevice(&file);
        input = stream.readLine();
        file.close();
        file.setFileName(input);
        file.open(QIODevice::Text|QIODevice::ReadOnly);
        int i = 0;

        while(i<5)
        {
            QString inputs = stream.readLine();
            QStringList list = inputs.split(" ",QString::SkipEmptyParts);
            if(i == 0)
                cols = list.takeLast().toInt();
            if(i == 1)
                rows = list.takeLast().toInt();
            if(i == 4)
                cellsize = list.takeLast().toDouble();
            i++;
        }
        file.close();
        newcols = cols*cellsize/this->p8microclimate->gridsize;
        newrows = rows*cellsize/this->p8microclimate->gridsize;
        if(newcols - (int)newcols != 0)
            newcols = (int)newcols +1;
        if(newrows - (int)newrows != 0)
            newrows = (int)newrows + 1;


        edit=new mcedit(this,ui->le_map->text(),QString(this->p8microclimate->workingDir.c_str()),newcols,newrows,30,30);
        edit->show();
    }
    else
        QMessageBox::critical(this,"Error","Internal Error 354235");
}
