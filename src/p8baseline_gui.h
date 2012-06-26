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
    void on_pushButton_load_released();

private:
    Ui::P8BaseLine_GUI *ui;
    P8BaseLine * p8baseline;


};

#endif // P8BASELINE_GUI_H
