#ifndef MCGRAPHICSSCENE_H
#define MCGRAPHICSSCENE_H

#include <QGraphicsScene>

class mcedit;
class mcedit_heat;

class McGraphicsScene : public QGraphicsScene
{
    Q_OBJECT
public:
    explicit McGraphicsScene(mcedit *parent);
    explicit McGraphicsScene(mcedit_heat *parent);

signals:
    
public slots:
    void mouseMoveEvent(QGraphicsSceneMouseEvent* event);
    void mousePressEvent(QGraphicsSceneMouseEvent* event);
    void mouseReleaseEvent(QGraphicsSceneMouseEvent* event);
protected:
    mcedit *parent;
    mcedit_heat *parent_heat;
};

#endif // MCGRAPHICSSCENE_H
