#include "p8microclimate_heat_gui.h"
#include "p8microclimate_heat.h"
#include <QFileDialog>
#include "ui_p8microclimate_heat_gui.h"
#include "string"
#include "sstream"
#include <QTextStream>
#include <QMessageBox>
#include <QSettings>
#include "mcedit/mcedit_heat.h"


p8microclimate_heat_gui::p8microclimate_heat_gui(Microclimate_heat * p8, QWidget *parent) :
    QDialog(parent),
    ui(new Ui::p8microclimate_heat_gui)
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
    if(p8microclimate->percentile == 4)
    {
        ui->cmb_perc->setCurrentIndex(3);
    }
    ostringstream tmp;
    tmp << p8microclimate->gridsize;
    ui->le_gridsize->setText(tmp.str().c_str());
    ui->le_landuse->setText(p8microclimate->landuse.c_str());
    ui->le_map->setText(p8microclimate->mapPic.c_str());
    ui->le_shape->setText(p8microclimate->shapefile.c_str());
    //ui->le_WSUDtech->setText(p8microclimate->wsudTech.c_str());
    ui->le_techFile->setText(p8microclimate->techFile.c_str());
    this->oldGridsize = this->p8microclimate->gridsize;

}

QList<QList<double> > p8microclimate_heat_gui::getTec()
{
    foreach (QList<double> list,this->p8microclimate->tec)
    {
        cout << endl;
        foreach (double val,list)
        {
            cout << val << " ";
        }
    }
    return this->p8microclimate->tec;
}

void p8microclimate_heat_gui::setTec(QList<QList<double> > tec)
{
    /*

*/
    this->p8microclimate->tec = tec;
}

p8microclimate_heat_gui::~p8microclimate_heat_gui()
{
    delete ui;
}

void p8microclimate_heat_gui::on_pb_map_released()
{
    QSettings settings;
    this->p8microclimate->workingDir = settings.value("workPath").toString().toStdString();
    QString datapath = settings.value("dataPath").toString() + "/";
    QString fname = QFileDialog::getOpenFileName(this,"Map png",datapath,"*.png");
    if (fname == "")
        return;
    QFileInfo finfo = QFileInfo(fname);
    ui->le_map->setText(finfo.fileName());
    this->p8microclimate->setParameterValue("MapPic",finfo.fileName().toStdString());
    QFileInfo workfinfo = QFileInfo(QString(settings.value("workPath").toString() + "/" + finfo.fileName()));
    if(finfo.absolutePath() != workfinfo.absolutePath())
    {
        if( QFile::exists(settings.value("workPath").toString() + finfo.fileName()))
        {
            QFile::remove(settings.value("workPath").toString() +"/"+ finfo.fileName());
            QFile::copy(fname,settings.value("workPath").toString() +"/"+ finfo.fileName());
        }
        else
        {
            QFile::copy(fname,settings.value("workPath").toString() +"/"+ finfo.fileName());
        }
    }
    settings.setValue("dataPath",finfo.absolutePath());

}

void p8microclimate_heat_gui::on_pb_shape_released()
{
    QSettings settings;
    this->p8microclimate->workingDir = settings.value("workPath").toString().toStdString();
    QString datapath = settings.value("dataPath").toString() + "/";
    QString fname = QFileDialog::getOpenFileName(this,"Shape File", datapath, "*.sh");
    if (fname == "")
        return;
    QFileInfo finfo = QFileInfo(fname);
    ui->le_shape->setText(finfo.fileName());
    this->p8microclimate->setParameterValue("Shapefile",finfo.fileName().toStdString());
    QFileInfo workfinfo = QFileInfo(QString(settings.value("workPath").toString() + "/" + finfo.fileName()));
    if(finfo.absolutePath() != workfinfo.absolutePath())
    {
        if( QFile::exists(settings.value("workPath").toString() + finfo.fileName()))
        {
            QFile::remove(settings.value("workPath").toString() +"/"+ finfo.fileName());
            QFile::copy(fname,settings.value("workPath").toString() +"/"+ finfo.fileName());
        }
        else
        {
            QFile::copy(fname,settings.value("workPath").toString() +"/"+ finfo.fileName());
        }
    }
    settings.setValue("dataPath",finfo.absolutePath());

}

