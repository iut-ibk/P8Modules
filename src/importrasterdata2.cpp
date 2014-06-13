/**
 * @file
 * @author  Chrisitan Urich <christian.urich@gmail.com>
 * @version 1.0
 * @section LICENSE
 *
 * This file is part of DynaMind
 *
 * Copyright (C) 2012  Christian Urich

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

#include "importrasterdata2.h"
#include <QString>
#include <QFile>
#include <QTextStream>
#include <QStringList>
//DM_DECLARE_NODE_NAME(ImportRasterData2, Modules)
DM_DECLARE_CUSTOM_NODE_NAME(ImportRasterData2,"Land Cover Map (Microclimate)","Scenario Generation")
ImportRasterData2::ImportRasterData2()
{
	multiplier = 1;
	flip = true;
	FileName = "";
	dataname = "";
	appendToStream = false;

	this->addParameter("Filename", DM::FILENAME, &FileName);
	this->addParameter("DataName", DM::STRING, &dataname);
	this->addParameter("Multiplier", DM::DOUBLE, &multiplier);
	this->addParameter("Flip",DM::BOOL, &flip);
	this->addParameter("appendToStream", DM::BOOL, &this->appendToStream);
}

void ImportRasterData2::init()
{
	if (dataname.empty())
		return;

	DM::View data(dataname, DM::RASTERDATA, DM::WRITE);
	std::vector<DM::View> vdata;
	vdata.push_back(data);

	Coords = DM::View("CoordOffset",DM::COMPONENT, DM::WRITE);
	Coords.addAttribute("Xoffset");
	Coords.addAttribute("Yoffset");
	vdata.push_back(Coords);
	if (this->appendToStream)
		vdata.push_back(DM::View("dummy", DM::SUBSYSTEM, DM::READ));

	this->addData("Data", vdata);


}

string ImportRasterData2::getHelpUrl()
{
	return "https://github.com/iut-ibk/DynaMind-BasicModules/blob/master/doc/ImportRasterData.md";
}

void ImportRasterData2::run()
{
	DM::System * sys = this->getData("Data");
	DM::View data(dataname, DM::RASTERDATA, DM::WRITE);
	DM::RasterData * r = this->getRasterData("Data", data);
	QFile file(QString::fromStdString(FileName));



	DM::Component * cmp = new DM::Component();
	sys->addComponent(cmp,Coords);

	QTextStream stream(&file);
	if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
		DM::Logger(DM::Error) << "warning, read input file ";
		return;
	}

	QString line("NULL");

	int LineCounter  = 0;
	int rowCounter = 0;
	int ncols = 0;
	int nrows = 0;
	double xoffset = 0;
	double yoffset = 0;
	double cellsize = 0;
	double NoDataValue = -9999; //default

	//Read Header
	while (!line.isNull() && LineCounter < 6 ) {
		LineCounter++;
		line =stream.readLine();
		if (LineCounter == 1) {
			QStringList list = line.split(QRegExp("\\s+"));
			QString s = QString(list[1]);
			s.replace(",", ".");
			ncols = s.toInt();
		}
		if (LineCounter == 2) {
			QStringList list = line.split(QRegExp("\\s+"));
			QString s = QString(list[1]);
			s.replace(",", ".");
			nrows = s.toInt();
		}
		if (LineCounter == 3) {
			QStringList list = line.split(QRegExp("\\s+"));
			QString s = QString(list[1]);
			s.replace(",", ".");
			xoffset = s.toDouble();
			cmp->addAttribute("Xoffset",xoffset);
		}
		if (LineCounter == 4) {
			QStringList list = line.split(QRegExp("\\s+"));
			QString s = QString(list[1]);
			s.replace(",", ".");
			yoffset = s.toDouble();
			cmp->addAttribute("Yoffset",yoffset);
		}
		if (LineCounter == 5) {
			QStringList list = line.split(QRegExp("\\s+"));
			QString s = QString(list[1]);
			s.replace(",", ".");
			cellsize = s.toDouble() * multiplier;
		}
		if (LineCounter == 6) {
			QStringList list = line.split(QRegExp("\\s+"));
			QString s = QString(list[1]);
			s.replace(",", ".");
			NoDataValue = s.toDouble();
		}
	}
	std::cout <<" Cols " << ncols << std::endl;
	std::cout <<" Rows " << nrows << std::endl;
	std::cout <<" Cellsize " << cellsize << std::endl;
	r->setNoValue(NoDataValue);

	r->setSize(ncols, nrows, cellsize,cellsize,xoffset,yoffset);

	while (!line.isNull()) {
		LineCounter++;
		line =stream.readLine();
		if (LineCounter >= 6 && rowCounter < nrows) {
			QStringList list = line.split(QRegExp("\\s+"));
			for ( int i = 0; i < list.size(); i++ ) {
				QString s = QString(list[i]);
				s.replace(",", ".");
				if (flip)
					r->setCell(i, nrows-rowCounter-1, s.toDouble());
				else
					r->setCell(i, rowCounter, s.toDouble());
			}
			rowCounter++;

		}
	}
	file.close();
}
