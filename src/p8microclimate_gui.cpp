#include "p8microclimate_gui.h"
#include "ui_p8microclimate_gui.h"
#include "p8microclimate.h"

p8microclimate_gui::p8microclimate_gui(Microclimate * p8, QWidget *parent) :
    QDialog(parent),
    ui(new Ui::p8microclimate_gui)
{
    ui->setupUi(this);
    this->p8microclimate = p8;

}

p8microclimate_gui::~p8microclimate_gui()
{
    delete ui;
}
