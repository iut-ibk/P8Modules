#ifndef P8ENVIROMENTAL_BENEFITS_H
#define P8ENVIROMENTAL_BENEFITS_H

#include "dmcompilersettings.h"
#include <dmgroup.h>
#include <iostream>
#include <QMap>
#include <QString>

class DM_HELPER_DLL_EXPORT Enviromental_Benefits :public DM::Group
{
    DM_DECLARE_GROUP(Enviromental_Benefits)

    private :
        bool modulesHaveBeenCreated;

public:

    Enviromental_Benefits();
    void run();
    virtual bool createInputDialog();
    void init();
};

#endif // P8TREATMENT_PERFORMANCE_H
