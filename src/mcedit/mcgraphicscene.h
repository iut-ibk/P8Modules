#ifndef MCGRAPHICSSCENE_H
#define MCGRAPHICSSCENE_H

#include <QGraphicsScene>

class mcedit;

class McGraphicsScene : public QGraphicsScene
{
    Q_OBJECT
public:
    explicit McGraphicsScene(mcedit *parent);

signals:
    
public slots:
    void mouseMoveEvent(QGraphicsSceneMouseEvent* event);
    void mousePressEvent(QGraphicsSceneMouseEvent* event);
    void mouseReleaseEvent(QGraphicsSceneMouseEvent* event);
protected:
    mcedit *parent;
};

#endif // MCGRAPHICSSCENE_H
