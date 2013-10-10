#include "mcgraphicscene.h"

#include "mcedit.h"

McGraphicsScene::McGraphicsScene(mcedit *parent) :
    QGraphicsScene((QObject*)parent)
{
    this->parent=parent;
}

void McGraphicsScene::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
{
    parent->mousemove(event);
}

void McGraphicsScene::mousePressEvent(QGraphicsSceneMouseEvent *event)
{
    parent->mousepress(event);
}

void McGraphicsScene::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
{
    parent->mouserelease(event);
}
