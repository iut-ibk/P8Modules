/**
 * @file
 * @author  Chrisitan Urich <christian.urich@gmail.com>
 * @version 1.0
 * @section LICENSE
 *
 * This file is part of DynaMind
 *
 * Copyright (C) 2011  Christian Urich
 
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 *
 */

#include "graphicplacement.h"
#include <dm.h>
#include <dmview.h>
#include <dmlogger.h>

#include <cmath>
#ifndef M_PI
#define M_PI        3.14159265358979323846
#endif
//Creates a Block with 1 per 1 meter






DM_DECLARE_NODE_NAME( GraphicPlacement,CRCP8 )
GraphicPlacement::GraphicPlacement()
{
    std::vector<DM::View> views;
    block = DM::View("GraphicPlacement", DM::FACE, DM::WRITE);
    block.addAttribute("Color");
    views.push_back(block);
    this->addParameter("Color", DM::LONG, &color);
    this->addData("City", views);

}
void GraphicPlacement::run()
{
#if 0
    createFace_Circle(0, 0, 1, 256);
#else
    for (int i=0;i<200;i++)
    {
        double ulx=rand()%1000;
        double uly=rand()%1000;
        createGraphic(ulx,uly,1);//rand()%2);
    }
#endif

};

void GraphicPlacement::createGraphic(double px, double py, int no)
{
    if (no==0)
    {
        double w=rand()%100;
        double h=rand()%100;
        long color=rand()%256;
        createFace_Box(px,py,w,h,color);
    }
    else if (no==1)
    {
        double r=rand()%100;
        long color=rand()%256;
        createFace_Circle(px,py,r,color);
    }
}


void GraphicPlacement::createFace_Box( double px, double py, double w, double h, long color)
{
    QVector<QPointF> p;
    p<<QPointF(px, py);
    p<<QPointF(px+w, py);
    p<<QPointF(px+w, py+h);
    p<<QPointF(px, py+h);
    createFace_Polygon(p,color);
}

void GraphicPlacement::createFace_Circle( double px, double py, double r, long color)
{
#if 1
    int g=36;

    QVector<QPointF> p;

    for (int i=0;i<=360;i+=g)
    {
        double x=r*cos(M_PI*(double)i/180.0);
        double y=r*sin(M_PI*(double)i/180.0);
        p<<QPointF(px+x, py+y);
    }
    createFace_Polygon(p,color);
    p.clear();

#else
    QVector<QPointF> p;
    int n=5;
    p<<QPointF(px,py);
    for (int i=0;i<n;i++)
    {
        double x=-r*cos(M_PI*i/(n-1));
        double y=sqrt(r*r-x*x);
        p<<QPointF(px+x, py+y);
    }
    p<<QPointF(px,py);
    createFace_Polygon(p,color);
    p.clear();

    p<<QPointF(px,py);
    for (int i=0;i<n;i++)
    {
        double x=-r*cos(M_PI*i/(n-1));
        double y=sqrt(r*r-x*x);
        p<<QPointF(px+x, py-y);
    }
    p<<QPointF(px,py);
    createFace_Polygon(p,color);
    p.clear();

    p<<QPointF(px,py);
    for (int i=0;i<n;i++)
    {
        double x=-r*cos(M_PI*i/(n-1));
        double y=sqrt(r*r-x*x);
        p<<QPointF(px-x, py-y);
    }
    p<<QPointF(px,py);
    createFace_Polygon(p,color);
    p.clear();

    p<<QPointF(px,py);
    for (int i=0;i<n;i++)
    {
        double x=-r*cos(M_PI*i/(n-1));
        double y=sqrt(r*r-x*x);
        p<<QPointF(px-x, py+y);
    }
    p<<QPointF(px,py);
    createFace_Polygon(p,color);
    p.clear();
#endif

}

void GraphicPlacement::createFace_Polygon( QVector<QPointF> points, long color)
{
    DM::System * blocks = this->getData("City");
    std::vector<DM::Node*> ve;
    for (int i=0;i<points.size();i++)
    {
        cout << points[i].x() << " " << points[i].y()<<endl;
        DM::Node * n = blocks->addNode(points[i].x()  ,points[i].y()  , 0);
        ve.push_back(n);
    }

    DM::Node * ne = blocks->addNode(points[0].x()  ,points[0].y()  , 0);
    ve.push_back(ne);
    DM::Face * f = blocks->addFace(ve, block);
    f->addAttribute("Color", color);
}
