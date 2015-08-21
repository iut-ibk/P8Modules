#include "mcedit.h"
#include "ui_mcedit.h"

#include <QGraphicsScene>
#include <QGraphicsRectItem>
#include <QGraphicsItem>
#include <QGraphicsView>
#include <QLabel>
#include <QFileDialog>
#include <QPixmap>
#include "cell.h"
#include "mcgraphicscene.h"
#include <QGraphicsSceneMouseEvent>
#include <QGraphicsSimpleTextItem>
#include <QFile>
#include <QTextStream>
#include <QColor>
#include <QRect>
#include <QMessageBox>
#include <QTransform>
#include <cmath>
#include <QKeyEvent>
#include "../p8microclimate_gui.h"

#include "celldialog.h"

mcedit::mcedit(p8microclimate_gui *parent, QString bgimage, QString workpath, int cx, int cy, double sx, double sy) :
    QDialog(parent),
    ui(new Ui::mcedit)
{
    ui->setupUi(this);

    this->parent=parent;
    this->workpath=workpath;


    teccol.append(new QColor(4,224,23,255));
    teccol.append(new QColor(179,209,56,255));
    teccol.append(new QColor(7,224,126,255));
    teccol.append(new QColor(181,90,29,255));
    teccol.append(new QColor(9,0,173,255));
    teccol.append(new QColor(140,176,135,255));
    teccol.append(new QColor(4,224,23,255));
    teccol.append(new QColor(179,209,56,255));
    teccol.append(new QColor(7,224,126,255));
    teccol.append(new QColor(181,90,29,255));
    teccol.append(new QColor(9,0,173,255));

    minTempLandercover = 0;
    maxTempLandcover = 0;
    minTempReduction = -10;
    maxTempReduction = 10;
    minTempBefore = 20;
    maxTempBefore = 50;
    minTempAfter= 20;
    maxTempAfter = 50;

    this->cx=cx;
    this->cy=cy;
    this->sx=sx;
    this->sy=sy;

    scaleposx=0;
    scaleposy=-30;
    scalehight=10;
    scalelength=100;
    scalesteps=10;


    scene=new McGraphicsScene(this);
    ui->graphicsView->setScene(scene);
    ui->graphicsView->setDragMode(QGraphicsView::RubberBandDrag);

    double lx=cx*sx;
    double ly=cy*sy;
    scene->setSceneRect(0,-30,lx,ly);
    bgrect=scene->addRect(0,0,lx,ly);
    changebgcont(0);
    cellmap.clear();
    int pos=0;
    for (int y=0;y<cy;y++)
        for (int x=0;x<cx;x++)
        {
            Cell *cell=new Cell(x*sx,y*sy,sx,sy,scene,ui->graphicsView,pos,&teccol);
            cellmap.insert(cell->getRect(),cell);
            pos++;
        }

    QList<QRect> coverlist;
    coverlist << QRect(-100000,ly+2,lx+2*100000,100000) << QRect(-100000,-2,lx+2*100000,-100000) << QRect(-2,-100000,-100000,ly+2*100000) << QRect(lx+2,-100000,100000,ly+2*100000);
    foreach (QRect rect, coverlist)
    {
        QBrush brush;
        brush.setStyle(Qt::SolidPattern);
        brush.setColor(QColor(255,255,255,255));
        QPen pen;
        pen.setColor(QColor(255,255,255,255));
        QGraphicsRectItem *cover=scene->addRect(rect);
        cover->setBrush(brush);
        cover->setPen(pen);
    }
    ui->graphicsView->show();
    ui->graphicsView->setMouseTracking(true);

    double rectwidth=double(scalelength)/double(scalesteps);
    for (int i=0;i<scalesteps;i++)
    {
        int rectposx=scaleposx+i*rectwidth;
        QGraphicsRectItem *scalebox=scene->addRect(QRect(rectposx,scaleposy,rectwidth,scalehight));
        scaleboxes.append(scalebox);
    }
    scalestart=scene->addSimpleText("25.0 °C");
    scalestart->moveBy(0,scaleposy+scalehight+5);
    scaleend=scene->addSimpleText("40.0 °C");
    scaleend->moveBy(rectwidth*(scalesteps-1),scaleposy+scalehight+5);
    scaletitle=scene->addSimpleText("Scale");
    scaletitle->moveBy(rectwidth*scalesteps+5,scaleposy);

    setScale(25,40,0);



    mode=0;
    viewmode=1;
    tecLoad(parent);
    tecLoad(workpath+"/WSUDtech.mcd");
    if (QFile::exists(workpath+"/Reduction in LST.mcd"))
    {
        resLoad(0,workpath+"/Reduction in LST.mcd");
        ui->cb_mode->setCurrentIndex(1);
    }
    if (QFile::exists(workpath+"/LST before WSUD.mcd"))
    {
        resLoad(1,workpath+"/LST before WSUD.mcd");
    }
    if (QFile::exists(workpath+"/LST after WSUD.mcd"))
    {
        resLoad(2,workpath+"/LST after WSUD.mcd");
    }


    if (!bgimage.isEmpty())
        loadbackground(workpath+"/"+bgimage);
    cellupdate();
}

