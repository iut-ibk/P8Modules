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

#include "celldialog.h"

mcedit::mcedit(QWidget *parent, int cx, int cy, double sx, double sy) :
    QDialog(parent),
    ui(new Ui::mcedit)
{
    ui->setupUi(this);

    teccol.append(new QColor(4,224,23,255));
    teccol.append(new QColor(179,209,56,255));
    teccol.append(new QColor(7,224,126,255));
    teccol.append(new QColor(181,90,29,255));
    teccol.append(new QColor(9,0,173,255));
    teccol.append(new QColor(140,176,135,255));


    this->cx=cx;
    this->cy=cy;
    this->sx=sx;
    this->sy=sy;

    scene=new McGraphicsScene(this);
    ui->graphicsView->setScene(scene);
    ui->graphicsView->setDragMode(QGraphicsView::RubberBandDrag);
    scene->setSceneRect(0,0,cx*sx,cy*sy);
    bgrect=scene->addRect(0,0,cx*sx,cy*sy);
    changebgcont(0);
    cellmap.clear();
    int pos=0;
    for (int y=0;y<cy;y++)
        for (int x=0;x<cx;x++)
        {
            Cell *cell=new Cell(x*sx,y*sy,sx,sy,scene,pos,&teccol);
            cellmap.insert(cell->getRect(),cell);
            pos++;
        }
    ui->graphicsView->show();
    ui->graphicsView->setMouseTracking(true);

    mode=0;
    viewmode=0;
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
    ui->graphicsView->scale(1.1,1.1);
}

void mcedit::on_pb_zoomout_clicked()
{
    ui->graphicsView->scale(1.0/1.1,1.0/1.1);
}

void mcedit::on_pushButton_clicked()
{
    QString filename=QFileDialog::getOpenFileName(this,"Select background imgage",QDir::currentPath(),"*.png");
    if (!filename.isEmpty())
    {
        pixmap=QPixmap(filename).scaled(cx*sx,cy*sy,Qt::IgnoreAspectRatio,Qt::SmoothTransformation);
        scene->setBackgroundBrush(pixmap);
    }
}

int cellComp (Cell* a,  Cell* b)
{
    return (a->getNo()) < (b->getNo());
}

void mcedit::tecLoad()
{
    QString tfilename=QFileDialog::getOpenFileName(this,"Load mcd",QDir::currentPath(),"*.mcd");
    if (!tfilename.isEmpty())
    {
        filename=tfilename;
        QFile file;
        file.setFileName(filename);
        file.open(QIODevice::ReadOnly|QIODevice::Text);
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
        QString tfilename=QFileDialog::getSaveFileName(this,"Save mcd",QDir::currentPath(),"*.mcd");
        if (!tfilename.isEmpty())
        {
            filename=tfilename;
            tecSave(filename);

        }
    }
}

void mcedit::tecSaveAs()
{
    QString tfilename=QFileDialog::getSaveFileName(this,"Save mcd",QDir::currentPath(),"*.mcd");
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
               << cell->getV(5) << "\n";
    }
    file.close();
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

    double v1=0;
    double v2=0;
    double v3=0;
    double v4=0;
    double v5=0;
    double v6=0;
    CellDialog *dia=new CellDialog(NULL,&v1,&v2,&v3,&v4,&v5,&v6);
    dia->exec();
    foreach (Cell *cell, selectedCells)
    {
        dia->getValues(&v1,&v2,&v3,&v4,&v5,&v6);
        cell->setV(0,v1);
        cell->setV(1,v2);
        cell->setV(2,v3);
        cell->setV(3,v4);
        cell->setV(4,v5);
        cell->setV(5,v6);
    }
    cellupdate();
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
