#ifndef P8MICROCLIMATE_GUI_H
#define P8MICROCLIMATE_GUI_H

#include <QDialog>

#include "p8microclimate.h"
#include "ui_p8microclimate_gui.h"

namespace Ui {
class p8microclimate_gui;
}

class p8microclimate_gui : public QDialog
{
    Q_OBJECT

public:
    explicit p8microclimate_gui(Microclimate * p8,QWidget *parent = 0);

    ~p8microclimate_gui();

private slots:
    void on_pb_map_released();
    void on_pb_shape_released();
    void on_pb_landuse_released();

    void on_bBox_accepted();

private:
    Ui::p8microclimate_gui *ui;
    Microclimate *p8microclimate;
};

#endif // P8MICROCLIMATE_GUI_H
