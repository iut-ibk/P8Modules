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

#ifndef GRAPHICPLACEMENT_H
#define GRAPHICPLACEMENT_H

#include <QVector>
#include <QPointF>

#include <dmmodule.h>
#include <dm.h>
class GraphicPlacement : public  DM::Module
{
    DM_DECLARE_NODE( GraphicPlacement )
    private:
        DM::View block ;
    long color;

public:
    GraphicPlacement();
    void run();
    void createGraphic(double px, double py, int no);
    void createFace_Box( double px, double py, double w, double h, long color);
    void createFace_Circle( double px, double py, double r, long color);
    void createFace_Polygon( QVector<QPointF> points, long color);
};

#endif // BLOCK_H
