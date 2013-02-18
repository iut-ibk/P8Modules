/*
#ifndef P8EVALUATION_GUI_H
#define P8EVALUATION_GUI_H

#include <QDialog>

class P8Evaluation;

namespace Ui {
class P8Evaluation_GUI;
}

class P8Evaluation_GUI : public QDialog
{
    Q_OBJECT
    
public:
    explicit P8Evaluation_GUI(P8Evaluation * p8,QWidget *parent = 0);
    ~P8Evaluation_GUI();
    
private slots:
    void on_buttonBox_accepted();

    void on_pb_ui_delinblocks_released();

    void on_pb_ui_urbplanbb_released();

    void on_pb_ui_techplacement_released();

private:
    Ui::P8Evaluation_GUI *ui;
    P8Evaluation * p8evaluation;


};

#endif // P8BASELINE_GUI_H
*/
