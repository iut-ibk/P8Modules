#ifndef MCEDIT_HEAT_H
#define MCEDIT_HEAT_H

#include <QDialog>
#include <QMap>
#include <QPixmap>
#include <QList>

class McGraphicsScene;
class QGraphicsRectItem;
class Cell_heat;
class QGraphicsItem;
class QGraphicsSceneMouseEvent;
class QColor;
class p8microclimate_heat_gui;
class QGraphicsSimpleTextItem;
namespace Ui {
class mcedit_heat;
}

class mcedit_heat : public QDialog
{
    Q_OBJECT
    
public:
    explicit mcedit_heat(p8microclimate_heat_gui *parent, QString bgimage, QString workpath, int cx, int cy, double sx, double sy);
    ~mcedit_heat();
    void mousemove(QGraphicsSceneMouseEvent* event);
    void mousepress(QGraphicsSceneMouseEvent* event);
    void mouserelease(QGraphicsSceneMouseEvent* event);
    void mousedoubleclick(QGraphicsSceneMouseEvent* event);

    void tecLoad();
    void tecSave();
    void tecSaveAs();
    void tecSave(QString filename);
    void tecSave(p8microclimate_heat_gui *parent);
    void tecLoad(p8microclimate_heat_gui *parent);
    void tecLoad(QString tfilename);
    void cellupdate();
    void changebgcont(int c);
    void resLoad(int no, QString tfilename);
    void zoomin();
    void zoomout();
    void loadbackground(QString bgfilename);
    void setScale(double startTemp, double endTemp, int colorramp);
    int getMinValue(int mode);
    int getMaxValue(int mode);
    int getMinValueForLstAfterBefore();
    int getMaxValueForLstAfterBefore();

    QColor getColor(double startTemp, double endTemp, double temp, int colorramp);

private slots:
    void on_pb_zoomin_clicked();
    void on_pb_zoomout_clicked();
    void on_pb_load_clicked();
    void on_pb_saveas_clicked();
    void on_pb_save_clicked();
    void on_pb_clear_clicked();
    void on_pb_edit_clicked();
    void on_cb_mode_currentIndexChanged(int index);
    void on_horizontalSlider_valueChanged(int value);
    void on_comboBox_currentIndexChanged(int index);    
    void on_buttonBox_accepted();
    void on_rb_edit_toggled(bool checked);
    void on_pb_zoomout_2_clicked();
    void on_pushButton_clicked();

private:
    p8microclimate_heat_gui *parent;
    QString filename;
    Ui::mcedit_heat *ui;
    McGraphicsScene *scene;
    QMap<QGraphicsRectItem*,Cell_heat*> cellmap;
    QPixmap pixmap;
    int cx;
    int cy;
    double sx;
    double sy;
    int mode;
    int viewmode;
    QList<QColor*> teccol;
    QGraphicsRectItem *bgrect;
    QString workpath;
    QList<QGraphicsRectItem *> scaleboxes;
    QGraphicsSimpleTextItem* scalestart;
    QGraphicsSimpleTextItem* scaleend;
    QGraphicsSimpleTextItem* scaletitle;
    int scaleposx;
    int scaleposy;
    int scalehight;
    int scalelength;
    int scalesteps;

};

#endif // MCEDIT_HEAT_H
