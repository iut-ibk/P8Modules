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
     double total;
     Ui::CellDialog_heat *ui;


public slots:
private slots:
     void on_v1_valueChanged(double arg1);
     void on_v2_valueChanged(double arg1);
     void on_v3_valueChanged(double arg1);
     void on_v4_valueChanged(double arg1);
     void on_v5_valueChanged(double arg1);
     void on_v6_valueChanged(double arg1);
     void on_v7_valueChanged(double arg1);
     void on_v8_valueChanged(double arg1);
     void on_v9_valueChanged(double arg1);
     void on_v10_valueChanged(double arg1);
     void on_v11_valueChanged(double arg1);
     void on_v12_valueChanged(double arg1);
     void on_v13_valueChanged(double arg1);
     void on_v14_valueChanged(double arg1);
     void on_v15_valueChanged(double arg1);
     void getTotal();
     void on_buttonBox_accepted();
};

#endif // CELLDIALOG_HEAT_H
