#ifndef CELLDIALOG_HEAT_H
#define CELLDIALOG_HEAT_H

#include <QDialog>

namespace Ui {
class CellDialog_heat;
}

class CellDialog_heat : public QDialog
{
    Q_OBJECT
    
public:
    explicit CellDialog_heat(QWidget *parent,double *v1,double *v2,double *v3,double *v4,double *v5,double *v6,double *v7,double *v8,double *v9,double *v10,double *v11,double *v12,double *v13,double *v14,double *v15);
    ~CellDialog_heat();
     void closeEvent(QCloseEvent * ev);
     void getValues(double *v1,double *v2,double *v3,double *v4,double *v5,double *v6,double *v7,double *v8,double *v9,double *v10,double *v11,double *v12,double *v13,double *v14,double *v15);

private:
     double *v1;
     double *v2;
     double *v3;
     double *v4;
     double *v5;
     double *v6;
     double *v7;
     double *v8;
     double *v9;
     double *v10;
     double *v11;
     double *v12;
     double *v13;
     double *v14;
     double *v15;

     Ui::CellDialog_heat *ui;


public slots:
};

#endif // CELLDIALOG_HEAT_H
