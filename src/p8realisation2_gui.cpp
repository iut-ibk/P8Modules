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
    QString path = QString(this->p8realisation->getWorkPath());
    QDir dir = QDir(path);
    dir.setFilter(QDir::Files);
    QStringList files = dir.entryList();
    QList<QBool> fileIsSplit = QList<QBool>();
    for (int i = 0; i<files.length()+1; i++)
    {
        fileIsSplit.append(QBool(false));
    }
    int length = files.length();
    for(int i = 0;i<length;i++)
    {
        if(files.at(i).contains("Bas"))
        {
            int nr = QChar(files.at(i).at(10)).digitValue();
            fileIsSplit[nr] = QBool(true);
        }

        if(!files[i].contains("ubMUSIC-ID"))
        {
            files.removeAt(i);
            i--;
            length--;
        }

    }
    for(int i = 0;i<length;i++)
    {
        int number = QChar(files.at(i).at(10)).digitValue();
        bool b = fileIsSplit.at(number);
        if(b)
        {
            if(!files.at(i).contains("Bas"))
            {
                files.removeAt(i);
                i--;
                length--;
            }
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
    QString path = QString(this->p8realisation->getWorkPath());
        //this->p8realisation->setParameterValue("RealisationNr",ui->le_mNr->text().toStdString());
    this->p8realisation->setParameterValue("RealisationNr",path.toStdString() + "/" + ui->comboBox->currentText().toStdString());
}
