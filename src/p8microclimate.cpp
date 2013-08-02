#include "p8microclimate.h"
#include "p8microclimate_gui.h"
#include "math.h"
#include <QWidget>

DM_DECLARE_NODE_NAME(Microclimate,P8Modules)

Microclimate::Microclimate()
{
    gridsize = 10;

    this->addParameter("Gridsize", DM::INT, &gridsize);
}

void Microclimate::init()
{
    DM::View data("Topology", DM::RASTERDATA, DM::READ);
    std::vector<DM::View> vdata;
    vdata.push_back(data);
    this->addData("City", vdata);
}

void Microclimate::run()
{
    DM::View data("Topology", DM::RASTERDATA, DM::READ);
    DM::RasterData * topo = this->getRasterData("City",data);

    // getting rasterdata values
    int datagridsize = topo->getCellSizeX();
    int dataheight = topo->getHeight();
    int datawidth = topo->getWidth();

    int datatotalheight = datagridsize * dataheight;
    int datatotalwidth = datagridsize * datawidth;

    //calculating values for our new grid
    double height = (double)datatotalheight / gridsize;
    double width = (double)datatotalwidth / gridsize;
    if (height - (int)height != 0)
    {
        height = (int) height + 1;
    }
    if(width - (int) width != 0)
    {
        width = (int)width + 1;
    }

    DM::RasterData * newt = new DM::RasterData(width,height,gridsize,gridsize,topo->getXOffset(),topo->getYOffset());
    fillZeros(newt);
    std::cout << "new Topo:" << endl;
    std::cout << "width: " << width << endl;
    std::cout << "height: " << height << endl;
    std::cout << "gridsize: " << gridsize << endl;

    double percent;

    // two for loops over the rasterdata array
    for(int i = 0;i<width;i++)
    {
        for(int j =0; j<height; j++)
        {

            vector<QPointF> cells = getCoveringCells(i*gridsize,j*gridsize,gridsize,datagridsize);
            for (int k = 0;k<cells.size();k++)
            {
                QPointF p = cells.back();
                std::cout << p.x() << " " << p.y() << endl;
                percent = calcOverlay(i * gridsize, j * gridsize,gridsize, p.x(), p.y(),datagridsize);
                std::cout<< percent << endl;
                newt->setCell(i,j,newt->getCell(i,j)+(topo->getCell(p.x(),p.y())*(percent/100)));
                cells.pop_back();
            }


            //std::cout << "coords: " << i << " " << j << endl;
            //std::cout << "A: " << A << " dataA: " << dataA << endl;
            //std::cout << percent << "%" << endl;
        }
    }
    printRaster(newt);
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


/*
bool Microclimate::createInputDialog()
{
    QWidget * w = new p8microclimate_gui(this);
    w->show();
    return true;
}
*/
