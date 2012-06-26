#ifndef P8BASELINE_H
#define P8BASELINE_H

#include "dmcompilersettings.h"
#include <dmgroup.h>
#include <iostream>

class DM_HELPER_DLL_EXPORT P8BaseLine :public DM::Group
{
    DM_DECLARE_GROUP(P8BaseLine)
public:
    P8BaseLine();
    void run();
    virtual bool createInputDialog();
    void createShape(std::string name);
    void init();
    DM::Module * mux;
};

#endif // P8BASELINE_H
