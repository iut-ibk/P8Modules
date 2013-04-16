#include "p8realisation_gui.h"
#include "ui_p8realisation_gui.h"
#include "p8realisations.h"

p8realisation_gui::p8realisation_gui(Realisations * p8,QWidget *parent) :
    QDialog(parent),
    ui(new Ui::p8realisation_gui)
{
    ui->setupUi(this);
    this->p8realisation = p8;
    ui->le_mNr->setText(QString::fromStdString(p8->getParameterAsString("RealisationNr")));
}

p8realisation_gui::~p8realisation_gui()
{
    delete ui;
}

void p8realisation_gui::on_buttonBox_accepted()
{
    this->p8realisation->setParameterValue("RealisationNr",ui->le_mNr->text().toStdString());
}
