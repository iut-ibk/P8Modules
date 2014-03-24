#include "p8realisation2_gui.h"
#include "ui_p8realisation2_gui.h"
#include "p8realisation2.h"
#include "QDir"
#include "QSettings"
#include "QString"

p8realisationModule_gui::p8realisationModule_gui(Current_RealisationModule * p8,QWidget *parent) :
    QDialog(parent),
    ui(new Ui::p8realisationModule_gui)
{
    ui->setupUi(this);
    this->p8realisation = p8;
    //ui->le_mNr->setText(QString::fromStdString(p8->getParameterAsString("RealisationNr")));
    QSettings settings;
    QString path = settings.value("workPath").toString();
    QDir dir = QDir(path);
    dir.setFilter(QDir::Files);
    QStringList files = dir.entryList();
    int length = files.length();
    for(int i = 0;i<length;i++)
    {
        if(!files[i].contains("ubeatsMUSIC-ID"))
        {
            files.removeAt(i);
            i--;
            length--;
        }

    }
    ui->comboBox->addItems(files);
}

p8realisationModule_gui::~p8realisationModule_gui()
{
    delete ui;
}

void p8realisationModule_gui::on_buttonBox_accepted()
{
    QSettings settings;
    QString path = settings.value("workPath").toString();
        //this->p8realisation->setParameterValue("RealisationNr",ui->le_mNr->text().toStdString());
    this->p8realisation->setParameterValue("RealisationNr",path.toStdString() + "/" + ui->comboBox->currentText().toStdString());
}
