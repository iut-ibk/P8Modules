#ifndef P8SCENARIO_GUI_H
#define P8SCENARIO_GUI_H

#include <QDialog>

class P8Scenario;

namespace Ui {
class P8Scenario_GUI;
}

class P8Scenario_GUI : public QDialog
{
    Q_OBJECT
    
public:
    explicit P8Scenario_GUI(P8Scenario * p8,QWidget *parent = 0);
    ~P8Scenario_GUI();
    
private slots:
    void on_buttonBox_accepted();

    void on_pb_ui_delinblocks_released();

    void on_pb_ui_urbplanbb_released();

    void on_pb_ui_techplacement_released();

private:
    Ui::P8Scenario_GUI *ui;
    P8Scenario * p8scenario;


};

#endif // P8BASELINE_GUI_H
