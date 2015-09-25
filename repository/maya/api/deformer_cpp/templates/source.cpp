{{language.header}}
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnPlugin.h>
#include <maya/MItGeometry.h>
#include <maya/MPoint.h>

#include "{{basename}}.h"
#include "perlinNoise.hpp"

#define McheckErr(stat, msg)\
if ( MS::kSuccess != stat ) {\
        cerr << msg;\
        return MS::kFailure;\
}

{{project | classify}}::{{project | classify}}() { }

{{project | classify}}::~{{project | classify}}() { }

MStatus {{project | classify}}::deform(MDataBlock &block, MItGeometry &iter, const MMatrix &mat, unsigned int multiIndex) {
    MStatus status = MStatus::kSuccess;

    MDataHandle frequencyData = block.inputValue(a_frequency, &status);
    McheckErr(status, "Error getting frequencý data handle\n");
    double frequency = frequencyData.asDouble();

    MDataHandle multiplierData = block.inputValue(a_multiplier, &status);
    McheckErr(status, "Error getting multiplier data handle\n");
    double multiplier = multiplierData.asDouble();

    MDataHandle envData = block.inputValue(envelope, &status);
    McheckErr(status, "Error getting envelope data handle\n");
    float env = envData.asFloat();

    PerlinNoise<double> perlin;
    for (; !iter.isDone(); iter.next()) {
        MPoint pt = iter.position();
        MVector n = iter.normal();
        MVector dir;
        dir.x = perlin.noise(pt.x * frequency, pt.y * frequency, pt.z * frequency);
        dir.y = perlin.noise(pt.x * frequency + 250, pt.y * frequency + 250, pt.z * frequency + 250);
        dir.z = perlin.noise(pt.x * frequency + 500, pt.y * frequency + 500, pt.z * frequency + 500);
        pt += n * dir.x * multiplier * env;
        iter.setPosition(pt);
    }
    return status;
}

void *{{project | classify}}::creator() {
    return new {{project | classify}}();
}

MStatus {{project | classify}}::initialize() {
    MStatus status;
    MFnNumericAttribute nAttr;

    a_frequency = nAttr.create("frequency", "frq", MFnNumericData::kDouble, 1.0, &status);
    McheckErr(status, "Error creating frequency attribute\n");
    nAttr.setKeyable(true);
    status = addAttribute(a_frequency);
    McheckErr(status, status.errorString().asChar());
    status = attributeAffects(a_frequency, outputGeom);
    McheckErr(status, "Error setting attributeAffects for frequency attribute\n");

    a_multiplier = nAttr.create("multiplier", "m", MFnNumericData::kDouble, 1.0, &status);
    McheckErr(status, "Error creating multiplier attribute\n");
    nAttr.setKeyable(true);
    status = addAttribute(a_multiplier);
    McheckErr(status, "Error adding multiplier attribute\n");
    status = attributeAffects(a_multiplier, outputGeom);
    McheckErr(status, "Error setting attributeAffects for multiplier attribute\n");

    return MS::kSuccess;
}

#pragma GCC visibility push(default)

MStatus initializePlugin(MObject obj) {
    MStatus result;
    MFnPlugin plugin(obj, "Burnhill", "3.0", "Any");
    result = plugin.registerNode("{{project}}", {{project | classify}}::id, {{project | classify}}::creator,
                                 {{project | classify}}::initialize, MPxNode::kDeformerNode);
    return result;
}

#pragma GCC visibility push(default)

MStatus uninitializePlugin(MObject obj) {
    MStatus result;
    MFnPlugin plugin(obj);
    result = plugin.deregisterNode({{project | classify}}::id);
    return result;
}
{{language.footer}}