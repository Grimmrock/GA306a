select -cl  ;
select -r ImportPoly ;
select -r pCylinder1 ;
hyperShadePanelSceneAndGraphTabPopupMenu hyperShadePanel1 collection1HyperShadeEd collection1HyperShadeEdPopupMenu;
hyperShade -assign ImportPoly;
sets -e -forceElement ImportSurfaceShader;
mayaHasRenderSetup;
// 1 // 
// ImportSurfaceShader // 
plugNodeStripped "ImportSurfaceShader";
// ImportSurfaceShader // 
plugNodeStripped "ImportSurfaceShader";
// ImportSurfaceShader // 
setFilterScript "initialShadingGroup";
// 0 // 
setFilterScript "initialParticleSE";
// 0 // 
setFilterScript "defaultLightSet";
// 1 // 
setFilterScript "defaultObjectSet";
// 1 // 
setFilterScript "ImportSurfaceShader";
// 0 // 
mayaHasRenderSetup;
// 1 // 
setUITemplate -pst attributeEditorTemplate;
// attributeEditorTemplate // 
setParent hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|shadingEngineFormLayout|columnLayout117;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|shadingEngineFormLayout|columnLayout117 // 
AEswatchDisplayReplace surfaceShader1SG( "ImportSurfaceShader.message" );
setParent hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|shadingEngineFormLayout|scrollLayout23|columnLayout118|frameLayout153|columnLayout119|columnLayout120;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|shadingEngineFormLayout|scrollLayout23|columnLayout118|frameLayout153|columnLayout119|columnLayout120 // 
AEshadingEngineShadersReplace( "ImportSurfaceShader.surfaceShader", "ImportSurfaceShader.volumeShader", "ImportSurfaceShader.imageShader", "ImportSurfaceShader.displacementShader", "ImportSurfaceShader.defaultShadows" );
defaultNavigation -dtv -d ImportSurfaceShader.surfaceShader;
// ImportPoly // 
setUITemplate -ppt;
// NONE // 
refreshAE;
getUIComponentDockControl("Tool Settings", false);
// ToolSettings // 
showHelp -docs "CommandsPython/hyperShade.html";
if(!`exists "showHelpErrPromptIfRequired"`){ eval("source \"initHelp.mel\"");} showHelpErrPromptIfRequired "showHelp -d CommandsPython/hyperShade.html";
// 0 // 
checkHelpLanguageMismatch;
// 0 // 
// http://www.autodesk.com/maya-help-2018-enu/index.html?contextId=COMMANDSPYTHON-HYPERSHADE // 
import maya.cmds as mc
import maya.mel as ml

def selectAll():
   geometry = mc.ls(geometry=True)

   transforms = mc.listRelatives(geometry, p=True, path=True)

   mc.select(transforms, r=True)

selectAll();

ImportPoly = mc.shadingNode('blinn', asShader=True, name = 'ImportPoly',)
print (ImportPoly)

ImportPolySS = mc.sets(renderable=True,noSurfaceShader=True,empty=True, name = 'ImportSurfaceShader')
print (ImportPolySS)

mc.connectAttr(ImportPoly+'.outColor', ImportPolySS+'.surfaceShader');

selectAll();

