#ifndef CELL_H
#define CELL_H

class QGraphicsRectItem;
class QGraphicsScene;
class QGraphicsView;
class QColor;
class QGraphicsEllipseItem;

#include <QList>

class Cell
{
public:
    Cell(double px, double py, double sx, double sy, QGraphicsScene *scene, QGraphicsView *view, int no, QList<QColor*>* teccol);
    void editVals();
    QGraphicsRectItem *getRect();
    void update(int mode,int viewmode);
    double getRes(int p);
    void setRes(int p, double v_);
    double getV(int p);
    void setV(int p, double v_);
    double getPx();
    double getPy();
    bool getSelected();
    void setSelected(bool b);
    int getNo();
    void setNo(int nn);


protected:
    double v[11];
    double res[3];
    int no;
    bool selected;
    int px;
    int py;
    int sx;
    int sy;

    QGraphicsScene *scene;
    QGraphicsView *view;
    QGraphicsEllipseItem *circ;
    QGraphicsRectItem *rect;
    QList<QColor*> *teccol;

};

#endif // CELL_H
