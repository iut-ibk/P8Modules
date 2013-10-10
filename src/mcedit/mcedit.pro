#-------------------------------------------------
#
# Project created by QtCreator 2013-10-03T10:03:57
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = mcedit
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    mcedit.cpp \
    cell.cpp \
    celldialog.cpp \
    mcgraphicscene.cpp

HEADERS  += mainwindow.h \
    mcedit.h \
    cell.h \
    celldialog.h \
    mcgraphicscene.h

FORMS    += mainwindow.ui \
    mcedit.ui \
    celldialog.ui

RESOURCES += \
    images.qrc
