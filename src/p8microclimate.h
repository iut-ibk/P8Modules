#ifndef P8MICROCLIMATE_H
#define P8MICROCLIMATE_H

#include <dmmodule.h>
#include <dm.h>
#include <qrect.h>
class DM_HELPER_DLL_EXPORT Microclimate : public DM::Module
{
    DM_DECLARE_NODE(Microclimate)
private:
    int gridsize;

public:
    Microclimate();
    void init();
    void run();
   // virtual bool createInputDialog();
    void printRaster(DM::RasterData * r);
    double calcOverlay(double x1, double y1, double gridsize1, double x2, double y2, double gridsize2);
    double calcA(QRectF * r);
    std::vector<QPointF>  getCoveringCells(double x,double y,double g1,double g2);
    void fillZeros(DM::RasterData * r);
};

#endif // P8MICROCLIMATE_H
