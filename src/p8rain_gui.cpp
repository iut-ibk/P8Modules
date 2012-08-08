#include "p8rain_gui.h"
#include "ui_p8rain_gui.h"
#include "p8rain.h"
#include <QFileDialog>

P8Rain_GUI::P8Rain_GUI(P8Rain * p8, QWidget *parent) :
    QDialog(parent),
    ui(new Ui::P8Rain_GUI)
{
    ui->setupUi(this);
    this->p8rain = p8;

    ui->le_r->setText(QString::fromStdString(p8->getParameterAsString("FileNameR")));
}

P8Rain_GUI::~P8Rain_GUI()
{
    delete ui;
}

void P8Rain_GUI::on_pb_r_released()
{
    QString fname = QFileDialog::getOpenFileName(this,"Rain",QDir::currentPath(),"*.nc");
    this->p8rain->createRain(fname,"Rain","isFace");
    p8rain->setParameterValue("FileNameR",fname.toStdString());
    ui->le_r->setText(fname);
}
