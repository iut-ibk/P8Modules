#ifndef P8REALISATION2_GUI_H
#define P8REALISATION2_GUI_H

#include <QDialog>
//class Realisation2;

#include "p8realisation2.h"
#include "ui_p8realisation2_gui.h"


namespace Ui {
class p8realisation2_gui;
}

class p8realisation2_gui : public QDialog
{
    Q_OBJECT
    
public:
    explicit p8realisation2_gui(Current_Realisation2 * p8, QWidget *parent = 0);


    ~p8realisation2_gui();



private slots:
    void on_buttonBox_accepted();


private:
    Ui::p8realisation2_gui *ui;
    Current_Realisation2 *p8realisation;
};

#endif // P8REALISATION2_GUI_H