mcedit::~mcedit()
{
    delete ui;
}

void mcedit::mousemove(QGraphicsSceneMouseEvent *event)
{
    QGraphicsItem *item = scene->itemAt(event->scenePos(),ui->graphicsView->transform());
    Cell *selectedCell=cellmap.value((QGraphicsRectItem*)(item));
    if (selectedCell!=NULL)
    {
        ui->v1->setValue(selectedCell->getV(0));
        ui->v2->setValue(selectedCell->getV(1));
        ui->v3->setValue(selectedCell->getV(2));
        ui->v4->setValue(selectedCell->getV(3));
        ui->v5->setValue(selectedCell->getV(4));
        ui->v6->setValue(selectedCell->getV(5));
        ui->v7->setValue(selectedCell->getV(6));
        ui->v8->setValue(selectedCell->getV(7));
        ui->v9->setValue(selectedCell->getV(8));
        ui->v10->setValue(selectedCell->getV(9));
        ui->v11->setValue(selectedCell->getV(10));

        ui->temp->setValue(selectedCell->getRes(0));
    }
    ui->x->setValue(event->scenePos().x());
    ui->y->setValue(event->scenePos().y());
}

void mcedit::mousepress(QGraphicsSceneMouseEvent *event)
{
    QGraphicsItem *item = scene->itemAt(event->scenePos(),ui->graphicsView->transform());
    Cell *selectedCell=cellmap.value((QGraphicsRectItem*)(item));
    if (selectedCell!=NULL)
    {
        if (ui->rb_edit->isChecked())
            selectedCell->editVals();
    }
    cellupdate();
}

void mcedit::mouserelease(QGraphicsSceneMouseEvent *event)
{
    QGraphicsItem *item;
    item = scene->itemAt(event->scenePos(),ui->graphicsView->transform());
    Cell *selectedCell=cellmap.value((QGraphicsRectItem*)(item));
    item = scene->itemAt(event->lastScenePos(),ui->graphicsView->transform());
    Cell *lastSelectedCell=cellmap.value((QGraphicsRectItem*)(item));
    if (selectedCell==NULL || lastSelectedCell==NULL)
        return;
    int x1=lastSelectedCell->getPx();
    int x2=selectedCell->getPx();
    int y1=lastSelectedCell->getPy();
    int y2=selectedCell->getPy();
    if (x1>x2)
    {
        int h=x1; x1=x2; x2=h;
    }
    if (y1>y2)
    {
        int h=y1; y1=y2; y2=h;
    }

    QSet<Cell*> selectedCells;
    foreach (Cell *cell, cellmap.values())
    {
        if (cell->getPx()>=x1 && cell->getPx()<=x2 && cell->getPy()>=y1 && cell->getPy()<=y2)
        {
            selectedCells.insert(cell);
        }
    }

    foreach (Cell *cell, selectedCells)
    {
        if (ui->rb_toggle->isChecked())
            cell->setSelected(!cell->getSelected());
        if (ui->rb_select->isChecked())
            cell->setSelected(true);
        if (ui->rb_deselect->isChecked())
            cell->setSelected(false);
    }
    cellupdate();
}

void mcedit::mousedoubleclick(QGraphicsSceneMouseEvent *event)
{
    on_pb_edit_clicked();
}


