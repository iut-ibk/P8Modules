#include "mainwindow.h"
#include "ui_mainwindow.h"

#include "mcedit.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
    edit=new mcedit(NULL,ui->awidth->value()/30,ui->aheight->value()/30,30,30);
    edit->show();
}

void MainWindow::on_actionExit_triggered()
{
    exit(0);
}
