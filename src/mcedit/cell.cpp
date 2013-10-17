#include "cell.h"
#include <QGraphicsScene>
#include <QGraphicsRectItem>
#include <QGraphicsEllipseItem>
#include <cmath>
#include <QColor>

#include "celldialog.h"


Cell::Cell(double px, double py, double sx, double sy, QGraphicsScene *scene, int no,QList<QColor*>* teccol)
{
    this->scene=scene;
    this->teccol=teccol;
    circ=scene->addEllipse(QRectF(px, py, sx, sy));
    rect=scene->addRect(QRectF(px, py, sx, sy));
    /*
int techcountrand=rand()%100;
    int techcount=0;
    if (techcountrand>50)
        techcount=1;
    else if (techcountrand>90)
        techcount=2;



    for (int i=0;i<6;i++)
        v[i]=0;
    for (int i=0;i<techcount;i++)
        v[rand()%6]=rand()%100;

    for (int i=0;i<1;i++)
        if (rand()%10>2)
            res[i]=double(rand()%51-25)/10.0;
        else
            res[i]=0;
    */
    for (int i=0;i<6;i++)
        v[i]=0;
    for (int i=0;i<1;i++)
        res[i]=0;

    this->no=no;
    this->px=px;
    this->py=py;
    this->sx=sx;
    this->sy=sy;
    selected=false;

    QPen circpen;
    circpen.setColor(QColor(0,0,0,0));
    circ->setPen(circpen);

    //circ=NULL;
}

void Cell::editVals()
{
    CellDialog dia(NULL,&v[0],&v[1],&v[2],&v[3],&v[4],&v[5]);
    dia.exec();
}

QGraphicsRectItem *Cell::getRect()
{
    return rect;
}

void Cell::update(int mode,int viewmode)
{   
    QBrush brush;
    brush.setStyle(Qt::SolidPattern);
    brush.setColor(QColor(0,0,0,0));

    QBrush circbrush;
    circbrush.setStyle(Qt::SolidPattern);
    circbrush.setColor(QColor(0,0,0,0));


    if (mode==0)
    {
        if (selected)
            brush.setColor(QColor(200,200,200,96));

        double r=0;
        double g=0;
        double b=0;
        double techcover=0;
        for (int i=0;i<6;i++)
        {
            r+=(*teccol)[i]->redF()*v[i]/100.0;
            g+=(*teccol)[i]->greenF()*v[i]/100.0;
            b+=(*teccol)[i]->blueF()*v[i]/100.0;
            techcover+=v[i];
        }
        if (r>1)
            r=1;
        if (g>1)
            g=1;
        if (b>1)
            b=1;

        if (techcover>100)
            techcover=100;
        double dx=(100-techcover)*(sx/100.0)/2.0;
        double dy=(100-techcover)*(sy/100.0)/2.0;

        circ->setRect(QRectF(px+dx, py+dy, sx-(2*dx), sy-(2*dy)));
        if (viewmode==0)
            circbrush.setColor(QColor(255.0*r,255.0*g,255.0*b,127));
        else
            brush.setColor(QColor(255.0*r,255.0*g,255.0*b,techcover));
    }
    if (mode==1)
    {
        double maxdt=0.5;
        int col=255.0*fabs(res[0]/maxdt);
        if (res[0]>0)
            brush.setColor(QColor(255,255-col,255-col,127));
        if (res[0]<0)
            brush.setColor(QColor(255-col,255-col,255,127));
    }
    rect->setBrush(brush);
    circ->setBrush(circbrush);
}

double Cell::getRes(int p)
{
    return res[p];
}

void Cell::setRes(int p, double v_)
{
    res[p]=v_;
}


double Cell::getV(int p)
{
    return v[p];
}

void Cell::setV(int p, double v_)
{
    v[p]=v_;
}

double Cell::getPx()
{
    return px;
}

double Cell::getPy()
{
    return py;
}

bool Cell::getSelected()
{
    return selected;
}

void Cell::setSelected(bool b)
{
    selected=b;
}

int Cell::getNo()
{
    return no;
}

void Cell::setNo(int nn)
{
    no=nn;
}

