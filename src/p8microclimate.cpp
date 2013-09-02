#include "p8microclimate.h"
#include "p8microclimate_gui.h"
#include "math.h"
#include <QWidget>
#include "dmcomponent.h"
#include <iostream>
#include <fstream>
#include <string>
#include <QFile>
#include <QTextStream>
#include <QStringList>


DM_DECLARE_NODE_NAME(Microclimate,P8Modules)

Microclimate::Microclimate()
{
    gridsize = 30;
    percentile = 80;
    mapPic = "";
    shapefile = "";
    landuse = "";
    wsudTech = "";

    this->addParameter("Gridsize", DM::INT, &this->gridsize);
    this->addParameter("MapPic", DM::STRING, &this->mapPic);
    this->addParameter("Shapefile",DM::STRING,&this->shapefile);
    this->addParameter("Landuse",DM::STRING, &this->landuse);
    this->addParameter("Percentile",DM::INT, &this->percentile);
    this->addParameter("WSUDtech",DM::STRING, &this->wsudTech);

}

void Microclimate::init()
{
    //DM::View shape("Topology", DM::FACE, DM::READ);
    DM::View raster("Imp",DM::RASTERDATA,DM::READ);
    std::vector<DM::View> vdata;
    //vdata.push_back(shape);
    vdata.push_back(raster);
    this->addData("City", vdata);
}

