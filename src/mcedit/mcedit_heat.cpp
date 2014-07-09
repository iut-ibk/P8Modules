#include "mcedit_heat.h"
#include "ui_mcedit_heat.h"
#include <QGraphicsScene>
#include <QGraphicsRectItem>
#include <QGraphicsItem>
#include <QGraphicsView>
#include <QLabel>
#include <QFileDialog>
#include <QPixmap>
#include "cell_heat.h"
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
#include "../p8microclimate_heat_gui.h"

#include "celldialog_heat.h"

mcedit_heat::mcedit_heat(p8microclimate_heat_gui *parent, QString bgimage, QString workpath, int cx, int cy, double sx, double sy) :
    QDialog(parent),
    ui(new Ui::mcedit_heat)
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
            Cell_heat *cell=new Cell_heat(x*sx,y*sy,sx,sy,scene,ui->graphicsView,pos,&teccol);
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
    if(QFile::exists(workpath+"/WSUDtech.mcd"))
    {
        tecLoad(workpath+"/WSUDtech.mcd");
    }
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

mcedit_heat::~mcedit_heat()
{
    delete ui;
}

void mcedit_heat::mousemove(QGraphicsSceneMouseEvent *event)
{
    QGraphicsItem *item = scene->itemAt(event->scenePos(),ui->graphicsView->transform());
    Cell_heat *selectedCell=cellmap.value((QGraphicsRectItem*)(item));
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
        ui->v12->setValue(selectedCell->getV(11));
        ui->v13->setValue(selectedCell->getV(12));
        ui->v14->setValue(selectedCell->getV(13));
        ui->v15->setValue(selectedCell->getV(14));





        ui->temp->setValue(selectedCell->getRes(0));
    }
    ui->x->setValue(event->scenePos().x());
    ui->y->setValue(event->scenePos().y());
}

void mcedit_heat::mousepress(QGraphicsSceneMouseEvent *event)
{
    QGraphicsItem *item = scene->itemAt(event->scenePos(),ui->graphicsView->transform());
    Cell_heat *selectedCell=cellmap.value((QGraphicsRectItem*)(item));
    if (selectedCell!=NULL)
    {
        if (ui->rb_edit->isChecked())
            selectedCell->editVals();
    }
    cellupdate();
}

void mcedit_heat::mouserelease(QGraphicsSceneMouseEvent *event)
{
    QGraphicsItem *item;
    item = scene->itemAt(event->scenePos(),ui->graphicsView->transform());
    Cell_heat *selectedCell=cellmap.value((QGraphicsRectItem*)(item));
    item = scene->itemAt(event->lastScenePos(),ui->graphicsView->transform());
    Cell_heat *lastSelectedCell=cellmap.value((QGraphicsRectItem*)(item));
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

    QSet<Cell_heat*> selectedCells;
    foreach (Cell_heat *cell, cellmap.values())
    {
        if (cell->getPx()>=x1 && cell->getPx()<=x2 && cell->getPy()>=y1 && cell->getPy()<=y2)
        {
            selectedCells.insert(cell);
        }
    }

    foreach (Cell_heat *cell, selectedCells)
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



void mcedit_heat::on_pb_zoomin_clicked()
{
    zoomin();
    cellupdate();
}

void mcedit_heat::on_pb_zoomout_clicked()
{
    zoomout();
    cellupdate();
}


void mcedit_heat::zoomin()
{
    ui->graphicsView->scale(1.1,1.1);
    //    ui->pb_load->setText(QString("zoom %1").arg(ui->graphicsView->transform().m11()));
}

void mcedit_heat::zoomout()
{
    if (ui->graphicsView->transform().m11()>=0.05)
        ui->graphicsView->scale(1.0/1.1,1.0/1.1);
    //    ui->pb_load->setText(QString("zoom %1").arg(ui->graphicsView->transform().m11()));
}

void mcedit_heat::loadbackground(QString bgfilename)
{
    if (!bgfilename.isEmpty())
    {
        pixmap=QPixmap(bgfilename).scaled(cx*sx,cy*sy,Qt::IgnoreAspectRatio,Qt::SmoothTransformation);
        scene->setBackgroundBrush(pixmap);
    }
}

QColor mcedit_heat::getColor(double startTemp, double endTemp, double temp, int colorramp)
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

void mcedit_heat::setScale(double startTemp, double endTemp, int colorramp)
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

int cellCompare (Cell_heat* a,  Cell_heat* b)
{
    return (a->getNo()) < (b->getNo());
}


void mcedit_heat::tecLoad()
{
    QString tfilename=QFileDialog::getOpenFileName(this,"Load mcd",workpath,"*.mcd");
    tecLoad(tfilename);
}

void mcedit_heat::tecLoad(QString tfilename)
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
            QList<Cell_heat*> sortlist=cellmap.values();
            qSort(sortlist.begin(),sortlist.end(),cellCompare);

            foreach (Cell_heat *cell, sortlist)
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
                cell->setV(11,linelist[12].toDouble());
                cell->setV(12,linelist[13].toDouble());
                cell->setV(13,linelist[14].toDouble());
                cell->setV(14,linelist[15].toDouble());

            }
            file.close();
        }
    }
}


