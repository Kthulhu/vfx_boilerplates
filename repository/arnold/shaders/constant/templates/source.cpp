#include <ai.h>
AI_SHADER_NODE_EXPORT_METHODS({{project}}Mtd);

enum {{project}}Params {
   p_color,
   p_alpha
};

node_parameters
{
   AiParameterRGB("color",  1.0f, 1.0f, 1.0f);
   AiParameterFLT("alpha", 1.0f);

   AiMetaDataSetStr(mds, NULL, "description", "Constant.");
   AiMetaDataSetStr(mds, NULL, "maya.name", "{{project}}");
   AiMetaDataSetInt(mds, NULL, "maya.id", {{arnold.maya_id}});
   AiMetaDataSetStr(mds, NULL, "maya.classification", "shader/surface");

   AiMetaDataSetFlt(mds, "alpha", "softmin", 0.0);
   AiMetaDataSetFlt(mds, "alpha", "softmax", 1.0);
}

node_initialize
{
}

node_update
{
}

node_finish
{
}

shader_evaluate
{
   AtColor attr_color = AiShaderEvalParamRGB(p_color);
   float attr_alpha = AiShaderEvalParamFlt(p_alpha);
   AtRGBA result = AI_RGBA_BLACK;
   result.r = attr_color.r;
   result.g = attr_color.g;
   result.b = attr_color.b;
   result.a = attr_alpha;

   sg->out.RGBA = result;
}

node_loader
{
   if (i > 0)
      return FALSE;
   node->methods      = {{project}}Mtd;
   node->output_type  = AI_TYPE_RGBA;
   node->name         = "{{project}}";
   node->node_type    = AI_NODE_SHADER;
   strcpy(node->version, AI_VERSION);
   return TRUE;
}