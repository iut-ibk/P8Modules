#ifndef P8TREATMENT_PERFORMANCE_H
#define P8TREATMENT_PERFORMANCE_H

#include "dmcompilersettings.h"
#include <dmgroup.h>
#include <iostream>
#include <QMap>
#include <QString>

class DM_HELPER_DLL_EXPORT Treatment_Performance :public DM::Group
{
    DM_DECLARE_GROUP(Treatment_Performance)

    private :
        bool modulesHaveBeenCreated;

public:

    Treatment_Performance();
    void run();
    virtual bool createInputDialog();
    void init();
};

#endif // P8TREATMENT_PERFORMANCE_H
