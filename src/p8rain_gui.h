#ifndef P8RAIN_GUI_H
#define P8RAIN_GUI_H

#include <QDialog>

class P8Rain;

namespace Ui {
class P8Rain_GUI;
}

class P8Rain_GUI : public QDialog
{
    Q_OBJECT
    
public:
    explicit P8Rain_GUI(P8Rain * p8,QWidget *parent = 0);
    ~P8Rain_GUI();
    
private slots:
    void on_pb_r_released();

private:
    Ui::P8Rain_GUI *ui;
    P8Rain * p8rain;
};

#endif // P8RAIN_GUI_H
