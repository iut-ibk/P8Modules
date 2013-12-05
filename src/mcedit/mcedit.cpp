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

#include <QFile>
#include <QTextStream>
#include <QColor>
#include <QRect>
#include <QMessageBox>
#include <QTransform>
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


    this->cx=cx;
    this->cy=cy;
    this->sx=sx;
    this->sy=sy;

    scene=new McGraphicsScene(this);
    ui->graphicsView->setScene(scene);
    ui->graphicsView->setDragMode(QGraphicsView::RubberBandDrag);

    double lx=cx*sx;
    double ly=cy*sy;
    scene->setSceneRect(0,0,lx,ly);
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

    mode=0;
    viewmode=1;
    tecLoad(parent);
    tecLoad(workpath+"/WSUDtech.mcd");
    if (QFile::exists(workpath+"/Reduction in LST.mcd"))
    {
        resLoad(workpath+"/Reduction in LST.mcd");
        ui->cb_mode->setCurrentIndex(1);
    }
    if (!bgimage.isEmpty())
        loadbackground(bgimage);
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
        ui->v7->setValue(selectedCell->getV(5));
        ui->v8->setValue(selectedCell->getV(5));
        ui->v9->setValue(selectedCell->getV(5));
        ui->v10->setValue(selectedCell->getV(5));
        ui->v11->setValue(selectedCell->getV(5));

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


void mcedit::resLoad(QString tfilename)
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
        int linecount=0;
        while (!stream.atEnd())
        {
            stream.readLine();
            linecount++;
        }

        if (linecount==sortlist.size())
        {
            stream.seek(0);
            foreach (Cell *cell, sortlist)
            {
                QStringList linelist=stream.readLine().split(",");
                cell->setRes(0,linelist[1].toDouble());
            }
        }
        else
        {
            foreach (Cell *cell, sortlist)
            {
                cell->setRes(0,0);
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
