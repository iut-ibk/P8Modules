#ifndef P8SCENARIO_GUI_H
#define P8SCENARIO_GUI_H

#include <QDialog>

class SCENARIO;

namespace Ui {
class SCENARIO_GUI;
}

class SCENARIO_GUI : public QDialog
{
    Q_OBJECT
    
public:
    explicit SCENARIO_GUI(SCENARIO * p8,QWidget *parent = 0);
    ~SCENARIO_GUI();
    
private slots:
    void on_buttonBox_accepted();

    void on_pb_ui_delinblocks_released();

    void on_pb_ui_urbplanbb_released();

    void on_pb_ui_techplacement_released();

private:
    Ui::SCENARIO_GUI *ui;
    SCENARIO * p8scenario;


};

#endif // P8BASELINE_GUI_H