void Microclimate::run()
{

    //DM::View topo("Topology", DM::FACE, DM::READ);
    DM::View raster("Imp",DM::RASTERDATA,DM::READ);
    DM::System * data = this->getData("City");
    DM::RasterData * imp = this->getRasterData("City",raster);


    //getting x and y edges of the shapefile
    //with that information and the cellsize we can build the grid
    std::map<std::string,DM::Node*> cmp = data->getAllNodes();
    std::cout << "size: " << cmp.size() << endl;


    //topology map data
    /*
    double topoXoffset = 0;
    double topoYoffset = 0;
    double topototalheight = fabs(Xmin - Xmax);
    double topototalwidth = fabs(Ymin - Ymax);
    */


    // getting rasterdata values

    double impwidth = imp->getWidth();
    double impheight = imp->getHeight();

    double imptotalwidth = imp->getCellSizeX() * impwidth;
    double imptotalheight = imp->getCellSizeX() * impheight;


    //calculating values for our new grid
    double height = (double)imptotalheight / gridsize;
    double width = (double)imptotalwidth / gridsize;
    if (height - (int)height != 0)
    {
        height = (int) height + 1;
    }
    if(width - (int) width != 0)
    {
        width = (int)width + 1;
    }

    DM::RasterData * newgrid = new DM::RasterData(width,height,gridsize,gridsize,imp->getXOffset(),imp->getYOffset());
    fillZeros(newgrid);



    std::cout << "new Topo:" << endl;
    std::cout << "width: " << width << endl;
    std::cout << "height: " << height << endl;
    std::cout << "gridsize: " << gridsize << endl;





    DM::RasterData * lst = new DM::RasterData(width,height,gridsize,gridsize,imp->getXOffset(),imp->getYOffset());
    fillZeros(lst);
    DM::RasterData * newlst = new DM::RasterData(width,height,gridsize,gridsize,imp->getXOffset(),imp->getYOffset());
    fillZeros(newlst);
    DM::RasterData * lstReduction = new DM::RasterData(width,height,gridsize,gridsize,imp->getXOffset(),imp->getYOffset());
    fillZeros(lstReduction);
    DM::RasterData * lstReductionAir = new DM::RasterData(width,height,gridsize,gridsize,imp->getXOffset(),imp->getYOffset());
    fillZeros(lstReductionAir);
    DM::RasterData * lstAfterWsud = new DM::RasterData(width,height,gridsize,gridsize,imp->getXOffset(),imp->getYOffset());
    fillZeros(lstAfterWsud);
    DM::RasterData * impAreabeforeWSUD = new DM::RasterData(width,height,gridsize,gridsize,imp->getXOffset(),imp->getYOffset());
    fillZeros(impAreabeforeWSUD);
    DM::RasterData * perAreabeforeWSUD = new DM::RasterData(width,height,gridsize,gridsize,imp->getXOffset(),imp->getYOffset());
    fillZeros(perAreabeforeWSUD);
    DM::RasterData * newPervArea = new DM::RasterData(width,height,gridsize,gridsize,imp->getXOffset(),imp->getYOffset());
    fillZeros(newPervArea);
    DM::RasterData * newPervFrac = new DM::RasterData(width,height,gridsize,gridsize,imp->getXOffset(),imp->getYOffset());
    fillZeros(newPervFrac);
    DM::RasterData * newImpPervArea = new DM::RasterData(width,height,gridsize,gridsize,imp->getXOffset(),imp->getYOffset());
    fillZeros(newImpPervArea);
    DM::RasterData * newImpPervFrac = new DM::RasterData(width,height,gridsize,gridsize,imp->getXOffset(),imp->getYOffset());
    fillZeros(newImpPervFrac);
    DM::RasterData * testgrid = new DM::RasterData(width,height,gridsize,gridsize,imp->getXOffset(),imp->getYOffset());
    fillZeros(testgrid);


    QList<QList<double> >WsudTech = readWsud(QString(this->wsudTech.c_str()));

    double percent;
    int impervcounter;
    int pervcounter;
    int totalcounter;
    double impPercentage;
    double techarea;
    double pervareafrac;
    double delta;
    double realx;
    double realy;
    bool first = true;
    QList<double> wsudline;
    QList<QList<double> >wsudlines;
    // two for loops over the rasterdata array
    for(int i = 0;i<width;i++)
    {
        for(int j =0; j<height; j++)
        {
            /*
            realx = imp->getXOffset() + i * imp->getCellSizeX();
            realy = imp->getYOffset() + j * imp->getCellSizeY();
            DM::Node * a;
            DM::Node * b;
            DM::Node c = DM::Node(realx,realy,0);
            //std::cout << "x coord: " << realx << endl;
            //std::cout << "y coord: " << realy << endl;
            for(map<std::string,DM::Node*>::iterator ii=cmp.begin(); ii!=cmp.end(); ++ii)
            {
                a = (*ii).second;
                //std::cout << "nodeXY: " << a->getX() << " " << a->getY() << endl;
                if(a->getX() == 0 || a->getY() == 0)
                    continue;
                if(first)
                {
                    first = false;
                }
                else
                {
                    if(isleft(*b,*a,c))
                    {
                        testgrid->setCell(i,j,1);
                    }
                }
                b = a;

            }
            */
            delta = 0;
            wsudlines.clear();
            impervcounter = 0;
            pervcounter = 0;
            techarea = 0;
            vector<QPointF> cells = getCoveringCells(i*gridsize,j*gridsize,gridsize,imp->getCellSizeX());
            while(!cells.empty())
            {
                QPointF p = cells.back();
                //std::cout << p.x() << " " << p.y() << endl;
                //percent = calcOverlay(i * gridsize, j * gridsize,gridsize, p.x(), p.y(),imp->getCellSizeX());
                //std::cout<< percent << endl;

                // change calculation here -> dont add up values anymore
                // ->count "17s" and/or "1s" and then determen percentage of impervious
                //newgrid->setCell(i,j,newgrid->getCell(i,j)+(imp->getCell(p.x(),p.y())*(percent/100)));        old code
                wsudline = getTechAreasForCell(p.x(),p.y(),imp->getWidth(),WsudTech);
                wsudlines.append(wsudline);
                for (int k = 1;k<wsudline.size();k++)
                {
                    techarea += wsudline[k];
                }
                if(imp->getCell(p.x(),p.y()) == 1)  //if cell has value 1 in raster data it means its impervious
                {                                   //this value can and most porbably will change
                    impervcounter ++;
                }
                else
                {
                    pervcounter ++;
                }
                cells.pop_back();
            }

            totalcounter = impervcounter + pervcounter;
            impPercentage = (double)impervcounter/(double)totalcounter*100;
            newgrid->setCell(i,j,impPercentage);          
            lst->setCell(i,j,chooseTab(impPercentage));

            impAreabeforeWSUD->setCell(i,j,(impPercentage/100)*(gridsize*gridsize));
            perAreabeforeWSUD->setCell(i,j,(gridsize*gridsize) - ((impPercentage/100)*(gridsize*gridsize)));
            newPervArea->setCell(i,j, perAreabeforeWSUD->getCell(i,j) + perAreabeforeWSUD->getCell(i,j) * techarea / 100);
            pervareafrac = newPervArea->getCell(i,j) / (gridsize * gridsize);
            if (pervareafrac > 100)
                pervareafrac = 100;
            newPervFrac->setCell(i,j,pervareafrac);
            newImpPervArea->setCell(i,j,(gridsize*gridsize) - newPervArea->getCell(i,j));
            newImpPervFrac->setCell(i,j,newImpPervArea->getCell(i,j) / (gridsize * gridsize));
            newlst->setCell(i,j,chooseTab(newImpPervFrac->getCell(i,j)*100));
            for(int k = 0;k<wsudlines.size();k++)
            {
                if(newPervFrac->getCell(i,j) < 20)
                {
                    break;
                }
                delta += calcDeltaLst(wsudlines[k],newPervFrac->getCell(i,j));
            }
            lstAfterWsud->setCell(i,j,newlst->getCell(i,j)+delta);
            lstReduction->setCell(i,j,lstAfterWsud->getCell(i,j) - lst->getCell(i,j));
            lstReductionAir->setCell(i,j,lstReduction->getCell(i,j) * (-0.1));

        }
    }

    std::cout << "NEWGRID:" << endl;
    printRaster(newgrid);
    std::cout << "LST" << endl;
    printRaster(lst);
    std::cout << "lstAFTER" << endl;
    printRaster(lstAfterWsud);
    std::cout << "lstReduction" << endl;
    printRaster(lstReduction);
    std::cout << "lstReductionAIR" << endl;
    printRaster(lstReductionAir);
    exportRasterData(imp,"Grid.txt");
    exportRasterData(lst,"LST before WSUD.txt");
    exportRasterData(lstAfterWsud,"LST after WSUD.txt");
    exportRasterData(lstReduction,"Reduction in LST.txt");
    exportRasterData(lstReductionAir,"Reduction in Air Temperature.txt");

}
void Microclimate::printRaster(DM::RasterData * r)
{
    for(int i = 0;i<r->getWidth();i++)
    {
        for(int j = 0; j<r->getHeight();j++)
        {
            std::cout<<r->getCell(i,j)<< "\t\t";
        }
        std::cout<<endl;
    }
}

