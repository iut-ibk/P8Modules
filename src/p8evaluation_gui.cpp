/*
#include "p8evaluation_gui.h"
#include "ui_p8evaluation_gui.h"
#include "p8evaluation.h"
#include <QFileDialog>


P8Evaluation_GUI::P8Evaluation_GUI(P8Evaluation * p8, QWidget *parent) :
    QDialog(parent),
    ui(new Ui::P8Evaluation_GUI)
{
    ui->setupUi(this);
    this->p8evaluation = p8;
}

P8Evaluation_GUI::~P8Evaluation_GUI()
{
    delete ui;
}


void P8Evaluation_GUI::on_buttonBox_accepted()
{
}

void P8Evaluation_GUI::on_pb_ui_delinblocks_released()
{
    this->p8evaluation->open_ui_delinblocks();
}

void P8Evaluation_GUI::on_pb_ui_urbplanbb_released()
{
    this->p8evaluation->open_ui_urbplanbb();
}

void P8Evaluation_GUI::on_pb_ui_techplacement_released()
{
    this->p8evaluation->open_ui_techplacement();
}
*/