mc.hyperShade(assign = ImportPoly)
ImportPoly1
mayaHasRenderSetup;
// 1 // 
ImportSurfaceShader1
sets -e -forceElement ImportSurfaceShader1;
mayaHasRenderSetup;
// 1 // 
// ImportSurfaceShader1 // 
plugNodeStripped "ImportPoly1";
// ImportPoly1 // 
plugNodeStripped "ImportPoly1";
// ImportPoly1 // 
plugNodeStripped "ImportSurfaceShader1";
// ImportSurfaceShader1 // 
plugNodeStripped "ImportSurfaceShader1";
// ImportSurfaceShader1 // 
evalDeferred -lp "hyperShadeRefreshActiveNode";
evalDeferred -lp "hyperShadeRefreshActiveNode";
plugNodeStripped "ImportSurfaceShader1";
// ImportSurfaceShader1 // 
plugNodeStripped "ImportSurfaceShader1";
// ImportSurfaceShader1 // 
plugNodeStripped "ImportSurfaceShader";
// ImportSurfaceShader // 
plugNodeStripped "ImportSurfaceShader";
// ImportSurfaceShader // 
plugNodeStripped "ImportPoly1";
// ImportPoly1 // 
plugNodeStripped "ImportPoly1";
// ImportPoly1 // 
lsThroughFilter -na DefaultMaterialsAndShaderGlowFilter7 -sort byName -reverse false;
// ImportPoly ImportPoly1 lambert1 particleCloud1 shaderGlow1 // 
setFilterScript "initialShadingGroup";
// 0 // 
setFilterScript "initialParticleSE";
// 0 // 
setFilterScript "defaultLightSet";
// 1 // 
setFilterScript "defaultObjectSet";
// 1 // 
setFilterScript "ImportSurfaceShader";
// 0 // 
setFilterScript "ImportSurfaceShader1";
// 0 // 
mayaHasRenderSetup;
// 1 // 
setUITemplate -pst attributeEditorTemplate;
// attributeEditorTemplate // 
setParent hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|shadingEngineFormLayout|columnLayout117;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|shadingEngineFormLayout|columnLayout117 // 
AEswatchDisplayReplace surfaceShader1SG( "ImportSurfaceShader.message" );
setParent hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|shadingEngineFormLayout|scrollLayout23|columnLayout118|frameLayout153|columnLayout119|columnLayout120;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|shadingEngineFormLayout|scrollLayout23|columnLayout118|frameLayout153|columnLayout119|columnLayout120 // 
AEshadingEngineShadersReplace( "ImportSurfaceShader.surfaceShader", "ImportSurfaceShader.volumeShader", "ImportSurfaceShader.imageShader", "ImportSurfaceShader.displacementShader", "ImportSurfaceShader.defaultShadows" );
defaultNavigation -dtv -d ImportSurfaceShader.surfaceShader;
// ImportPoly // 
setUITemplate -ppt;
// NONE // 
refreshAE;
autoUpdateAttrEd;
updateAnimLayerEditor("AnimLayerTab");
statusLineUpdateInputField;
if (!`exists polyNormalSizeMenuUpdate`) {eval "source buildDisplayMenu";} polyNormalSizeMenuUpdate;
dR_updateCounter;
uvTkUpdateSelectionCompInfo;
uvTkResolveAndUpdateTrees;
hyperShadeSelectionChangedCallback;
dR_updateCommandPanel;
doUpdatePropertyPanel("hyperShadePanel1dockStation|propertyPanelForm|ppRoot", "hyperShadePropertyPanelSelectionCallback" , "hyperShadePropertyPanelActiveNodeCallback", "hyperShadeNodeDeletedCallback", "hyperShadeNodeNameChangedCallback" , 1);
modelEditor -e -aog "" $gShaderBallEditor;
// modelEditor2 // 
attrColorSliderGrp -label "Color" -attribute ImportPoly1.color;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout59|frameLayout366|columnLayout333|frameLayout367|columnLayout334|attrColorSliderGrp315 // 
attrColorSliderGrp -label "Transparency" -attribute ImportPoly1.transparency;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout59|frameLayout366|columnLayout333|frameLayout367|columnLayout334|attrColorSliderGrp316 // 
attrColorSliderGrp -label "Ambient Color" -attribute ImportPoly1.ambientColor;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout59|frameLayout366|columnLayout333|frameLayout367|columnLayout334|attrColorSliderGrp317 // 
attrColorSliderGrp -label "Incandescence" -attribute ImportPoly1.incandescence;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout59|frameLayout366|columnLayout333|frameLayout367|columnLayout334|attrColorSliderGrp318 // 
attrColorSliderGrp -label "Specular Color" -attribute ImportPoly1.specularColor;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout59|frameLayout366|columnLayout333|frameLayout368|columnLayout335|attrColorSliderGrp319 // 
attrColorSliderGrp -label "Reflected Color" -attribute ImportPoly1.reflectedColor;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout59|frameLayout366|columnLayout333|frameLayout368|columnLayout335|attrColorSliderGrp320 // 
plugNodeStripped "ImportSurfaceShader1";
// ImportSurfaceShader1 // 
plugNodeStripped "ImportSurfaceShader1";
// ImportSurfaceShader1 // 
plugNodeStripped "ImportSurfaceShader";
// ImportSurfaceShader // 
plugNodeStripped "ImportSurfaceShader";
// ImportSurfaceShader // 
setFilterScript "initialShadingGroup";
// 0 // 
setFilterScript "initialParticleSE";
// 0 // 
setFilterScript "defaultLightSet";
// 1 // 
setFilterScript "defaultObjectSet";
// 1 // 
setFilterScript "ImportSurfaceShader";
// 0 // 
setFilterScript "ImportSurfaceShader1";
// 0 // 
mayaHasRenderSetup;
// 1 // 
setUITemplate -pst attributeEditorTemplate;
// attributeEditorTemplate // 
setParent hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|shadingEngineFormLayout|columnLayout117;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|shadingEngineFormLayout|columnLayout117 // 
AEswatchDisplayReplace surfaceShader1SG( "ImportSurfaceShader.message" );
setParent hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|shadingEngineFormLayout|scrollLayout23|columnLayout118|frameLayout153|columnLayout119|columnLayout120;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|shadingEngineFormLayout|scrollLayout23|columnLayout118|frameLayout153|columnLayout119|columnLayout120 // 
AEshadingEngineShadersReplace( "ImportSurfaceShader.surfaceShader", "ImportSurfaceShader.volumeShader", "ImportSurfaceShader.imageShader", "ImportSurfaceShader.displacementShader", "ImportSurfaceShader.defaultShadows" );
defaultNavigation -dtv -d ImportSurfaceShader.surfaceShader;
// ImportPoly // 
setUITemplate -ppt;
// NONE // 
refreshAE;
dR_setModelEditorTypes;
hyperShadeRefreshActiveNode;
hyperShadeRefreshActiveNode;
ml.eval('MLdeleteUnused;')
MLdeleteUnused;
delete "ImportSurfaceShader";
evalDeferred -lp "hyperShadeRefreshActiveNode";
evalDeferred -lp "hyperShadeRefreshActiveNode";
delete "ImportPoly";
evalDeferred -lp "hyperShadeRefreshActiveNode";
// 2 // 
# 2L # 
lsThroughFilter -na DefaultMaterialsAndShaderGlowFilter7 -sort byName -reverse false;
// ImportPoly1 lambert1 particleCloud1 shaderGlow1 // 
setFilterScript "initialShadingGroup";
// 0 // 
setFilterScript "initialParticleSE";
// 0 // 
setFilterScript "defaultLightSet";
// 1 // 
setFilterScript "defaultObjectSet";
// 1 // 
setFilterScript "ImportSurfaceShader1";
// 0 // 
mayaHasRenderSetup;
// 1 // 
refreshAE;
hyperShadeRefreshActiveNode;
hyperShadeRefreshActiveNode;
hyperShadeRefreshActiveNode;
hyperShadePanelSetActiveTabLayout hyperShadePanel1 firstPaneTabs false;
nodeReleaseCallback collection1HyperShadeEd ImportPoly1 none;
select -r ImportPoly1 ;
mayaHasRenderSetup;
// 1 // 
autoUpdateAttrEd;
updateAnimLayerEditor("AnimLayerTab");
statusLineUpdateInputField;
if (!`exists polyNormalSizeMenuUpdate`) {eval "source buildDisplayMenu";} polyNormalSizeMenuUpdate;
dR_updateCounter;
uvTkUpdateSelectionCompInfo;
uvTkResolveAndUpdateTrees;
hyperShadeSelectionChangedCallback;
dR_updateCommandPanel;
doUpdatePropertyPanel("hyperShadePanel1dockStation|propertyPanelForm|ppRoot", "hyperShadePropertyPanelSelectionCallback" , "hyperShadePropertyPanelActiveNodeCallback", "hyperShadeNodeDeletedCallback", "hyperShadeNodeNameChangedCallback" , 1);
attrColorSliderGrp -label "Color" -attribute ImportPoly1.color;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout60|frameLayout372|columnLayout339|frameLayout373|columnLayout340|attrColorSliderGrp321 // 
attrColorSliderGrp -label "Transparency" -attribute ImportPoly1.transparency;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout60|frameLayout372|columnLayout339|frameLayout373|columnLayout340|attrColorSliderGrp322 // 
attrColorSliderGrp -label "Ambient Color" -attribute ImportPoly1.ambientColor;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout60|frameLayout372|columnLayout339|frameLayout373|columnLayout340|attrColorSliderGrp323 // 
attrColorSliderGrp -label "Incandescence" -attribute ImportPoly1.incandescence;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout60|frameLayout372|columnLayout339|frameLayout373|columnLayout340|attrColorSliderGrp324 // 
attrColorSliderGrp -label "Specular Color" -attribute ImportPoly1.specularColor;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout60|frameLayout372|columnLayout339|frameLayout374|columnLayout341|attrColorSliderGrp325 // 
attrColorSliderGrp -label "Reflected Color" -attribute ImportPoly1.reflectedColor;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout60|frameLayout372|columnLayout339|frameLayout374|columnLayout341|attrColorSliderGrp326 // 
delete;
evalDeferred -lp "hyperShadeRefreshActiveNode";
modelEditor -e -aog "" $gShaderBallEditor;
// modelEditor2 // 
plugNodeStripped "ImportSurfaceShader1";
// ImportSurfaceShader1 // 
plugNodeStripped "ImportSurfaceShader1";
// ImportSurfaceShader1 // 
lsThroughFilter -na DefaultMaterialsAndShaderGlowFilter7 -sort byName -reverse false;
// lambert1 particleCloud1 shaderGlow1 // 
setFilterScript "initialShadingGroup";
// 0 // 
setFilterScript "initialParticleSE";
// 0 // 
setFilterScript "defaultLightSet";
// 1 // 
setFilterScript "defaultObjectSet";
// 1 // 
setFilterScript "ImportSurfaceShader1";
// 0 // 
mayaHasRenderSetup;
// 1 // 
propertyPanelOnNodeDeleteCB "ImportPoly1" "hyperShadePanel1dockStation|propertyPanelForm|ppRoot" "hyperShadePropertyPanelSelectionCallback" "hyperShadePropertyPanelActiveNodeCallback" "hyperShadeNodeDeletedCallback" "hyperShadeNodeNameChangedCallback" false;
dR_setModelEditorTypes;
autoUpdateAttrEd;
updateAnimLayerEditor("AnimLayerTab");
statusLineUpdateInputField;
if (!`exists polyNormalSizeMenuUpdate`) {eval "source buildDisplayMenu";} polyNormalSizeMenuUpdate;
dR_updateCounter;
uvTkUpdateSelectionCompInfo;
uvTkResolveAndUpdateTrees;
hyperShadeSelectionChangedCallback;
dR_updateCommandPanel;
updatePropertyPanel "hyperShadePanel1dockStation|propertyPanelForm|ppRoot" "hyperShadePropertyPanelSelectionCallback" "hyperShadePropertyPanelActiveNodeCallback" "hyperShadeNodeDeletedCallback" "hyperShadeNodeNameChangedCallback" 0;
doUpdatePropertyPanel("hyperShadePanel1dockStation|propertyPanelForm|ppRoot", "hyperShadePropertyPanelSelectionCallback" , "hyperShadePropertyPanelActiveNodeCallback", "hyperShadeNodeDeletedCallback", "hyperShadeNodeNameChangedCallback" , 1);
doUpdatePropertyPanel("hyperShadePanel1dockStation|propertyPanelForm|ppRoot", "hyperShadePropertyPanelSelectionCallback" , "hyperShadePropertyPanelActiveNodeCallback", "hyperShadeNodeDeletedCallback", "hyperShadeNodeNameChangedCallback" , 0);
hyperShadeRefreshActiveNode;
modelEditor -e -aog "" $gShaderBallEditor;
// modelEditor2 // 
setFilterScript "initialShadingGroup";
// 0 // 
setFilterScript "initialParticleSE";
// 0 // 
setFilterScript "defaultLightSet";
// 1 // 
setFilterScript "defaultObjectSet";
// 1 // 
setFilterScript "ImportSurfaceShader1";
// 0 // 
mayaHasRenderSetup;
// 1 // 
dR_setModelEditorTypes;
getUIComponentDockControl("Tool Settings", false);
// ToolSettings // 
select -r pCylinder1 ;
mayaHasRenderSetup;
// 1 // 
autoUpdateAttrEd;
updateAnimLayerEditor("AnimLayerTab");
statusLineUpdateInputField;
if (!`exists polyNormalSizeMenuUpdate`) {eval "source buildDisplayMenu";} polyNormalSizeMenuUpdate;
dR_updateCounter;
uvTkUpdateSelectionCompInfo;
uvTkResolveAndUpdateTrees;
hyperShadeSelectionChangedCallback;
dR_updateCommandPanel;
doUpdatePropertyPanel("hyperShadePanel1dockStation|propertyPanelForm|ppRoot", "hyperShadePropertyPanelSelectionCallback" , "hyperShadePropertyPanelActiveNodeCallback", "hyperShadeNodeDeletedCallback", "hyperShadeNodeNameChangedCallback" , 1);
defaultNavigation -source lambert1 -destination |pCylinder1|pCylinderShape1.instObjGroups[0] -connectToExisting;
connectNodeToAttrOverride("lambert1", "pCylinderShape1.instObjGroups[0]");
// 1 // 
sets -edit -forceElement initialShadingGroup |pCylinder1|pCylinderShape1;
mayaHasRenderSetup;
// 1 // 
// initialShadingGroup // 
// Dropped lambert1 onto pCylinder1 // 
plugNodeStripped "ImportSurfaceShader1";
// ImportSurfaceShader1 // 
plugNodeStripped "ImportSurfaceShader1";
// ImportSurfaceShader1 // 
setFilterScript "initialShadingGroup";
// 0 // 
setFilterScript "initialParticleSE";
// 0 // 
setFilterScript "defaultLightSet";
// 1 // 
setFilterScript "defaultObjectSet";
// 1 // 
setFilterScript "ImportSurfaceShader1";
// 0 // 
mayaHasRenderSetup;
// 1 // 
getUIComponentDockControl("Tool Settings", false);
// ToolSettings // 
select -cl  ;
mayaHasRenderSetup;
// 1 // 
getUIComponentDockControl("Tool Settings", false);
// ToolSettings // 
autoUpdateAttrEd;
updateAnimLayerEditor("AnimLayerTab");
statusLineUpdateInputField;
if (!`exists polyNormalSizeMenuUpdate`) {eval "source buildDisplayMenu";} polyNormalSizeMenuUpdate;
dR_updateCounter;
uvTkUpdateSelectionCompInfo;
uvTkResolveAndUpdateTrees;
hyperShadeSelectionChangedCallback;
dR_updateCommandPanel;
doUpdatePropertyPanel("hyperShadePanel1dockStation|propertyPanelForm|ppRoot", "hyperShadePropertyPanelSelectionCallback" , "hyperShadePropertyPanelActiveNodeCallback", "hyperShadeNodeDeletedCallback", "hyperShadeNodeNameChangedCallback" , 1);
import maya.cmds as mc
import maya.mel as ml

