#ifndef MCEDIT_H
#define MCEDIT_H

#include <QDialog>
#include <QMap>
#include <QPixmap>
#include <QList>

class McGraphicsScene;
class QGraphicsRectItem;
class Cell;
class QGraphicsItem;
class QGraphicsSceneMouseEvent;
class QColor;
class p8microclimate_gui;
namespace Ui {
class mcedit;
}

class mcedit : public QDialog
{
    Q_OBJECT
    
public:
    explicit mcedit(p8microclimate_gui *parent, QString bgimage, QString workpath, int cx, int cy, double sx, double sy);
    ~mcedit();
    void mousemove(QGraphicsSceneMouseEvent* event);
    void mousepress(QGraphicsSceneMouseEvent* event);
    void mouserelease(QGraphicsSceneMouseEvent* event);
    void tecLoad();
    void tecSave();
    void tecSaveAs();
    void tecSave(QString filename);
    void tecSave(p8microclimate_gui *parent);
    void tecLoad(p8microclimate_gui *parent);
    void tecLoad(QString tfilename);
    void cellupdate();
    void changebgcont(int c);
    void resLoad(QString tfilename);
    void zoomin();
    void zoomout();
    void loadbackground(QString bgfilename);

private slots:
    void on_pb_zoomin_clicked();
    void on_pb_zoomout_clicked();
//    void on_pushButton_clicked();
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

private:
    p8microclimate_gui *parent;
    QString filename;
    Ui::mcedit *ui;
    McGraphicsScene *scene;
    QMap<QGraphicsRectItem*,Cell*> cellmap;
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
};

#endif // MCEDIT_H
