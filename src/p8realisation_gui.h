#ifndef P8REALISATION_GUI_H
#define P8REALISATION_GUI_H

#include <QDialog>
//class Realisations;

#include "p8realisations.h"
#include "ui_p8realisation_gui.h"


namespace Ui {
class p8realisation_gui;
}

class p8realisation_gui : public QDialog
{
    Q_OBJECT
    
public:
    explicit p8realisation_gui(Realisations * p8, QWidget *parent = 0);


    ~p8realisation_gui();



private slots:
    void on_buttonBox_accepted();


private:
    Ui::p8realisation_gui *ui;
    Realisations *p8realisation;
};

#endif // P8REALISATION_GUI_H


