#include "p8scenario_gui.h"
#include "ui_p8scenario_gui.h"
#include "p8scenario.h"
#include <QFileDialog>

P8Scenario_GUI::P8Scenario_GUI(P8Scenario * p8, QWidget *parent) :
    QDialog(parent),
    ui(new Ui::P8Scenario_GUI)
{
    ui->setupUi(this);
    this->p8scenario = p8;
}

P8Scenario_GUI::~P8Scenario_GUI()
{
    delete ui;
}


void P8Scenario_GUI::on_buttonBox_accepted()
{
}

void P8Scenario_GUI::on_pb_ui_delinblocks_released()
{
    this->p8scenario->open_ui_delinblocks();
}

void P8Scenario_GUI::on_pb_ui_urbplanbb_released()
{
    this->p8scenario->open_ui_urbplanbb();
}

void P8Scenario_GUI::on_pb_ui_techplacement_released()
{
    this->p8scenario->open_ui_techplacement();
}
