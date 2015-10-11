{{language.header}}
#include <maya/MPxDeformerNode.h>

class {{project | classify}} : MPxDeformerNode {

public:
    {{project | classify}}();

    virtual ~{{project | classify}}();
    virtual MStatus deform(MDataBlock &block,
                           MItGeometry &iter,
                           const MMatrix &mat,
                           unsigned int multiIndex);
    static void *creator();
    static MStatus initialize();

public:
    static MTypeId id;
    static MObject a_frequency;
    static MObject a_multiplier;

};
MTypeId {{project | classify}}::id( {{maya.id}} );
MObject {{project | classify}}::a_frequency;
MObject {{project | classify}}::a_multiplier;

{{language.footer}}