def selectAll():
   geometry = mc.ls(geometry=True)

   transforms = mc.listRelatives(geometry, p=True, path=True)

   mc.select(transforms, r=True)

selectAll();

ImportPoly = mc.shadingNode('blinn', asShader=True, name = 'ImportPoly',)
print (ImportPoly)

ImportPolySS = mc.sets(renderable=True,noSurfaceShader=True,empty=True, name = 'ImportSurfaceShader')
print (ImportPolySS)

mc.connectAttr(ImportPoly+'.outColor', ImportPolySS+'.surfaceShader');

selectAll();

mc.hyperShade(assign = ImportPoly)

ImportPoly
mayaHasRenderSetup;
// 1 // 
ImportSurfaceShader
sets -e -forceElement ImportSurfaceShader;
mayaHasRenderSetup;
// 1 // 
// ImportSurfaceShader // 
plugNodeStripped "ImportPoly";
// ImportPoly // 
plugNodeStripped "ImportPoly";
// ImportPoly // 
plugNodeStripped "ImportSurfaceShader";
// ImportSurfaceShader // 
plugNodeStripped "ImportSurfaceShader";
// ImportSurfaceShader // 
evalDeferred -lp "hyperShadeRefreshActiveNode";
evalDeferred -lp "hyperShadeRefreshActiveNode";
lsThroughFilter -na DefaultMaterialsAndShaderGlowFilter7 -sort byName -reverse false;
// ImportPoly lambert1 particleCloud1 shaderGlow1 // 
plugNodeStripped "ImportSurfaceShader";
// ImportSurfaceShader // 
plugNodeStripped "ImportSurfaceShader";
// ImportSurfaceShader // 
plugNodeStripped "ImportPoly";
// ImportPoly // 
plugNodeStripped "ImportPoly";
// ImportPoly // 
setFilterScript "initialShadingGroup";
// 0 // 
setFilterScript "initialParticleSE";
// 0 // 
setFilterScript "defaultLightSet";
// 1 // 
setFilterScript "defaultObjectSet";
// 1 // 
setFilterScript "ImportSurfaceShader1";
// 0 // 
setFilterScript "ImportSurfaceShader";
// 0 // 
mayaHasRenderSetup;
// 1 // 
refreshAE;
autoUpdateAttrEd;
updateAnimLayerEditor("AnimLayerTab");
statusLineUpdateInputField;
if (!`exists polyNormalSizeMenuUpdate`) {eval "source buildDisplayMenu";} polyNormalSizeMenuUpdate;
dR_updateCounter;
uvTkUpdateSelectionCompInfo;
uvTkResolveAndUpdateTrees;
hyperShadeSelectionChangedCallback;
dR_updateCommandPanel;
doUpdatePropertyPanel("hyperShadePanel1dockStation|propertyPanelForm|ppRoot", "hyperShadePropertyPanelSelectionCallback" , "hyperShadePropertyPanelActiveNodeCallback", "hyperShadeNodeDeletedCallback", "hyperShadeNodeNameChangedCallback" , 1);
modelEditor -e -aog "" $gShaderBallEditor;
// modelEditor2 // 
attrColorSliderGrp -label "Color" -attribute ImportPoly.color;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout61|frameLayout378|columnLayout345|frameLayout379|columnLayout346|attrColorSliderGrp327 // 
attrColorSliderGrp -label "Transparency" -attribute ImportPoly.transparency;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout61|frameLayout378|columnLayout345|frameLayout379|columnLayout346|attrColorSliderGrp328 // 
attrColorSliderGrp -label "Ambient Color" -attribute ImportPoly.ambientColor;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout61|frameLayout378|columnLayout345|frameLayout379|columnLayout346|attrColorSliderGrp329 // 
attrColorSliderGrp -label "Incandescence" -attribute ImportPoly.incandescence;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout61|frameLayout378|columnLayout345|frameLayout379|columnLayout346|attrColorSliderGrp330 // 
attrColorSliderGrp -label "Specular Color" -attribute ImportPoly.specularColor;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout61|frameLayout378|columnLayout345|frameLayout380|columnLayout347|attrColorSliderGrp331 // 
attrColorSliderGrp -label "Reflected Color" -attribute ImportPoly.reflectedColor;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout61|frameLayout378|columnLayout345|frameLayout380|columnLayout347|attrColorSliderGrp332 // 
plugNodeStripped "ImportSurfaceShader";
// ImportSurfaceShader // 
plugNodeStripped "ImportSurfaceShader";
// ImportSurfaceShader // 
setFilterScript "initialShadingGroup";
// 0 // 
setFilterScript "initialParticleSE";
// 0 // 
setFilterScript "defaultLightSet";
// 1 // 
setFilterScript "defaultObjectSet";
// 1 // 
setFilterScript "ImportSurfaceShader1";
// 0 // 
setFilterScript "ImportSurfaceShader";
// 0 // 
mayaHasRenderSetup;
// 1 // 
dR_setModelEditorTypes;
hyperShadeRefreshActiveNode;
hyperShadeRefreshActiveNode;
select -cl  ;
mayaHasRenderSetup;
// 1 // 
autoUpdateAttrEd;
updateAnimLayerEditor("AnimLayerTab");
statusLineUpdateInputField;
if (!`exists polyNormalSizeMenuUpdate`) {eval "source buildDisplayMenu";} polyNormalSizeMenuUpdate;
dR_updateCounter;
uvTkUpdateSelectionCompInfo;
uvTkResolveAndUpdateTrees;
hyperShadeSelectionChangedCallback;
dR_updateCommandPanel;
doUpdatePropertyPanel("hyperShadePanel1dockStation|propertyPanelForm|ppRoot", "hyperShadePropertyPanelSelectionCallback" , "hyperShadePropertyPanelActiveNodeCallback", "hyperShadeNodeDeletedCallback", "hyperShadeNodeNameChangedCallback" , 1);
attrColorSliderGrp -label "Color" -attribute ImportPoly.color;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout62|frameLayout384|columnLayout351|frameLayout385|columnLayout352|attrColorSliderGrp333 // 
attrColorSliderGrp -label "Transparency" -attribute ImportPoly.transparency;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout62|frameLayout384|columnLayout351|frameLayout385|columnLayout352|attrColorSliderGrp334 // 
attrColorSliderGrp -label "Ambient Color" -attribute ImportPoly.ambientColor;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout62|frameLayout384|columnLayout351|frameLayout385|columnLayout352|attrColorSliderGrp335 // 
attrColorSliderGrp -label "Incandescence" -attribute ImportPoly.incandescence;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout62|frameLayout384|columnLayout351|frameLayout385|columnLayout352|attrColorSliderGrp336 // 
attrColorSliderGrp -label "Specular Color" -attribute ImportPoly.specularColor;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout62|frameLayout384|columnLayout351|frameLayout386|columnLayout353|attrColorSliderGrp337 // 
attrColorSliderGrp -label "Reflected Color" -attribute ImportPoly.reflectedColor;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout62|frameLayout384|columnLayout351|frameLayout386|columnLayout353|attrColorSliderGrp338 // 
defaultNavigation -source lambert1 -destination |pCylinder1|pCylinderShape1.instObjGroups[0] -connectToExisting;
connectNodeToAttrOverride("lambert1", "pCylinderShape1.instObjGroups[0]");
// 1 // 
sets -edit -forceElement initialShadingGroup |pCylinder1|pCylinderShape1;
mayaHasRenderSetup;
// 1 // 
// initialShadingGroup // 
// Dropped lambert1 onto pCylinder1 // 
plugNodeStripped "ImportSurfaceShader";
// ImportSurfaceShader // 
plugNodeStripped "ImportSurfaceShader";
// ImportSurfaceShader // 
setFilterScript "initialShadingGroup";
// 0 // 
setFilterScript "initialParticleSE";
// 0 // 
setFilterScript "defaultLightSet";
// 1 // 
setFilterScript "defaultObjectSet";
// 1 // 
setFilterScript "ImportSurfaceShader1";
// 0 // 
setFilterScript "ImportSurfaceShader";
// 0 // 
mayaHasRenderSetup;
// 1 // 
getUIComponentDockControl("Tool Settings", false);
// ToolSettings // 
getUIComponentDockControl("Tool Settings", false);
// ToolSettings // 
hyperShadePanelSetActiveTabLayout hyperShadePanel1 firstPaneTabs false;
getUIComponentDockControl("Tool Settings", false);
// ToolSettings // 
nodeReleaseCallback collection1HyperShadeEd ImportPoly none;
select -r ImportPoly ;
mayaHasRenderSetup;
// 1 // 
autoUpdateAttrEd;
updateAnimLayerEditor("AnimLayerTab");
statusLineUpdateInputField;
if (!`exists polyNormalSizeMenuUpdate`) {eval "source buildDisplayMenu";} polyNormalSizeMenuUpdate;
dR_updateCounter;
uvTkUpdateSelectionCompInfo;
uvTkResolveAndUpdateTrees;
hyperShadeSelectionChangedCallback;
dR_updateCommandPanel;
doUpdatePropertyPanel("hyperShadePanel1dockStation|propertyPanelForm|ppRoot", "hyperShadePropertyPanelSelectionCallback" , "hyperShadePropertyPanelActiveNodeCallback", "hyperShadeNodeDeletedCallback", "hyperShadeNodeNameChangedCallback" , 1);
attrColorSliderGrp -label "Color" -attribute ImportPoly.color;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout63|frameLayout390|columnLayout357|frameLayout391|columnLayout358|attrColorSliderGrp339 // 
attrColorSliderGrp -label "Transparency" -attribute ImportPoly.transparency;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout63|frameLayout390|columnLayout357|frameLayout391|columnLayout358|attrColorSliderGrp340 // 
attrColorSliderGrp -label "Ambient Color" -attribute ImportPoly.ambientColor;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout63|frameLayout390|columnLayout357|frameLayout391|columnLayout358|attrColorSliderGrp341 // 
attrColorSliderGrp -label "Incandescence" -attribute ImportPoly.incandescence;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout63|frameLayout390|columnLayout357|frameLayout391|columnLayout358|attrColorSliderGrp342 // 
attrColorSliderGrp -label "Specular Color" -attribute ImportPoly.specularColor;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout63|frameLayout390|columnLayout357|frameLayout392|columnLayout359|attrColorSliderGrp343 // 
attrColorSliderGrp -label "Reflected Color" -attribute ImportPoly.reflectedColor;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|blinnFormLayout|scrollLayout63|frameLayout390|columnLayout357|frameLayout392|columnLayout359|attrColorSliderGrp344 // 
delete;
evalDeferred -lp "hyperShadeRefreshActiveNode";
modelEditor -e -aog "" $gShaderBallEditor;
// modelEditor2 // 
plugNodeStripped "ImportSurfaceShader";
// ImportSurfaceShader // 
plugNodeStripped "ImportSurfaceShader";
// ImportSurfaceShader // 
lsThroughFilter -na DefaultMaterialsAndShaderGlowFilter7 -sort byName -reverse false;
// lambert1 particleCloud1 shaderGlow1 // 
setFilterScript "initialShadingGroup";
// 0 // 
setFilterScript "initialParticleSE";
// 0 // 
setFilterScript "defaultLightSet";
// 1 // 
setFilterScript "defaultObjectSet";
// 1 // 
setFilterScript "ImportSurfaceShader1";
// 0 // 
setFilterScript "ImportSurfaceShader";
// 0 // 
mayaHasRenderSetup;
// 1 // 
dR_setModelEditorTypes;
propertyPanelOnNodeDeleteCB "ImportPoly" "hyperShadePanel1dockStation|propertyPanelForm|ppRoot" "hyperShadePropertyPanelSelectionCallback" "hyperShadePropertyPanelActiveNodeCallback" "hyperShadeNodeDeletedCallback" "hyperShadeNodeNameChangedCallback" false;
autoUpdateAttrEd;
updateAnimLayerEditor("AnimLayerTab");
statusLineUpdateInputField;
if (!`exists polyNormalSizeMenuUpdate`) {eval "source buildDisplayMenu";} polyNormalSizeMenuUpdate;
dR_updateCounter;
uvTkUpdateSelectionCompInfo;
uvTkResolveAndUpdateTrees;
hyperShadeSelectionChangedCallback;
dR_updateCommandPanel;
updatePropertyPanel "hyperShadePanel1dockStation|propertyPanelForm|ppRoot" "hyperShadePropertyPanelSelectionCallback" "hyperShadePropertyPanelActiveNodeCallback" "hyperShadeNodeDeletedCallback" "hyperShadeNodeNameChangedCallback" 0;
doUpdatePropertyPanel("hyperShadePanel1dockStation|propertyPanelForm|ppRoot", "hyperShadePropertyPanelSelectionCallback" , "hyperShadePropertyPanelActiveNodeCallback", "hyperShadeNodeDeletedCallback", "hyperShadeNodeNameChangedCallback" , 1);
doUpdatePropertyPanel("hyperShadePanel1dockStation|propertyPanelForm|ppRoot", "hyperShadePropertyPanelSelectionCallback" , "hyperShadePropertyPanelActiveNodeCallback", "hyperShadeNodeDeletedCallback", "hyperShadeNodeNameChangedCallback" , 0);
hyperShadeRefreshActiveNode;
modelEditor -e -aog "" $gShaderBallEditor;
// modelEditor2 // 
setFilterScript "initialShadingGroup";
// 0 // 
setFilterScript "initialParticleSE";
// 0 // 
setFilterScript "defaultLightSet";
// 1 // 
setFilterScript "defaultObjectSet";
// 1 // 
setFilterScript "ImportSurfaceShader1";
// 0 // 
setFilterScript "ImportSurfaceShader";
// 0 // 
mayaHasRenderSetup;
// 1 // 
dR_setModelEditorTypes;
mayaHasRenderSetup;
// 1 // 
autoUpdateAttrEd;
updateAnimLayerEditor("AnimLayerTab");
statusLineUpdateInputField;
if (!`exists polyNormalSizeMenuUpdate`) {eval "source buildDisplayMenu";} polyNormalSizeMenuUpdate;
dR_updateCounter;
uvTkUpdateSelectionCompInfo;
uvTkResolveAndUpdateTrees;
hyperShadeSelectionChangedCallback;
dR_updateCommandPanel;
doUpdatePropertyPanel("hyperShadePanel1dockStation|propertyPanelForm|ppRoot", "hyperShadePropertyPanelSelectionCallback" , "hyperShadePropertyPanelActiveNodeCallback", "hyperShadeNodeDeletedCallback", "hyperShadeNodeNameChangedCallback" , 1);
modelEditor -e -aog "" $gShaderBallEditor;
// modelEditor2 // 
setUITemplate -pst attributeEditorTemplate;
// attributeEditorTemplate // 
setParent hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|shadingEngineFormLayout|columnLayout117;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|shadingEngineFormLayout|columnLayout117 // 
AEswatchDisplayReplace surfaceShader1SG( "ImportSurfaceShader1.message" );
setParent hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|shadingEngineFormLayout|scrollLayout23|columnLayout118|frameLayout153|columnLayout119|columnLayout120;
// hyperShadePanel1dockStation|propertyPanelForm|ppRoot|ppDoSelection|ppSelected|ppControls|shadingEngineFormLayout|scrollLayout23|columnLayout118|frameLayout153|columnLayout119|columnLayout120 // 
AEshadingEngineShadersReplace( "ImportSurfaceShader1.surfaceShader", "ImportSurfaceShader1.volumeShader", "ImportSurfaceShader1.imageShader", "ImportSurfaceShader1.displacementShader", "ImportSurfaceShader1.defaultShadows" );
setUITemplate -ppt;
// propertyPanelUITemplate // 
setFilterScript "initialShadingGroup";
// 0 // 
setFilterScript "initialParticleSE";
// 0 // 
setFilterScript "defaultLightSet";
// 1 // 
setFilterScript "defaultObjectSet";
// 1 // 
setFilterScript "ImportSurfaceShader1";
// 0 // 
setFilterScript "ImportSurfaceShader";
// 0 // 
mayaHasRenderSetup;
// 1 // 
dR_setModelEditorTypes;
hyperShadePanelKeyPressCmd "hyperShadePrimaryNodeEditor" "Del";
delete ImportSurfaceShader1 ImportSurfaceShader;
evalDeferred -lp "hyperShadeRefreshActiveNode";
evalDeferred -lp "hyperShadeRefreshActiveNode";
// 1 // 
setFilterScript "initialShadingGroup";
// 0 // 
setFilterScript "initialParticleSE";
// 0 // 
setFilterScript "defaultLightSet";
// 1 // 
setFilterScript "defaultObjectSet";
// 1 // 
mayaHasRenderSetup;
// 1 // 
refreshAE;
propertyPanelOnNodeDeleteCB "ImportSurfaceShader1" "hyperShadePanel1dockStation|propertyPanelForm|ppRoot" "hyperShadePropertyPanelSelectionCallback" "hyperShadePropertyPanelActiveNodeCallback" "hyperShadeNodeDeletedCallback" "hyperShadeNodeNameChangedCallback" false;
propertyPanelOnNodeDeleteCB "ImportSurfaceShader" "hyperShadePanel1dockStation|propertyPanelForm|ppRoot" "hyperShadePropertyPanelSelectionCallback" "hyperShadePropertyPanelActiveNodeCallback" "hyperShadeNodeDeletedCallback" "hyperShadeNodeNameChangedCallback" false;
autoUpdateAttrEd;
updateAnimLayerEditor("AnimLayerTab");
statusLineUpdateInputField;
if (!`exists polyNormalSizeMenuUpdate`) {eval "source buildDisplayMenu";} polyNormalSizeMenuUpdate;
dR_updateCounter;
uvTkUpdateSelectionCompInfo;
uvTkResolveAndUpdateTrees;
hyperShadeSelectionChangedCallback;
hyperShadePanelKeyReleaseCmd "hyperShadePrimaryNodeEditor" "Del";
// 0 // 
dR_updateCommandPanel;
updatePropertyPanel "hyperShadePanel1dockStation|propertyPanelForm|ppRoot" "hyperShadePropertyPanelSelectionCallback" "hyperShadePropertyPanelActiveNodeCallback" "hyperShadeNodeDeletedCallback" "hyperShadeNodeNameChangedCallback" 0;
updatePropertyPanel "hyperShadePanel1dockStation|propertyPanelForm|ppRoot" "hyperShadePropertyPanelSelectionCallback" "hyperShadePropertyPanelActiveNodeCallback" "hyperShadeNodeDeletedCallback" "hyperShadeNodeNameChangedCallback" 0;
doUpdatePropertyPanel("hyperShadePanel1dockStation|propertyPanelForm|ppRoot", "hyperShadePropertyPanelSelectionCallback" , "hyperShadePropertyPanelActiveNodeCallback", "hyperShadeNodeDeletedCallback", "hyperShadeNodeNameChangedCallback" , 1);
doUpdatePropertyPanel("hyperShadePanel1dockStation|propertyPanelForm|ppRoot", "hyperShadePropertyPanelSelectionCallback" , "hyperShadePropertyPanelActiveNodeCallback", "hyperShadeNodeDeletedCallback", "hyperShadeNodeNameChangedCallback" , 0);
doUpdatePropertyPanel("hyperShadePanel1dockStation|propertyPanelForm|ppRoot", "hyperShadePropertyPanelSelectionCallback" , "hyperShadePropertyPanelActiveNodeCallback", "hyperShadeNodeDeletedCallback", "hyperShadeNodeNameChangedCallback" , 0);
hyperShadeRefreshActiveNode;
modelEditor -e -aog "" $gShaderBallEditor;
// modelEditor2 // 
setFilterScript "initialShadingGroup";
// 0 // 
setFilterScript "initialParticleSE";
// 0 // 
setFilterScript "defaultLightSet";
// 1 // 
setFilterScript "defaultObjectSet";
// 1 // 
mayaHasRenderSetup;
// 1 // 
dR_setModelEditorTypes;
hyperShadeRefreshActiveNode;
// Warning: file: C:/Program Files/Autodesk/Maya2018/scripts/startup/scriptEditorPanel.mel line 946: The -keyEquivalent/-ke flag has been removed. Keys can be set using the Hotkey Editor. // 
// Warning: file: C:/Program Files/Autodesk/Maya2018/scripts/startup/scriptEditorPanel.mel line 947: The -keyEquivalent/-ke flag has been removed. Keys can be set using the Hotkey Editor. // 
// Warning: file: C:/Program Files/Autodesk/Maya2018/scripts/startup/scriptEditorPanel.mel line 948: The -keyEquivalent/-ke flag has been removed. Keys can be set using the Hotkey Editor. // 
// Warning: file: C:/Program Files/Autodesk/Maya2018/scripts/startup/scriptEditorPanel.mel line 949: The -keyEquivalent/-ke flag has been removed. Keys can be set using the Hotkey Editor. // 
// Warning: file: C:/Program Files/Autodesk/Maya2018/scripts/startup/scriptEditorPanel.mel line 1007: The -keyEquivalent/-ke flag has been removed. Keys can be set using the Hotkey Editor. // 
SelectAll();
# Error: name 'SelectAll' is not defined
# Traceback (most recent call last):
#   File "<maya console>", line 1, in <module>
# NameError: name 'SelectAll' is not defined # 
mc.SelectAll()
CreatePolygonCube;
polyCube -w 1 -h 1 -d 1 -sx 1 -sy 1 -sz 1 -ax 0 1 0 -cuv 4 -ch 1;
// Result: pCube1 polyCube1 // 
CreatePolygonCube;
polyCube -w 1 -h 1 -d 1 -sx 1 -sy 1 -sz 1 -ax 0 1 0 -cuv 4 -ch 1;
// Result: pCube2 polyCube2 // 
select -r pCube1 ;
move -r 0 5.456524 0 ;
select -r pCube2 ;
move -r 0 -7.540436 0 ;
select -cl  ;
mc.SelectAll()
select -cl  ;
select -r pCylinder1 pCube1 pCube2 ;
move -r -5.985528 0 0 ;
move -r 0 7.530637 0 ;
move -r 0 0 -7.38049 ;
select -cl  ;
// Undo: select -cl   // 
// Undo: move -r 0 0 -7.38049  // 
// Undo: move -r 0 7.530637 0  // 
// Undo: move -r -5.985528 0 0  // 
move -r 0 9.540436 0 pCylinder1.scalePivot pCylinder1.rotatePivot pCube1.scalePivot pCube1.rotatePivot pCube2.scalePivot pCube2.rotatePivot ;
SnapToGridRelease; dR_enterForSnap;
// Undo: move -r 0 9.540436 0 pCylinder1.scalePivot pCylinder1.rotatePivot pCube1.scalePivot pCube1.rotatePivot pCube2.scalePivot pCube2.rotatePivot  // 
select -cl  ;
select -r pCylinder1 pCube1 pCube2 ;
FreezeTransformations;
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
select -cl  ;
select -r pCylinder1 pCube1 pCube2 ;
select -cl  ;
select -r pCylinder1 ;
select -r pCylinder1 pCube1 pCube2 ;
select -cl  ;
select -r pCylinder1 pCube1 pCube2 ;