void Microclimate::fillZeros(DM::RasterData * r)
{
    for(int i = 0;i<r->getWidth();i++)
    {
        for(int j = 0; j<r->getHeight();j++)
        {
            r->setCell(i,j,0);
        }
    }
}

double Microclimate::chooseTab(double perc)
{
    QList<QList<double> > tif02;
    QList<double> zeile1,zeile2;
    zeile1 << 27.59 << 28.54 << 29.49 << 30.44 << 31.40 << 32.36;
    zeile2 <<  1.52 <<  6.99 << 37.36 << 88.70 << 99.33 << 99.94;
    tif02 << zeile1 << zeile2;

    QList<QList<double> > tif03;
    zeile1.clear();zeile2.clear();
    zeile1 << 27.99 << 28.76 << 29.53 << 30.30 << 31.07 << 31.85 << 32.62;
    zeile2 <<  0.58 <<  2.92 << 15.49 << 48.22 << 92.35 << 99.36 << 99.95;
    tif03 << zeile1 << zeile2;

    QList<QList<double> > tif04;
    zeile1.clear();zeile2.clear();
    zeile1 << 28.61 << 29.24 << 29.87 << 30.51 << 31.15 << 31.78 << 32.41;
    zeile2 <<  0.91 <<  5.17 << 16.71 << 43.75 << 85.68 << 98.75 << 99.96;
    tif04 << zeile1 << zeile2;

    QList<QList<double> > tif05;
    zeile1.clear();zeile2.clear();
    zeile1 << 28.50 << 29.23 << 29.96 << 30.71 << 31.45 << 32.18 << 32.92;
    zeile2 <<  0.59 <<  2.67 << 13.35 << 43.91 << 90.48 << 99.38 << 99.98;
    tif05 << zeile1 << zeile2;

    QList<QList<double> > tif06;
    zeile1.clear();zeile2.clear();
    zeile1 << 29.53 << 30.30 << 31.10 << 31.90 << 32.68;
    zeile2 <<  2.01 << 15.18 << 57.01 << 95.11 << 99.98;
    tif06 << zeile1 << zeile2;

    QList<QList<double> > tif07;
    zeile1.clear();zeile2.clear();
    zeile1 << 26.14 << 28.03 << 29.45 << 30.38 << 31.34 << 32.30 << 33.23;
    zeile2 <<  0.64 <<  1.29 <<  4.50 << 34.08 << 89.38 << 99.67 << 99.99;
    tif07 << zeile1 << zeile2;

    QList<QList<double> > tif08;
    zeile1.clear();zeile2.clear();
    zeile1 << 29.10 << 30.04 << 30.97 << 31.92 << 32.84 << 33.77;
    zeile2 <<  0.63 <<  2.84 << 27.76 << 83.27 << 99.04 << 99.99;
    tif08 << zeile1 << zeile2;

    QList<QList<double> > tif09;
    zeile1.clear();zeile2.clear();
    zeile1 << 26.48 << 28.36 << 29.61 << 30.88 << 32.15 << 33.41 << 35.94;
    zeile2 <<  0.58 <<  1.16 <<  2.61 << 24.05 << 87.81 << 99.40 << 99.98;
    tif09 << zeile1 << zeile2;

    QList<QList<double> > tif1;
    zeile1.clear();zeile2.clear();
    zeile1 << 27.31 << 28.73 << 30.11 << 31.52 << 32.95 << 34.37 << 35.78;
    zeile2 <<  0.93 <<  2.48 <<  6.50 << 45.19 << 89.76 << 98.42 << 99.97;
    tif1 << zeile1 << zeile2;

    if(perc < 20)
    {
        return calcLST(tif02);
    }
    else if(perc < 30)
    {
        return calcLST(tif03);
    }
    else if(perc < 40)
    {
        return calcLST(tif04);
    }
    else if(perc < 50)
    {
        return calcLST(tif05);
    }
    else if(perc < 60)
    {
        return calcLST(tif06);
    }
    else if(perc < 70)
    {
        return calcLST(tif07);
    }
    else if(perc < 80)
    {
        return calcLST(tif08);
    }
    else if(perc < 90)
    {
        return calcLST(tif09);
    }
    else
    {
        return calcLST(tif1);
    }


}

