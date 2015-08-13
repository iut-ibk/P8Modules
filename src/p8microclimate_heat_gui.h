#ifndef P8MICROCLIMATE_HEAT_GUI_H
#define P8MICROCLIMATE_HEAT_GUI_H

#include <QDialog>

#include "p8microclimate_heat.h"
#include "ui_p8microclimate_heat_gui.h"
class mcedit_heat;
namespace Ui {
class p8microclimate_heat_gui;
}

class p8microclimate_heat_gui : public QDialog
{
    Q_OBJECT

public:
    explicit p8microclimate_heat_gui(Microclimate_heat * p8,QWidget *parent = 0);
    QList<QList<double> > getTec();
    void setTec(QList<QList<double> >);
    ~p8microclimate_heat_gui();
    void set_run();


private slots:
    void on_pb_map_released();
    void on_pb_shape_released();
    void on_pb_landuse_released();
    void on_bBox_accepted();

    void on_pb_wsud_released();


    void on_pb_placeTech_released();

    void on_pb_techFile_released();

private:
    Ui::p8microclimate_heat_gui *ui;
    Microclimate_heat *p8microclimate;
    mcedit_heat * edit;
    int oldGridsize;

};

#endif // P8MICROCLIMATE_GUI_H