mc.SelectAll()
def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel)
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True))
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)
# Error: invalid syntax
#   File "<maya console>", line 8
#     def CenterPiv_Funct(m_sel= mc.ls(sl=True))
#                                              ^
# SyntaxError: invalid syntax # 
def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel)
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True)

def CenterPiv_Funct(m_sel= mc.ls(sl=True))
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)

# Error: invalid syntax
#   File "<maya console>", line 8
#     def CenterPiv_Funct(m_sel= mc.ls(sl=True))
#       ^
# SyntaxError: invalid syntax # 
def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel)
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)
select -cl  ;
select -r pCylinder1 ;
select -r pCube2 pCube1 pCylinder1 ;
CenterPiv_Funct(m_sel= mc.ls(sl=True))
select -cl  ;
select -r pCube2 ;
select -r group1 ;
select -r pCube2 ;
select -r pCube1 ;
select -r pCylinder1 ;
select -r pCube1 ;
select -r -ne defaultLightSet ;
select -r pCube2 ;
select -r pCube1 ;
select -r pCylinder1 ;
select -cl  ;
select -r group1 ;
pickWalk -d up;
// Result: group1 // 
print(bbox)
# Error: name 'bbox' is not defined
# Traceback (most recent call last):
#   File "<maya console>", line 1, in <module>
# NameError: name 'bbox' is not defined # 
def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)\
   print(bbox)

