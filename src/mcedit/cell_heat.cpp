#include "cell_heat.h"
#include <QGraphicsScene>
#include <QGraphicsView>
#include <QGraphicsRectItem>
#include <QGraphicsEllipseItem>
#include <cmath>
#include <QColor>

#include "celldialog_heat.h"


Cell_heat::Cell_heat(double px, double py, double sx, double sy, QGraphicsScene *scene, QGraphicsView *view, int no,QList<QColor*>* teccol)
{
    this->scene=scene;
    this->view=view;
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
    for (int i=0;i<15;i++)
        v[i]=0;
    for (int i=0;i<3;i++)
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

void Cell_heat::editVals()
{
    CellDialog_heat dia(NULL,&v[0],&v[1],&v[2],&v[3],&v[4],&v[5],&v[6],&v[7],&v[8],&v[9],&v[10],&v[11],&v[12],&v[13],&v[14]);
    dia.exec();
}

QGraphicsRectItem *Cell_heat::getRect()
{
    return rect;
}

void Cell_heat::update(int mode,int viewmode)
{   
    QPen pen;
    pen.setColor(QColor(0,0,0,255));

    QBrush brush;
    brush.setStyle(Qt::SolidPattern);
    brush.setColor(QColor(0,0,0,0));

    QBrush circbrush;
    circbrush.setStyle(Qt::SolidPattern);
    circbrush.setColor(QColor(0,0,0,0));


    if (mode==0)
    {
        double r=0;
        double g=0;
        double b=0;
        double techcover=0;
        for (int i=0;i<15;i++)
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
        if (view->transform().m11()<0.25)
            pen.setColor(QColor(0,0,0,0));
    }
    if (mode==1) // lst change
    {
        double maxdt=20;
        int col=255.0*fabs((res[0])/maxdt);
        int alpha = 127;
        if(col > 255)
        {
            col = 255;
            alpha = 220;
        }
        if (res[0]>0)
            brush.setColor(QColor(255,255-col,255-col,alpha));
        if (res[0]<0)
            brush.setColor(QColor(255-col,255-col,255,alpha));
        if (view->transform().m11()<0.25)
            pen.setColor(QColor(0,0,0,0));
    }
    if (mode==2) // lst before wusd
    {
        double maxdt=20;
        int col=255.0*fabs((res[1]-20)/maxdt);
        if (res[1]>0)
            brush.setColor(QColor(255,255-col,255-col,127));
        if (res[1]<0)
            brush.setColor(QColor(255-col,255-col,255,127));
        if (view->transform().m11()<0.25)
            pen.setColor(QColor(0,0,0,0));
    }
    if (mode==3) // lst after wusd
    {
        double maxdt=20;
        int col=255.0*fabs((res[2]-20)/maxdt);
        if (res[2]>0)
            brush.setColor(QColor(255,255-col,255-col,127));
        if (res[2]<0)
            brush.setColor(QColor(255-col,255-col,255,127));
        if (view->transform().m11()<0.25)
            pen.setColor(QColor(0,0,0,0));
    }

    if (selected)
        brush.setColor(QColor(200,200,200,96));

    rect->setPen(pen);
    rect->setBrush(brush);
    circ->setBrush(circbrush);
}

double Cell_heat::getRes(int p)
{
    return res[p];
}

void Cell_heat::setRes(int p, double v_)
{
    res[p]=v_;
}


double Cell_heat::getV(int p)
{
    return v[p];
}

void Cell_heat::setV(int p, double v_)
{
    v[p]=v_;
}

double Cell_heat::getPx()
{
    return px;
}

double Cell_heat::getPy()
{
    return py;
}

bool Cell_heat::getSelected()
{
    return selected;
}

void Cell_heat::setSelected(bool b)
{
    selected=b;
}

int Cell_heat::getNo()
{
    return no;
}

void Cell_heat::setNo(int nn)
{
    no=nn;
}

