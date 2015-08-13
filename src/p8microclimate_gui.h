#ifndef P8MICROCLIMATE_GUI_H
#define P8MICROCLIMATE_GUI_H

#include <QDialog>

#include "p8microclimate.h"
#include "ui_p8microclimate_gui.h"
class mcedit;
namespace Ui {
class p8microclimate_gui;
}

class p8microclimate_gui : public QDialog
{
    Q_OBJECT

public:
    explicit p8microclimate_gui(Microclimate * p8,QWidget *parent = 0);
    QList<QList<double> > getTec();
    void setTec(QList<QList<double> >);
    ~p8microclimate_gui();
    void set_run();

private slots:
    void on_pb_map_released();
    void on_pb_shape_released();
    void on_pb_landuse_released();

    void on_bBox_accepted();

    void on_pb_wsud_released();


    void on_pb_placeTech_released();

private:
    Ui::p8microclimate_gui *ui;
    Microclimate *p8microclimate;
    mcedit * edit;
    int oldGridsize;
};

#endif // P8MICROCLIMATE_GUI_H