void mcedit_heat::resLoad(int no, QString tfilename)
{
    if (!tfilename.isEmpty())
    {
        QFile file;
        file.setFileName(tfilename);
        file.open(QIODevice::ReadOnly|QIODevice::Text);
        QTextStream stream;
        stream.setDevice(&file);
        QList<Cell_heat*> sortlist=cellmap.values();
        qSort(sortlist.begin(),sortlist.end(),cellCompare);
        int linecount=0;
        while (!stream.atEnd())
        {
            stream.readLine();
            linecount++;
        }

        if (linecount==sortlist.size())
        {
            stream.seek(0);
            foreach (Cell_heat *cell, sortlist)
            {
                QStringList linelist=stream.readLine().split(",");
                cell->setRes(no,linelist[1].toDouble());
            }
        }
        else
        {
            foreach (Cell_heat *cell, sortlist)
            {
                cell->setRes(no,0);
            }
        }
        file.close();
    }
}

void mcedit_heat::tecSave()
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

void mcedit_heat::tecSaveAs()
{
    QString tfilename=QFileDialog::getSaveFileName(this,"Save mcd",workpath,"*.mcd");
    if (!tfilename.isEmpty())
    {
        filename=tfilename;
        tecSave(filename);
    }
}

void mcedit_heat::tecSave(QString filename)
{
    QFile file;
    file.setFileName(filename);
    file.open(QIODevice::WriteOnly|QIODevice::Text);
    QTextStream stream;
    stream.setDevice(&file);
    QList<Cell_heat*> sortlist=cellmap.values();
    qSort(sortlist.begin(),sortlist.end(),cellCompare);
    foreach (Cell_heat *cell, sortlist)
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
               << cell->getV(10) << ","
               << cell->getV(11) << ","
               << cell->getV(12) << ","
               << cell->getV(13) << ","
               << cell->getV(14) << "\n";
    }
    file.close();
}

void mcedit_heat::tecSave(p8microclimate_heat_gui *parent)
{
    QList<Cell_heat*> sortlist=cellmap.values();
    qSort(sortlist.begin(),sortlist.end(),cellCompare);
    QList<QList<double> > qsortlist;
    foreach (Cell_heat *cell, sortlist)
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
             << cell->getV(10)
             << cell->getV(11)
             << cell->getV(12)
             << cell->getV(13)
             << cell->getV(14);

        qsortlist << line;
    }
    parent->setTec(qsortlist);
}

