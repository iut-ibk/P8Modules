#include "mcgraphicscene.h"

#include <QGraphicsSceneMouseEvent>

#include "mcedit.h"
#include "mcedit_heat.h"

McGraphicsScene::McGraphicsScene(mcedit *parent) :
    QGraphicsScene((QObject*)parent)
{
    this->parent=parent;
    this->parent_heat = 0;
}
McGraphicsScene::McGraphicsScene(mcedit_heat *parent) :
    QGraphicsScene((QObject*)parent)
{
    this->parent_heat=parent;
    this->parent = 0;
}

void McGraphicsScene::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
{
    if(parent != 0)
        parent->mousemove(event);
    else
        parent_heat->mousemove(event);
}

void McGraphicsScene::mousePressEvent(QGraphicsSceneMouseEvent *event)
{
    if(parent != 0)
        parent->mousepress(event);
    else
        parent_heat->mousepress(event);
}

void McGraphicsScene::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
{
    if(parent != 0)
        parent->mouserelease(event);
    else
        parent_heat->mouserelease(event);
}

void McGraphicsScene::mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event)
{
    if(parent != 0)
        parent->mousedoubleclick(event);
    else
        parent_heat->mousedoubleclick(event);
}