# Error: invalid syntax
#   File "<maya console>", line 6
#     print(bbox)
#         ^
# SyntaxError: invalid syntax # 
def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)\
   print(bbox)



CenterPiv_Funct(m_sel= mc.ls(sl=True))
# Error: invalid syntax
#   File "<maya console>", line 6
#     print(bbox)
#         ^
# SyntaxError: invalid syntax # 
GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)
   print(bbox)



CenterPiv_Funct(m_sel= mc.ls(sl=True))

[-0.9999998807907104, -8.040435791015625, -0.9999998807907104, 1.0, 5.95652437210083, 0.9999999403953552]
select -r group2 ;
move -r 0 13.971718 0 ;
move -r 0 12.063002 0 ;
// Undo: move -r 0 12.063002 0  // 
move -r 0 6.542195 0 ;
// Undo: move -r 0 6.542195 0  // 
select -r group1 ;
move -r 0 -3.108837 0 ;
// Undo: move -r 0 -3.108837 0  // 
select -r group2 ;
select -r group1 ;
select -r group2 ;
select -r pCube1 ;
select -r pCylinder1 ;
select -r pCylinder1 pCube1 pCube2 ;
parent -w;
// Result: pCylinder1 pCube1 pCube2 // 
select -r group2 ;
select -r pCube2 pCube1 pCylinder1 ;
mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel)
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', n= null)
mc.parent(addObject= True, relative = True,)
# Error: name 'null' is not defined
# Traceback (most recent call last):
#   File "<maya console>", line 17, in <module>
# NameError: name 'null' is not defined # 
move -r 0 -0.00565328 0 ;
select -r pCylinder1 ;
select -r pCube1 ;
select -r pCube2 ;
select -r group1 ;
select -r pCylinder1 ;
select -r pCylinder1 pCube1 pCube2 ;
parent -w;
// Result: pCylinder1 pCube1 pCube2 // 
// Error: file: C:/Program Files/Autodesk/Maya2018/scripts/others/fluidSetSubVolumeLocation.mel line 40: No fluids selected // 
select -r group1 ;
mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel)
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = null)
mc.parent(addObject= True, relative = True,)
# Error: name 'null' is not defined
# Traceback (most recent call last):
#   File "<maya console>", line 17, in <module>
# NameError: name 'null' is not defined # 
select -r pCylinder1 ;
select -r pCylinder1 pCube1 pCube2 ;
parent -w;
// Result: pCylinder1 pCube1 pCube2 // 
select -r group1 ;
select -r pCube1 pCube2 pCylinder1 ;
mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel)
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]print(bbox)
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
# Error: invalid syntax
#   File "<maya console>", line 12
#     bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]print(bbox)
#                                                                         ^
# SyntaxError: invalid syntax # 
mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel)
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]print(bbox)
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
# Error: invalid syntax
#   File "<maya console>", line 12
#     bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]print(bbox)
#                                                                         ^
# SyntaxError: invalid syntax # 
mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel)
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]print(bbox)
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
# Error: invalid syntax
#   File "<maya console>", line 12
#     bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]print(bbox)
#                                                                         ^
# SyntaxError: invalid syntax # 
mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel)
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]print(bbox)
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
# Error: invalid syntax
#   File "<maya console>", line 12
#     bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]print(bbox)
#                                                                         ^
# SyntaxError: invalid syntax # 
mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel)
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2])
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
# Error: invalid syntax
#   File "<maya console>", line 12
#     bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2])
#                                                                     ^
# SyntaxError: invalid syntax # 
mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel)
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2])
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
# Error: invalid syntax
#   File "<maya console>", line 12
#     bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2])
#                                                                     ^
# SyntaxError: invalid syntax # 
mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel)
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2])
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
# Error: invalid syntax
#   File "<maya console>", line 12
#     bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2])
#                                                                     ^
# SyntaxError: invalid syntax # 
mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel)
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2])
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
# Error: invalid syntax
#   File "<maya console>", line 12
#     bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2])
#                                                                     ^
# SyntaxError: invalid syntax # 
mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel)
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2])
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
# Error: invalid syntax
#   File "<maya console>", line 12
#     bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2])
#                                                                     ^
# SyntaxError: invalid syntax # 
mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel)
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2])
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
# Error: invalid syntax
#   File "<maya console>", line 12
#     bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2])
#                                                                     ^
# SyntaxError: invalid syntax # 
select -cl  ;
mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel)
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2])
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')

