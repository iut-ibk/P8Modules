#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
class mcedit;

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT
    
public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
    
private slots:
    void on_pushButton_clicked();

    void on_actionExit_triggered();

private:
    Ui::MainWindow *ui;
    mcedit *edit;
};

#endif // MAINWINDOW_H
