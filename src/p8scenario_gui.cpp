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
    this->p8scenario->createCityBlocksFromShape(ui->sb_gs->value(), ui->sb_gs->value());
}

void P8Scenario_GUI::on_pb_ui_delimblocks_released()
{
    this->p8scenario->open_ui_delimblocks();
}
