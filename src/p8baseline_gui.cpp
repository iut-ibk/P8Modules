#include "p8baseline_gui.h"
#include "ui_p8baseline_gui.h"
#include "p8baseline.h"
#include <QFileDialog>

P8BaseLine_GUI::P8BaseLine_GUI(P8BaseLine * p8, QWidget *parent) :
    QDialog(parent),
    ui(new Ui::P8BaseLine_GUI)
{
    ui->setupUi(this);
    this->p8baseline = p8;


}

P8BaseLine_GUI::~P8BaseLine_GUI()
{
    delete ui;
}

void P8BaseLine_GUI::on_pushButton_load_released()
{
    QString fname = QFileDialog::getOpenFileName();
    this->p8baseline->createShape(fname.toStdString());
}