# Error: invalid syntax
#   File "<maya console>", line 12
#     bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2])
#                                                                     ^
# SyntaxError: invalid syntax # 
mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel)
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
mc.parentConstraint('null', 'highPoly', mo=false)
# Error: name 'false' is not defined
# Traceback (most recent call last):
#   File "<maya console>", line 1, in <module>
# NameError: name 'false' is not defined # 
mc.parentConstraint('null', 'highPoly', mo=False)
# Error: No object matches name: highPoly
# Traceback (most recent call last):
#   File "<maya console>", line 1, in <module>
# ValueError: No object matches name: highPoly # 
select -r null ;
select -r group1 ;
rename "group1" "highPoly";
// Result: highPoly // 
select -r -ne defaultObjectSet ;
mc.parentConstraint('null', 'highPoly', mo=False)
# Result: [u'highPoly_parentConstraint1'] # 
select -r null ;
select -r highPoly_parentConstraint1 ;
select -r null ;
select -r pCylinder1 ;
select -r pCube2 ;
select -r pCube2 pCube1 pCylinder1 ;
parent -w;
// Result: pCube2 pCube1 pCylinder1 // 
select -r highPoly ;
select -r pCube2 ;
select -cl  ;
mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel, name = 'highPoly')
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
mc.parentConstraint('null', 'highPoly', mo=False)
select -cl  ;
// Undo: select -cl   // 
// Undo: mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel, name = 'highPoly')
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
mc.parentConstraint('null', 'highPoly', mo=False) // 
select -r pCube1 pCube2 pCylinder1 ;
move -r 0 6.080258 0 ;
select -cl  ;
select -r pCube1 pCube2 pCylinder1 ;
move -r 5.94646 0 0 ;
select -cl  ;
// Undo: select -cl   // 
// Undo: move -r 5.94646 0 0  // 
move -r 0 0 -5.707733 ;
select -cl  ;
select -r pCube1 pCube2 pCylinder1 ;
move -r -6.429879 0 0 ;
select -cl  ;

mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel, name = 'highPoly')
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
mc.parentConstraint('null', 'highPoly', mo=False)
select -r highPoly_parentConstraint1 ;
mc.delete(OffsetPC)
# Error: name 'OffsetPC' is not defined
# Traceback (most recent call last):
#   File "<maya console>", line 1, in <module>
# NameError: name 'OffsetPC' is not defined # 
select -cl  ;
select -r pCylinder1 ;
select -r pCube1 pCylinder1 ;
select -cl  ;
// Undo: select -cl   // 
// Undo: select -r pCube1 pCylinder1  // 
// Undo: select -r pCylinder1  // 
// Undo: select -cl   // 
// Undo: select -r highPoly_parentConstraint1  // 
// Undo: 
mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel, name = 'highPoly')
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
mc.parentConstraint('null', 'highPoly', mo=False) // 
select -r pCube1 pCylinder1 pCube2 ;
def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel, name = 'highPoly')
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
OffsetPC = mc.parentConstraint('null', 'highPoly', mo=False)
mc.delete('null')
mc.delete(OffsetPC)
# Error: No object matches name: [u'highPoly_parentConstraint1']
# Traceback (most recent call last):
#   File "<maya console>", line 18, in <module>
# ValueError: No object matches name: [u'highPoly_parentConstraint1'] # 
select -r highPoly ;
select -r pCylinder1 ;
select -r pCube1 ;
select -r pCube2 ;
select -r highPoly ;
select -cl  ;
select -r pCube2 pCylinder1 pCube1 ;
move -r -4.653231 0 0 ;
move -r 0 0 -6.223316 ;
move -r 0 7.163329 0 ;
FreezeTransformations;
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
select -r pCylinder1 ;
select -r pCube1 ;
select -r pCube1 pCylinder1 pCube2 ;
parent -w;
// Result: pCube1 pCylinder1 pCube2 // 
select -r highPoly ;
select -r pCube2 pCylinder1 pCube1 ;
FreezeTransformations;
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
select -cl  ;
mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel, name = 'highPoly')
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
OffsetPC = mc.parentConstraint('null', 'highPoly', mo=False)[0]
mc.delete('null')
mc.delete(OffsetPC)
# Error: No object matches name: highPoly_parentConstraint1
# Traceback (most recent call last):
#   File "<maya console>", line 20, in <module>
# ValueError: No object matches name: highPoly_parentConstraint1 # 
// Undo: mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel, name = 'highPoly')
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
OffsetPC = mc.parentConstraint('null', 'highPoly', mo=False)[0]
mc.delete('null')
mc.delete(OffsetPC) // 
// Undo: select -cl   // 
// Undo: FreezeTransformations // 
select -cl  ;
mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel, name = 'highPoly')
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
OffsetPC = mc.parentConstraint('null', 'highPoly', mo=False)[0]
select -r highPoly_parentConstraint1 ;
# Error: invalid syntax
#   File "<maya console>", line 2
#     if '',' in locals():locals()['',']
#          ^
# SyntaxError: invalid syntax # 
# Error: invalid syntax
#   File "<maya console>", line 2
#     if '('' in locals():locals()['('']
#                                      ^
# SyntaxError: invalid syntax # 
# Error: invalid syntax
#   File "<maya console>", line 2
#     if '('' in locals():locals()['('']
#                                      ^
# SyntaxError: invalid syntax # 
mc.parentConstraint('highPoly', edit = True, rm= True)
# Result: [u'highPoly_parentConstraint1'] # 
select -cl  ;
mc.parentConstraint('highPoly', edit = True, rm= True)
# Result: [u'highPoly_parentConstraint1'] # 
mc.parentConstraint('null', 'highPoly', edit = True, rm= True)
select -r pCube1 pCylinder1 pCube2 ;
move -r 5.388472 0 0 ;
move -r 0 0 -11.375601 ;
move -r 0 10.016448 0 ;
parent -w;
// Result: pCube1 pCylinder1 pCube2 // 
FreezeTransformations;
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
select -r null ;
select -add highPoly ;
select -r pCube1 pCylinder1 pCube2 ;
select -cl  ;
import maya.cmds as mc
import maya.mel as ml

                                                #start of texture Assignment 