void mcedit::on_pb_zoomin_clicked()
{
    zoomin();
    cellupdate();
}

void mcedit::on_pb_zoomout_clicked()
{
    zoomout();
    cellupdate();
}


void mcedit::zoomin()
{
    ui->graphicsView->scale(1.1,1.1);
    //    ui->pb_load->setText(QString("zoom %1").arg(ui->graphicsView->transform().m11()));
}

void mcedit::zoomout()
{
    if (ui->graphicsView->transform().m11()>=0.05)
        ui->graphicsView->scale(1.0/1.1,1.0/1.1);
    //    ui->pb_load->setText(QString("zoom %1").arg(ui->graphicsView->transform().m11()));
}

void mcedit::loadbackground(QString bgfilename)
{
    if (!bgfilename.isEmpty())
    {
        pixmap=QPixmap(bgfilename).scaled(cx*sx,cy*sy,Qt::IgnoreAspectRatio,Qt::SmoothTransformation);
        scene->setBackgroundBrush(pixmap);
    }
}

QColor mcedit::getColor(double startTemp, double endTemp, double temp, int colorramp)
{
    QColor retVal(0,0,0,255);

    if (temp<startTemp || temp>endTemp )
        return retVal;

    double perc=(temp-startTemp)/(endTemp-startTemp);

    if (colorramp==0)
    {
        QColor startColor(0,0,255,255);
        QColor endColor(255,0,0,255);
        retVal.setRedF((1-perc)*startColor.redF()+perc*endColor.redF());
        retVal.setGreenF((1-perc)*startColor.greenF()+perc*endColor.greenF());
        retVal.setBlueF((1-perc)*startColor.blueF()+perc*endColor.blueF());
    }

    if (colorramp==1)
    {
        QColor startColor(255,255,255,255);
        QColor endColor(255,0,0,255);
        retVal.setRedF((1-perc)*startColor.redF()+perc*endColor.redF());
        retVal.setGreenF((1-perc)*startColor.greenF()+perc*endColor.greenF());
        retVal.setBlueF((1-perc)*startColor.blueF()+perc*endColor.blueF());
    }

    return retVal;
}

void mcedit::setScale(double startTemp, double endTemp, int colorramp)
{
    for (int i=0;i<scalesteps;i++)
    {
        QBrush brush;
        brush.setStyle(Qt::SolidPattern);
        double temp=startTemp+i*(endTemp-startTemp)/scalesteps;
        brush.setColor(getColor(startTemp,endTemp,temp,colorramp));
        //        QPen pen;
        //        pen.setColor(QColor(0,0,0,255));
        QGraphicsRectItem *scalebox=scaleboxes[i];
        scalebox->setBrush(brush);
        //        scalebox->setPen(pen);
    }
    scalestart->setText(QString("%1 °C").arg(startTemp));
    scaleend->setText(QString("%1 °C").arg(endTemp));
}


/*
void mcedit::on_pushButton_clicked()
{
    QString bgfilename=QFileDialog::getOpenFileName(this,"Select background imgage",QDir::currentPath(),"*.png");
    loadbackground(bgfilename);
}
*/

int cellComp (Cell* a,  Cell* b)
{
    return (a->getNo()) < (b->getNo());
}


void mcedit::tecLoad()
{
    QString tfilename=QFileDialog::getOpenFileName(this,"Load mcd",workpath,"*.mcd");
    tecLoad(tfilename);
}

void mcedit::tecLoad(QString tfilename)
{
    if (!tfilename.isEmpty())
    {
        filename=tfilename;
        QFile file;
        file.setFileName(filename);
        if (file.open(QIODevice::ReadOnly|QIODevice::Text))
        {
            QTextStream stream;
            stream.setDevice(&file);
            stream.readLine(); // skip first line because of headers
            QList<Cell*> sortlist=cellmap.values();
            qSort(sortlist.begin(),sortlist.end(),cellComp);

            foreach (Cell *cell, sortlist)
            {
                QStringList linelist=stream.readLine().split(",");
                cell->setNo(linelist[0].toInt());
                cell->setV(0,linelist[1].toDouble());
                cell->setV(1,linelist[2].toDouble());
                cell->setV(2,linelist[3].toDouble());
                cell->setV(3,linelist[4].toDouble());
                cell->setV(4,linelist[5].toDouble());
                cell->setV(5,linelist[6].toDouble());
                cell->setV(6,linelist[7].toDouble());
                cell->setV(7,linelist[8].toDouble());
                cell->setV(8,linelist[9].toDouble());
                cell->setV(9,linelist[10].toDouble());
                cell->setV(10,linelist[11].toDouble());
            }
            file.close();
        }
    }
}


