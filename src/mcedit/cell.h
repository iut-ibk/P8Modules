#ifndef CELL_H
#define CELL_H

class QGraphicsRectItem;
class QGraphicsScene;
class QColor;
class QGraphicsEllipseItem;

#include <QList>

class Cell
{
public:
    Cell(double px, double py, double sx, double sy, QGraphicsScene *scene,int no, QList<QColor*>* teccol);
    void editVals();
    QGraphicsRectItem *getRect();
    void update(int mode,int viewmode);
    double getRes(int p);
    double getV(int p);
    void setV(int p, double v_);
    double getPx();
    double getPy();
    bool getSelected();
    void setSelected(bool b);
    int getNo();
    void setNo(int nn);


protected:
    double v[6];
    double res[1];
    int no;
    bool selected;
    int px;
    int py;
    int sx;
    int sy;

    QGraphicsScene *scene;
    QGraphicsEllipseItem *circ;
    QGraphicsRectItem *rect;
    QList<QColor*> *teccol;

};

#endif // CELL_H
