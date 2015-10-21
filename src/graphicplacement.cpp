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
#include <dmcomponent.h>

#include <QColorDialog>

#include <cmath>
#ifndef M_PI
#define M_PI        3.14159265358979323846
#endif
//Creates a Block with 1 per 1 meter






DM_DECLARE_NODE_NAME( GraphicPlacement, )
GraphicPlacement::GraphicPlacement()
{
    //QColorDialog::getColor();
    std::vector<DM::View> views;

    graphicPositions = DM::View("graphicPositions", DM::COMPONENT, DM::READ);
    graphicPositions.getAttribute("xCoords");
    graphicPositions.getAttribute("yCoords");
    graphicPositions.getAttribute("Types");
    views.push_back(graphicPositions);

    block = DM::View("GraphicPlacement", DM::FACE, DM::WRITE);
    block.addAttribute("Color");
    views.push_back(block);
    this->addParameter("Color", DM::LONG, &color);
    this->addData("City", views);

}
void GraphicPlacement::run()
{
    DM::System * city = this->getData("City");
    std::vector<std::string> strvec = city->getUUIDsOfComponentsInView(graphicPositions);
    cout<< "strvec length: "<< strvec.size() << endl;

    foreach (std::string str, strvec)
    {
        DM::Component *graposAttr = city->getComponent(str);
        std::vector<double> xCoords =  graposAttr->getAttribute("xCoords")->getDoubleVector();
        std::vector<double> yCoords =  graposAttr->getAttribute("yCoords")->getDoubleVector();
        std::vector<double> gTypes =  graposAttr->getAttribute("Types")->getDoubleVector();

        for (int i=0;i<xCoords.size();i++)
        {
            createGraphic(xCoords[i],yCoords[i],int(gTypes[i]));//rand()%2);
            cout << "create graphic: "<<xCoords[i]<<","<<yCoords[i]<<endl;
        }
    }
    /*
    for (int i=0;i<20;i++)
    {
        double ulx=rand()%1000;
        double uly=rand()%1000;
        createGraphic(ulx,uly,0);//rand()%2);
    }

*/
};

void GraphicPlacement::createGraphic(double px, double py, int no)
{
    /*
WSUR - Wetland = 1 –  green circle - 107
PB - Pond = 2 – orange circle - 40
IS - Infil = 3 – dark red circle - 360
BF - BioRetention = 4 - ? - 176
SW - Swale = 5 – green - black square - 262
*/

    double w=100;
    double h=100;
    long color;

    if (no==1) //Wetland
    {
        color=107;
        createFace_Box(px,py,w,h,color);
    }
    else if (no==2) //Pond
    {
        color=40;
        createFace_Box(px,py,w,h,color);
    }
    else if (no==3) //Infil
    {
        color=360;
        createFace_Box(px,py,w,h,color);
    }
    else if (no==4) //BioRetention
    {
        color=176;
        createFace_Box(px,py,w,h,color);
    }
    else if (no==5) //Swale
    {
        color=262;
        createFace_Box(px,py,w,h,color);
    }
    else
    {
        color=130;
        createFace_Box(px,py,w,h,color);
    }



/*
    if (no==0)
    {
        double w=100;
        double h=100;
        long color=rand()%256;
        createFace_Box(px,py,w,h,color);
    }
    else if (no==1)
    {
        double r=rand()%100;
        long color=rand()%256;
        createFace_Circle(px,py,r,color);
    }
    */
}


void GraphicPlacement::createFace_Box( double px, double py, double w, double h, long color)
{
    QVector<QPointF> p;
    p<<QPointF(px-w/2.0, py-h/2.0);
    p<<QPointF(px+w/2.0, py-h/2.0);
    p<<QPointF(px+w/2.0, py+h/2.0);
    p<<QPointF(px-w/2.0, py+h/2.0);
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
