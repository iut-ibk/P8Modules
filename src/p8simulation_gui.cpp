/*
#include "p8simulation_gui.h"
#include "ui_p8simulation_gui.h"
#include "p8simulation.h"
#include <QFileDialog>

P8Simulation_GUI::P8Simulation_GUI(P8Simulation * p8, QWidget *parent) :
    QDialog(parent),
    ui(new Ui::P8Simulation_GUI)
{
    ui->setupUi(this);
    this->P8simulation = p8;
}

P8Simulation_GUI::~P8Simulation_GUI()
{
    delete ui;
}


void P8Simulation_GUI::on_buttonBox_accepted()
{
}

void P8Simulation_GUI::on_pb_ui_delinblocks_released()
{
    this->P8Simulation->open_ui_delinblocks();
}

void P8Simulation_GUI::on_pb_ui_urbplanbb_released()
{
    this->P8Simulation->open_ui_urbplanbb();
}

void P8Simulation_GUI::on_pb_ui_techplacement_released()
{
    this->P8Simulation->open_ui_techplacement();
}
*/