double Microclimate::calcLST(QList<QList<double> > t)
{
    int pointer;
    double res;
    for(int i = 0;i<t[1].size();i++)
    {
        if(this->percentile < t[1][i])
        {
            pointer = i;
            break;
        }
    }
    // interpolating the perc value of the cell to the values in the table
    res = t[0][pointer-1] + ( (double)this->percentile - t[1][pointer-1])/(t[1][pointer] - t[1][pointer-1])*(t[0][pointer] - t[0][pointer-1]);
    return res;
}

QList<QList<double> > Microclimate::readWsud(QString filename)
{
    QList<QList<double> > res;
    QList<double> line;
    QFile file;
    file.setFileName(filename);
    file.open(QIODevice::Text|QIODevice::ReadOnly);
    QTextStream stream;
    stream.setDevice(&file);

    while(!stream.atEnd())
    {
        QString input=stream.readLine();
        QStringList list=input.split(",",QString::KeepEmptyParts);
        while(!list.isEmpty())
            line.append(list.takeFirst().toDouble());
        res.append(line);
        line.clear();
    }
    return res;
}

QList<double> Microclimate::getTechAreasForCell(int x, int y,double w, QList<QList<double> > table)
{
    QList<double>zero;
    zero.append(0);
    //double res = 0;
    double cellarea = this->gridsize * this->gridsize;
    int pos = x * w + y;
    /*for(int i = 1;i<table[0].size();i++)
    {
        res += table[pos][i]/100 * cellarea;
    }*/
    if (pos > table.size()-1)
        return zero;
    return table[pos];
}

