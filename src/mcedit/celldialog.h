#ifndef CELLDIALOG_H
#define CELLDIALOG_H

#include <QDialog>

namespace Ui {
class CellDialog;
}

class CellDialog : public QDialog
{
    Q_OBJECT
    
public:
    explicit CellDialog(QWidget *parent,double *v1,double *v2,double *v3,double *v4,double *v5,double *v6,double *v7,double *v8,double *v9,double *v10,double *v11);
    ~CellDialog();
     void closeEvent(QCloseEvent * ev);
     void getValues(double *v1,double *v2,double *v3,double *v4,double *v5,double *v6,double *v7,double *v8,double *v9,double *v10,double *v11);

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
     Ui::CellDialog *ui;


public slots:
};

#endif // CELLDIALOG_H
