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