double Microclimate::calcDeltaLst(QList<double> t, double frac)
{
    int counter = 0;
    double res = 0;
    if(t[1] != 0)
    {
        counter++;
        res += frac /100;
    }
    if(t[2] != 0)
    {
        counter++;
        res += frac /100 -(0.2*0.5);
    }
    if(t[3] != 0)
    {
        counter++;
        res += frac /100 -(0.2*0.5);
    }
    if(t[4] != 0)
    {
        counter++;
        res += frac /100 - 0.2;
    }
    if(t[5] != 0)
    {
        counter++;
        res += frac /100 - 0.2;
    }
    if(t[6] != 0)
    {
        counter++;
        res += frac /100 - (0.2 * 2.75);
    }
    if(res != 0)
    {
        res = res / (double)counter;
    }
    return res;
}

void Microclimate::exportRasterData(DM::RasterData *r, QString filename)
{
    QFile file (filename);
    if(file.open(QIODevice::WriteOnly))
    {
        QTextStream outstream (&file);
        outstream << "ncols" << "\t" << r->getWidth() << endl;
        outstream << "nrows" << "\t" << r->getHeight() << endl;
        outstream << "xllcorner" << "\t" << r->getXOffset() << endl;
        outstream << "yllcorner" << "\t" << r->getYOffset() << endl;
        outstream << "cellsize" << "\t" << r->getCellSizeX() << endl;
        outstream << "NODATA_value" << "\t" << r->getNoValue() << endl;

        for(int i = 0; i<r->getWidth();i++)
        {
            for(int j = 0; j< r->getHeight(); j++)
            {
                outstream << r->getCell(i,j) << " ";
            }
            outstream << endl;
        }
    }
}

bool Microclimate::isleft(DM::Node a, DM::Node b, DM::Node c)
{
    return ((b.getX() - a.getX()) * (c.getY() - a.getY()) - (b.getY() - a.getY()) * (c.getX() - a.getX())) > 0;
}


double Microclimate::calcOverlay(double x1,double y1,double g1,double x2,double y2, double g2)
{

    QRectF * cell1 = new QRectF(x1,y1, g1,g1);
    QRectF * cell2 = new QRectF(x2,y2,g2,g2);

    //check if overlapping
    if (cell1->topLeft().x() > cell2->topRight().x())
        return 0;
    if (cell1->topLeft().y() > cell2->bottomLeft().y())
        return 0;
    //adjust boundrys of cell1
    if(cell1->left() < cell2->left())
        cell1->setLeft(cell2->left());
    if(cell1->right() > cell2->right())
        cell1->setRight(cell2->right());
    if(cell1->top()< cell2->top())
        cell1->setTop(cell2->top());
    if(cell1->bottom() > cell2->bottom())
        cell1->setBottom(cell2->bottom());

    return (calcA(cell1)/calcA(cell2))*100;
}

double Microclimate::calcA(QRectF *r)
{
    return r->width() * r->height();
}

std::vector<QPointF> Microclimate::getCoveringCells(double x, double y, double g1,double g2)
{
    std::vector<QPointF> res;
    QRectF * cell = new QRectF(x,y,g1,g1);

    int leftX = cell->left() / g2;
    int topY = cell->top() / g2;
    int rightX = cell->right() / g2;
    int botY = cell->bottom() / g2;

    int columns = (rightX - leftX) / g2;
    int rows = (botY - topY) / g2;
    int correction = 2;
    if (fmod(cell->right(),g2) == 0)
    {
        correction --;
    }
    if (fmod(cell->left(),g2) == 0)
    {
        correction --;
    }
    for(int i = 0; i<columns + correction;i++)
    {
        for(int j = 0; j < rows + correction;j++)
        {
            QPointF p = QPointF(leftX + i * g2,topY + j * g2);
            res.push_back(p);
        }
    }
    return res;
}

bool Microclimate::createInputDialog()
{
    QWidget * w = new p8microclimate_gui(this);
    w->show();
    return true;
}
