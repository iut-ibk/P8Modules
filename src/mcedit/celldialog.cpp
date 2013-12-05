#include "celldialog.h"
#include "ui_celldialog.h"


#include <QCloseEvent>

CellDialog::CellDialog(QWidget *parent,double *v1,double *v2,double *v3,double *v4,double *v5,double *v6,double *v7,double *v8,double *v9,double *v10,double *v11) :
    QDialog(parent),
    ui(new Ui::CellDialog)
{
    ui->setupUi(this);

    this->v1=v1;
    this->v2=v2;
    this->v3=v3;
    this->v4=v4;
    this->v5=v5;
    this->v6=v6;
    this->v7=v7;
    this->v8=v8;
    this->v9=v9;
    this->v10=v10;
    this->v11=v11;
    ui->v1->setValue(*v1);
    ui->v2->setValue(*v2);
    ui->v3->setValue(*v3);
    ui->v4->setValue(*v4);
    ui->v5->setValue(*v5);
    ui->v6->setValue(*v6);
    ui->v7->setValue(*v7);
    ui->v8->setValue(*v8);
    ui->v9->setValue(*v9);
    ui->v10->setValue(*v10);
    ui->v11->setValue(*v11);
}



CellDialog::~CellDialog()
{
    *v1=ui->v1->value();
    *v2=ui->v2->value();
    *v3=ui->v3->value();
    *v4=ui->v4->value();
    *v5=ui->v5->value();
    *v6=ui->v6->value();
    *v7=ui->v7->value();
    *v8=ui->v8->value();
    *v9=ui->v9->value();
    *v10=ui->v10->value();
    *v11=ui->v11->value();
    delete ui;
}

void CellDialog::closeEvent(QCloseEvent *ev)
{
/*
    if (ev->isAccepted());
    {
        *v1=ui->v1->value();
        *v2=ui->v2->value();
        *v3=ui->v3->value();
        *v4=ui->v4->value();
        *v5=ui->v5->value();
        *v6=ui->v6->value();
    }
    */
}

void CellDialog::getValues(double *v1,double *v2,double *v3,double *v4,double *v5,double *v6,double *v7,double *v8,double *v9,double *v10,double *v11)
{
    *v1=ui->v1->value();
    *v2=ui->v2->value();
    *v3=ui->v3->value();
    *v4=ui->v4->value();
    *v5=ui->v5->value();
    *v6=ui->v6->value();
    *v7=ui->v7->value();
    *v8=ui->v8->value();
    *v9=ui->v9->value();
    *v10=ui->v10->value();
    *v11=ui->v11->value();
}
