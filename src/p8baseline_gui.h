#ifndef P8BASELINE_GUI_H
#define P8BASELINE_GUI_H

#include <QDialog>

class P8BaseLine;

namespace Ui {
class P8BaseLine_GUI;
}

class P8BaseLine_GUI : public QDialog
{
    Q_OBJECT
    
public:
    explicit P8BaseLine_GUI(P8BaseLine * p8,QWidget *parent = 0);
    ~P8BaseLine_GUI();
    
private slots:
    void on_pb_c_released();

    void on_pb_e_released();

    void on_pb_s_released();

    void on_pb_p_released();

    void on_pb_l_released();

    void on_sb_gs_editingFinished();

    void on_buttonBox_accepted();

private:
    Ui::P8BaseLine_GUI *ui;
    P8BaseLine * p8baseline;


};

#endif // P8BASELINE_GUI_H
