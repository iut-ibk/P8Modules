/**
 * @file
 * @author  Chrisitan Urich <christian.urich@gmail.com>
 * @version 1.0
 * @section LICENSE
 *
 * This file is part of DynaMind
 *
 * Copyright (C) 2011  Christian Urich

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
#include "dmnodefactory.h"
#include "dmmoduleregistry.h"
#include "p8scenariogroup.h"
#include "p8baseline.h"
//#include "p8rain.h"
#include "p8scenario.h"
#include "p8treatment_performance.h"
#include "p8enviromental_benefits.h"
//#include "p8simulation.h"
//#include "p8evaluation.h"
#include "graphicplacement.h"
#include "appendrasterasattribute.h"
#include "p8realisations.h"
#include "p8realisation2.h"
#include "p8microclimate.h"
#include "importrasterdata2.h"
//#include "p8shapemicro.h"
#include "p8microclimate_heat.h"
using namespace std;
using namespace DM;


extern "C" void DM_HELPER_DLL_EXPORT  registerModules(ModuleRegistry *registry)
{
    //registry->addNodeFactory(new NodeFactory<URBAN_FORM>());
   // registry->addNodeFactory(new NodeFactory<P8Rain>());
    //registry->addNodeFactory(new NodeFactory<SCENARIO>());
    registry->addNodeFactory(new NodeFactory<GraphicPlacement>());
    registry->addNodeFactory(new NodeFactory<Treatment_Performance>());
    registry->addNodeFactory(new NodeFactory<Enviromental_Benefits>());
//    registry->addNodeFactory(new NodeFactory<P8Simulation>());
//    registry->addNodeFactory(new NodeFactory<P8Evaluation>());
    registry->addNodeFactory(new NodeFactory<AppendRasterAsAttribute>());
    //registry->addNodeFactory(new NodeFactory<Current_Realisation>());
    //registry->addNodeFactory(new NodeFactory<Current_RealisationModule>());
    registry->addNodeFactory(new NodeFactory<Microclimate>());
    registry->addNodeFactory(new NodeFactory<ImportRasterData2>());
    //registry->addNodeFactory(new NodeFactory<p8shapemicro>());
    registry->addNodeFactory(new NodeFactory<Microclimate_heat>());

}

