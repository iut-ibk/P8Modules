#ifndef P8BASELINE_GUI_H
#define P8BASELINE_GUI_H

#include <QDialog>

class URBAN_FORM;

namespace Ui {
class URBAN_FORM_GUI;
}

class URBAN_FORM_GUI : public QDialog
{
    Q_OBJECT
    
public:
    explicit URBAN_FORM_GUI(URBAN_FORM * p8,QWidget *parent = 0);
    ~URBAN_FORM_GUI();
    
private slots:
    /*
      catchment     = c
      soil          = s
      topo          = t*
      plamMap       = p
      popdensity    = d*
      landuse       = l
      */
    void on_pb_c_released();
    void on_pb_s_released();
    void on_pb_t_released();
    void on_pb_p_released();
    void on_pb_d_released();
    void on_pb_l_released();

    void on_sb_gs_editingFinished();

    void on_buttonBox_accepted();

private:
    Ui::URBAN_FORM_GUI *ui;
    URBAN_FORM * p8baseline;


};

#endif // P8BASELINE_GUI_H