void p8microclimate_heat_gui::on_pb_landuse_released()
{
    QSettings settings;
    this->p8microclimate->workingDir = settings.value("workPath").toString().toStdString();
    QString datapath = settings.value("dataPath").toString() + "/";
    QString fname = QFileDialog::getOpenFileName(this,"Landuse File",datapath,"*.txt");
    if(fname == "")
        return;
    QFileInfo finfo = QFileInfo(fname);
    ui->le_landuse->setText(finfo.fileName());
    this->p8microclimate->setParameterValue("Landuse",finfo.fileName().toStdString());
    QFileInfo workfinfo = QFileInfo(QString(settings.value("workPath").toString() + "/" + finfo.fileName()));
    if(finfo.absolutePath() != workfinfo.absolutePath())
    {
        if( QFile::exists(settings.value("workPath").toString() + finfo.fileName()))
        {
            QFile::remove(settings.value("workPath").toString() +"/"+ finfo.fileName());
            QFile::copy(fname,settings.value("workPath").toString() +"/"+ finfo.fileName());
        }
        else
        {
            QFile::copy(fname,settings.value("workPath").toString() +"/"+ finfo.fileName());
        }
    }
    settings.setValue("dataPath",finfo.absolutePath());
}

void p8microclimate_heat_gui::on_pb_wsud_released()
{
    QSettings settings;
    this->p8microclimate->workingDir = settings.value("workPath").toString().toStdString();
    QString fname = QFileDialog::getOpenFileName(this,"WSUD Tech File",QString(this->p8microclimate->workingDir.c_str()),"*.csv");
    if(fname == "")
        return;
    //ui->le_WSUDtech->setText(fname);
    this->p8microclimate->setParameterValue("WSUDtech",fname.toStdString());
}
void p8microclimate_heat_gui::on_pb_techFile_released()
{
    QSettings settings;
    this->p8microclimate->workingDir = settings.value("workPath").toString().toStdString();
    QString datapath = settings.value("dataPath").toString() + "/";
    QString fname = QFileDialog::getOpenFileName(this,"Landuse File",datapath,"*.txt");
    if(fname == "")
        return;
    QFileInfo finfo = QFileInfo(fname);
    ui->le_techFile->setText(finfo.fileName());
    this->p8microclimate->setParameterValue("Techfile",finfo.fileName().toStdString());
    QFileInfo workfinfo = QFileInfo(QString(settings.value("workPath").toString() + "/" + finfo.fileName()));
    if(finfo.absolutePath() != workfinfo.absolutePath())
    {
        if( QFile::exists(settings.value("workPath").toString() + finfo.fileName()))
        {
            QFile::remove(settings.value("workPath").toString() +"/"+ finfo.fileName());
            QFile::copy(fname,settings.value("workPath").toString() +"/"+ finfo.fileName());
        }
        else
        {
            QFile::copy(fname,settings.value("workPath").toString() +"/"+ finfo.fileName());
        }
    }
    settings.setValue("dataPath",finfo.absolutePath());
    if(QFile::exists(settings.value("workPath").toString() + "/WSUDtech.mcd"));
        QFile::remove(settings.value("workPath").toString() +"/WSUDtech.mcd");
}
void p8microclimate_heat_gui::on_bBox_accepted()
{
    this->p8microclimate->setParameterValue("MapPic",ui->le_map->text().toStdString());
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
    if(index == 3)
    {
        this->p8microclimate->setParameterValue("Percentile","4");
    }
    this->p8microclimate->setParameterValue("Techfile",ui->le_techFile->text().toStdString());

    // remove mcd file if gridsize is changed
    if(this->oldGridsize != this->p8microclimate->gridsize)
    {
        QSettings settings;
        if(QFile::exists(settings.value("workPath").toString() + "/WSUDtech.mcd"));
            QFile::remove(settings.value("workPath").toString() +"/WSUDtech.mcd");
    }
}

void p8microclimate_heat_gui::on_pb_placeTech_released()
{
    this->p8microclimate->setParameterValue("Gridsize",ui->le_gridsize->text().toStdString());
    QSettings settings;
    this->p8microclimate->workingDir = settings.value("workPath").toString().toStdString();
    int cols;
    int rows;
    double cellsize,newcols,newrows;
    QString input;
    QFile file(QString(this->p8microclimate->workingDir.c_str()) + "/impfile.txt");

    if (file.open(QIODevice::Text|QIODevice::ReadOnly))
    {
        QTextStream stream;
        stream.setDevice(&file);
        input = stream.readLine();
        file.close();
        file.setFileName(QString(this->p8microclimate->workingDir.c_str()) +"/"+ input);
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


        edit=new mcedit_heat(this,ui->le_map->text(),QString(this->p8microclimate->workingDir.c_str()),newcols,newrows,30,30);
        edit->show();
    }
    else
        QMessageBox::critical(this,"Error","Internal Error 354235");
}


