#include "p8scenario_gui.h"
#include "ui_p8scenario_gui.h"
#include "p8scenario.h"
#include <QFileDialog>

SCENARIO_GUI::SCENARIO_GUI(SCENARIO * p8, QWidget *parent) :
    QDialog(parent),
    ui(new Ui::SCENARIO_GUI)
{
    ui->setupUi(this);
    this->p8scenario = p8;
}

SCENARIO_GUI::~SCENARIO_GUI()
{
    delete ui;
}


void SCENARIO_GUI::on_buttonBox_accepted()
{
}

void SCENARIO_GUI::on_pb_ui_delinblocks_released()
{
    this->p8scenario->open_ui_delinblocks();
}

void SCENARIO_GUI::on_pb_ui_urbplanbb_released()
{
    this->p8scenario->open_ui_urbplanbb();
}

void SCENARIO_GUI::on_pb_ui_techplacement_released()
{
    this->p8scenario->open_ui_techplacement();
}