void mcedit::resLoad(int no, QString tfilename)
{
    if (!tfilename.isEmpty())
    {
        QFile file;
        file.setFileName(tfilename);
        file.open(QIODevice::ReadOnly|QIODevice::Text);
        QTextStream stream;
        stream.setDevice(&file);
        QList<Cell*> sortlist=cellmap.values();
        qSort(sortlist.begin(),sortlist.end(),cellComp);
        int linecount=-1; // because of header
        while (!stream.atEnd())
        {
            stream.readLine();
            linecount++;
        }

        if (linecount==sortlist.size())
        {
            stream.seek(0);
            stream.readLine(); // because of header
            foreach (Cell *cell, sortlist)
            {
                QStringList linelist=stream.readLine().split(",");
                cell->setRes(no,linelist[1].toDouble());
            }
        }
        else
        {
            foreach (Cell *cell, sortlist)
            {
                cell->setRes(no,0);
            }
        }
        file.close();
    }
}

void mcedit::tecSave()
{
    if (!filename.isEmpty())
        tecSave(filename);
    else
    {
        QString tfilename=QFileDialog::getSaveFileName(this,"Save mcd",workpath,"*.mcd");
        if (!tfilename.isEmpty())
        {
            filename=tfilename;
            tecSave(filename);
        }
    }
}

void mcedit::tecSaveAs()
{
    QString tfilename=QFileDialog::getSaveFileName(this,"Save mcd",workpath,"*.mcd");
    if (!tfilename.isEmpty())
    {
        filename=tfilename;
        tecSave(filename);
    }
}

void mcedit::tecSave(QString filename)
{
    QFile file;
    file.setFileName(filename);
    file.open(QIODevice::WriteOnly|QIODevice::Text);
    QTextStream stream;
    stream.setDevice(&file);
    stream << "Block, Swale, Bioretention, Infiltration system, Surface wetland, Pond and basin, Tree, Grass, Impervious area, Green wall, Green roof, User defined" << endl;
    QList<Cell*> sortlist=cellmap.values();
    qSort(sortlist.begin(),sortlist.end(),cellComp);
    foreach (Cell *cell, sortlist)
    {
        stream << cell->getNo() << ","
               << cell->getV(0) << ","
               << cell->getV(1) << ","
               << cell->getV(2) << ","
               << cell->getV(3) << ","
               << cell->getV(4) << ","
               << cell->getV(5) << ","
               << cell->getV(6) << ","
               << cell->getV(7) << ","
               << cell->getV(8) << ","
               << cell->getV(9) << ","
               << cell->getV(10) << "\n";
    }
    file.close();
}

void mcedit::tecSave(p8microclimate_gui *parent)
{
    QList<Cell*> sortlist=cellmap.values();
    qSort(sortlist.begin(),sortlist.end(),cellComp);
    QList<QList<double> > qsortlist;
    foreach (Cell *cell, sortlist)
    {
        QList<double> line;
        line << cell->getV(0)
             << cell->getV(1)
             << cell->getV(2)
             << cell->getV(3)
             << cell->getV(4)
             << cell->getV(5)
             << cell->getV(6)
             << cell->getV(7)
             << cell->getV(8)
             << cell->getV(9)
             << cell->getV(10);
        qsortlist << line;
    }
    parent->setTec(qsortlist);
}

