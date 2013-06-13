#include "p8realisation2_gui.h"
#include "ui_p8realisation2_gui.h"
#include "p8realisation2.h"

p8realisation2_gui::p8realisation2_gui(Current_Realisation2 * p8,QWidget *parent) :
    QDialog(parent),
    ui(new Ui::p8realisation2_gui)
{
    ui->setupUi(this);
    this->p8realisation = p8;
    ui->le_mNr->setText(QString::fromStdString(p8->getParameterAsString("RealisationNr")));
}

p8realisation2_gui::~p8realisation2_gui()
{
    delete ui;
}

void p8realisation2_gui::on_buttonBox_accepted()
{
    this->p8realisation->setParameterValue("RealisationNr",ui->le_mNr->text().toStdString());
}