void mcedit_heat::tecLoad(p8microclimate_heat_gui *parent)
{
    QList<QList<double> >qsortlist=parent->getTec();
    QList<Cell_heat*> sortlist=cellmap.values();
    qSort(sortlist.begin(),sortlist.end(),cellCompare);
    int i=0;
    if(qsortlist.isEmpty())
    {
        cout << "Map reset!!!!!!!!!!"<<endl;
        foreach (Cell_heat *cell, sortlist)
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
            cell->setV(11,0);
            cell->setV(12,0);
            cell->setV(13,0);
            cell->setV(14,0);
            i++;
        }
    }
    else{
        foreach (Cell_heat *cell, sortlist)
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
            cell->setV(11,qsortlist[i][11]);
            cell->setV(12,qsortlist[i][12]);
            cell->setV(13,qsortlist[i][13]);
            cell->setV(14,qsortlist[i][14]);

            i++;
        }
    }
}

void mcedit_heat::cellupdate()
{
    foreach(QGraphicsRectItem* scalebox,scaleboxes)
    {
        if (mode==0)
        {
            setScale(0,0,0);
        }
        if (mode==1)
        {
            setScale(-5,5,0);
        }
        if (mode==2)
        {
            setScale(30,45,1);
        }
        if (mode==3)
        {
            setScale(30,40,1);
        }
    }


    foreach (Cell_heat *cell, cellmap.values())
    {
        cell->update(mode,viewmode);
    }
}

void mcedit_heat::changebgcont(int c)
{
    QBrush brush;
    brush.setStyle(Qt::SolidPattern);
    brush.setColor(QColor(255,255,255,c));
    bgrect->setBrush(brush);
}

void mcedit_heat::on_pb_load_clicked()
{
    tecLoad();
}

void mcedit_heat::on_pb_saveas_clicked()
{
    tecSaveAs();
}

void mcedit_heat::on_pb_save_clicked()
{
    tecSave();
}

void mcedit_heat::on_pb_clear_clicked()
{
    foreach (Cell_heat *cell, cellmap.values())
    {
        cell->setSelected(false);
    }
    cellupdate();
}

void mcedit_heat::on_pb_edit_clicked()
{
    QList<Cell_heat*> selectedCells;
    foreach (Cell_heat *cell, cellmap.values())
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
        double v12=0;
        double v13=0;
        double v14=0;
        double v15=0;

        CellDialog_heat *dia=new CellDialog_heat(NULL,&v1,&v2,&v3,&v4,&v5,&v6,&v7,&v8,&v9,&v10,&v11,&v12,&v13,&v14,&v15);
        dia->exec();
        foreach (Cell_heat *cell, selectedCells)
        {
            dia->getValues(&v1,&v2,&v3,&v4,&v5,&v6,&v7,&v8,&v9,&v10,&v11,&v12,&v13,&v14,&v15);
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
            cell->setV(11,v12);
            cell->setV(12,v13);
            cell->setV(13,v14);
            cell->setV(14,v15);
        }
        cellupdate();
    }
    else
        QMessageBox::warning(this,"Warning","No cells selected.");
}

void mcedit_heat::on_cb_mode_currentIndexChanged(int index)
{
    mode=index;
    cellupdate();
}

void mcedit_heat::on_horizontalSlider_valueChanged(int value)
{
    changebgcont(value);
}

void mcedit_heat::on_comboBox_currentIndexChanged(int index)
{
    viewmode=index;
    cellupdate();
}

void mcedit_heat::on_buttonBox_accepted()
{
    tecSave(workpath+"/WSUDtech.mcd");
    tecSave(parent);
    //    tecFill(doublecelllist);

    cout << "Workpath: "<<workpath.toStdString()<<endl;
    /*QFile file;
    file.setFileName(workpath+QString("/userdefcoef.txt"));
    file.open(QIODevice::WriteOnly|QIODevice::Text);
    QTextStream stream;
    stream.setDevice(&file);
    stream <<     ui->v11coeff->value() << endl;
    file.close();
    */
}


void mcedit_heat::on_rb_edit_toggled(bool checked)
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

void mcedit_heat::on_pb_zoomout_2_clicked()
{
    while (ui->graphicsView->transform().m11()>=0.05)
        ui->graphicsView->scale(1.0/1.1,1.0/1.1);
    cellupdate();
}

void mcedit_heat::on_pushButton_clicked()
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