void mcedit::tecLoad(p8microclimate_gui *parent)
{
    QList<QList<double> >qsortlist=parent->getTec();
    QList<Cell*> sortlist=cellmap.values();
    qSort(sortlist.begin(),sortlist.end(),cellComp);
    int i=0;
    if(qsortlist.isEmpty())
    {
        cout << "Map reset!!!!!!!!!!"<<endl;
        foreach (Cell *cell, sortlist)
        {
            cell->setNo(i);
            cell->setV(0,0);
            cell->setV(1,0);
            cell->setV(2,0);
            cell->setV(3,0);
            cell->setV(4,0);
            cell->setV(5,0);
            cell->setV(6,0);
            cell->setV(7,0);
            cell->setV(8,0);
            cell->setV(9,0);
            cell->setV(10,0);
            i++;
        }
    }
    else{
        foreach (Cell *cell, sortlist)
        {
            cell->setNo(i);
            cell->setV(0,qsortlist[i][0]);
            cell->setV(1,qsortlist[i][1]);
            cell->setV(2,qsortlist[i][2]);
            cell->setV(3,qsortlist[i][3]);
            cell->setV(4,qsortlist[i][4]);
            cell->setV(5,qsortlist[i][5]);
            cell->setV(6,qsortlist[i][6]);
            cell->setV(7,qsortlist[i][7]);
            cell->setV(8,qsortlist[i][8]);
            cell->setV(9,qsortlist[i][9]);
            cell->setV(10,qsortlist[i][10]);
            i++;
        }
    }
}

void mcedit::cellupdate()
{
    double startTemp = 0;
    double endTemp = 0;
    foreach(QGraphicsRectItem* scalebox,scaleboxes)
    {
        if (mode==0)
        {
            setScale(0,0,0);
        }
        if (mode==1)
        {
            startTemp = minTempReduction;
            endTemp = maxTempReduction;
            setScale(minTempReduction,maxTempReduction,0);//setScale(getMinValue(0)-3,getMaxValue(0)+3,0);
        }
        if (mode==2)
        {
            startTemp = minTempBefore;
            endTemp = maxTempBefore;
            setScale(minTempBefore,maxTempBefore,0);//setScale(getMinValueForLstAfterBefore()-5,getMaxValueForLstAfterBefore()+5,1);
        }
        if (mode==3)
        {
            startTemp = minTempAfter;
            endTemp = maxTempAfter;
            setScale(minTempAfter,maxTempAfter,0); // setScale(getMinValueForLstAfterBefore()-5,getMaxValueForLstAfterBefore()+5,1);
        }
    }


    foreach (Cell *cell, cellmap.values())
    {
        cell->update(mode,viewmode);
    }
}

void mcedit::changebgcont(int c)
{
    QBrush brush;
    brush.setStyle(Qt::SolidPattern);
    brush.setColor(QColor(255,255,255,c));
    bgrect->setBrush(brush);
}

void mcedit::on_pb_load_clicked()
{
    tecLoad();
}

void mcedit::on_pb_saveas_clicked()
{
    tecSaveAs();
}

void mcedit::on_pb_save_clicked()
{
    tecSave();
}

void mcedit::on_pb_clear_clicked()
{
    foreach (Cell *cell, cellmap.values())
    {
        cell->setSelected(false);
    }
    cellupdate();
}

void mcedit::on_pb_edit_clicked()
{
    QList<Cell*> selectedCells;
    foreach (Cell *cell, cellmap.values())
    {
        if (cell->getSelected())
        {
            selectedCells.append(cell);
            cell->setSelected(false);
        }
    }

    if (!selectedCells.isEmpty())
    {
        double v1=0;
        double v2=0;
        double v3=0;
        double v4=0;
        double v5=0;
        double v6=0;
        double v7=0;
        double v8=0;
        double v9=0;
        double v10=0;
        double v11=0;
        CellDialog *dia=new CellDialog(NULL,&v1,&v2,&v3,&v4,&v5,&v6,&v7,&v8,&v9,&v10,&v11);
        dia->exec();
        foreach (Cell *cell, selectedCells)
        {
            dia->getValues(&v1,&v2,&v3,&v4,&v5,&v6,&v7,&v8,&v9,&v10,&v11);
            cell->setV(0,v1);
            cell->setV(1,v2);
            cell->setV(2,v3);
            cell->setV(3,v4);
            cell->setV(4,v5);
            cell->setV(5,v6);
            cell->setV(6,v7);
            cell->setV(7,v8);
            cell->setV(8,v9);
            cell->setV(9,v10);
            cell->setV(10,v11);
        }
        cellupdate();
    }
    else
        QMessageBox::warning(this,"Warning","No cells selected.");
}