## maya 2018 built a mother fucking select all fucntion into the code. this is useless now. def selectAll():
   #geometry = mc.ls(geometry=True)

   #transforms = mc.listRelatives(geometry, p=True, path=True)

   #mc.select(transforms, r=True)

mc.SelectAll()

ImportPoly = mc.shadingNode('blinn', asShader=True, name = 'ImportPoly',)
print (ImportPoly)

ImportPolySS = mc.sets(renderable=True,noSurfaceShader=True,empty=True, name = 'ImportSurfaceShader')
print (ImportPolySS)

mc.connectAttr(ImportPoly+'.outColor', ImportPolySS+'.surfaceShader');

selectAll();

mc.hyperShade(assign = ImportPoly)

ml.eval('MLdeleteUnused;')

#End of Texture Assignment

                                                    #start of Grouping and Centerbottom Piv

mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel, name = 'highPoly')
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
mc.parentConstraint('null', 'highPoly', mo=False)[0]
mc.parentConstraint('null', 'highPoly', edit = True, rm= True)
mc.delete('null')
ImportPoly
ImportSurfaceShader
sets -e -forceElement ImportSurfaceShader;
// Result: ImportSurfaceShader // 
select -r pCube1 ;
select -r pCylinder1 ;
select -cl  ;
select -r pCube2 ;
select -cl; select -r pCylinderShape1 pCubeShape2 pCubeShape1;
select -cl  ;
select -cl; select -r pCylinderShape1 pCubeShape2 pCubeShape1;
select -cl  ;
select -r pCylinder1 ;
select -cl  ;
select -r pCylinder1 pCube1 pCube2 ;
move -r 6.102102 0 0 ;
move -r 0 0 -4.976585 ;
move -r 0 10.504895 0 ;
parent -w;
// Result: pCylinder1 pCube1 pCube2 // 
FreezeTransformations;
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
select -r highPoly ;
popupMenu -e -deleteAllItems collection1HyperShadeEdPopupMenu;
// Result: collection1HyperShadeEdPopupMenu // 
select -r pCylinder1 pCube1 pCube2 ;
shadingNode -asShader phong;
// Result: phong1 // 
sets -renderable true -noSurfaceShader true -empty -name phong1SG;
// Result: phong1SG // 
connectAttr -f phong1.outColor phong1SG.surfaceShader;
// Result: Connected phong1.outColor to phong1SG.surfaceShader. // 
shadingNode -asShader phong;
// Result: phong2 // 
sets -renderable true -noSurfaceShader true -empty -name phong2SG;
// Result: phong2SG // 
connectAttr -f phong2.outColor phong2SG.surfaceShader;
// Result: Connected phong2.outColor to phong2SG.surfaceShader. // 
select -cl  ;
select -r pCylinder1 pCube1 pCube2 ;
sets -e -forceElement initialShadingGroup;
// Result: initialShadingGroup // 
select -cl  ;
select -r pCylinder1 pCube1 pCube2 ;
import maya.cmds as mc
import maya.mel as ml

                                                #start of texture Assignment 
## maya 2018 built a mother fucking select all fucntion into the code. this is useless now. def selectAll():
   #geometry = mc.ls(geometry=True)

   #transforms = mc.listRelatives(geometry, p=True, path=True)

   #mc.select(transforms, r=True)

mc.SelectAll()

ImportPoly = mc.shadingNode('blinn', asShader=True, name = 'ImportPoly',)
print (ImportPoly)

ImportPolySS = mc.sets(renderable=True,noSurfaceShader=True,empty=True, name = 'ImportSurfaceShader')
print (ImportPolySS)

mc.connectAttr(ImportPoly+'.outColor', ImportPolySS+'.surfaceShader');

selectAll();

mc.hyperShade(assign = ImportPoly)

ml.eval('MLdeleteUnused;')

#End of Texture Assignment

                                                    #start of Grouping and Centerbottom Piv

mc.SelectAll()

def GroupImport_Funct ( m_sel = mc.ls(sl = True)):
   mc.group(m_sel, name = 'highPoly')
   mc.CenterPivot(m_sel)

GroupImport_Funct(m_sel = mc.ls(sl = True))

def CenterPiv_Funct(m_sel= mc.ls(sl=True)):
   bbox = mc.exactWorldBoundingBox(m_sel)
   bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
   mc.xform(m_sel, piv=bottom, ws= True)


CenterPiv_Funct(m_sel= mc.ls(sl=True))

mc.createNode('transform', name = 'null')
mc.parentConstraint('null', 'highPoly', mo=False)[0]
mc.parentConstraint('null', 'highPoly', edit = True, rm= True)
mc.delete('null')

ImportPoly1
ImportSurfaceShader1
sets -e -forceElement ImportSurfaceShader1;
// Result: ImportSurfaceShader1 // 
delete "ImportSurfaceShader";
delete "phong1SG";
delete "phong2SG";
delete "ImportPoly";
delete "phong1";
delete "phong2";
// Error: file: C:/Program Files/Autodesk/Maya2018/scripts/startup/cutCopyPaste.mel line 114: Nothing is currently selected. // 