void mcedit::on_cb_mode_currentIndexChanged(int index)
{
    mode=index;
    if(index == 0){
        this->ui->minTemp->setValue(minTempLandercover);
        this->ui->maxTemp->setValue(maxTempLandcover);
    }else if(index == 1){
        this->ui->minTemp->setValue(minTempReduction);
        this->ui->maxTemp->setValue(maxTempReduction);
    }else if(index == 2){
        this->ui->minTemp->setValue(minTempBefore);
        this->ui->maxTemp->setValue(maxTempBefore);
    }else if(index == 3){
        this->ui->minTemp->setValue(minTempAfter);
        this->ui->maxTemp->setValue(maxTempAfter);
    }
    cellupdate();
}

void mcedit::on_horizontalSlider_valueChanged(int value)
{
    changebgcont(value);
}

void mcedit::on_comboBox_currentIndexChanged(int index)
{
    viewmode=index;
    cellupdate();
}

void mcedit::on_buttonBox_accepted()
{
    tecSave(workpath+"/WSUDtech.mcd");
    tecSave(parent);
    //    tecFill(doublecelllist);

    cout << "Workpath: "<<workpath.toStdString()<<endl;
    QFile file;
    file.setFileName(workpath+QString("/userdefcoef.txt"));
    file.open(QIODevice::WriteOnly|QIODevice::Text);
    QTextStream stream;
    stream.setDevice(&file);
    stream <<     ui->v11coeff->value() << endl;
    file.close();
}


void mcedit::on_rb_edit_toggled(bool checked)
{
    if (checked)
    {
        ui->pb_edit->setEnabled(false);
        ui->pb_clear->setEnabled(false);
    }
    else
    {
        ui->pb_edit->setEnabled(true);
        ui->pb_clear->setEnabled(true);
    }
}

void mcedit::on_pb_zoomout_2_clicked()
{
    while (ui->graphicsView->transform().m11()>=0.05)
        ui->graphicsView->scale(1.0/1.1,1.0/1.1);
    cellupdate();
}

void mcedit::on_pushButton_clicked()
{
    QString tfilename=QFileDialog::getSaveFileName(this,"Export tecnology map",workpath,"*.png");
    if (!tfilename.isEmpty())
    {
        /*
        QPixmap pixMap = QPixmap::grabWidget(ui->graphicsView);
        pixMap.save(tfilename);
        */
        //        ui->graphicsView->scene()->clearSelection();                                                  // Selections would also render to the file
        //ui->graphicsView->scene()->setSceneRect(ui->graphicsView->scene()->itemsBoundingRect());                          // Re-shrink the scene to it's bounding contents
        QImage image(ui->graphicsView->scene()->sceneRect().size().toSize(), QImage::Format_ARGB32);  // Create the image with the exact size of the shrunk scene
        //QImage image(1000,1000, QImage::Format_ARGB32);
        image.fill(Qt::transparent);                                              // Start all pixels transparent

        QPainter painter(&image);
        ui->graphicsView->scene()->render(&painter);
        image.save(tfilename);
    }
}

void mcedit::on_pb_run_released()
{
    this->parent->set_run();
    // emulate button box click
    QApplication::postEvent(this->ui->buttonBox->focusWidget(), new QKeyEvent(QEvent::KeyPress, Qt::Key_Enter, 0, 0));
    QApplication::postEvent(this->ui->buttonBox->focusWidget(), new QKeyEvent(QEvent::KeyRelease, Qt::Key_Enter, 0, 0));

}

void mcedit::on_minTemp_valueChanged(double arg1)
{
    if(mode == 0){
        minTempLandercover = arg1;
    }else if(mode == 1){
        minTempReduction = arg1;
    }else if(mode == 2){
        minTempBefore = arg1;
    }else if(mode == 3){
        minTempAfter = arg1;
    }
    cellupdate();}

void mcedit::on_maxTemp_valueChanged(double arg1)
{
    if(mode == 0){
        maxTempLandcover = arg1;
    }else if(mode == 1){
        maxTempReduction = arg1;
    }else if(mode == 2){
        maxTempBefore = arg1;
    }else if(mode == 3){
        maxTempAfter = arg1;
    }
    cellupdate();
}
