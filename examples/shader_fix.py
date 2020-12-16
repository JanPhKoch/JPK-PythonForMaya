import maya.cmds as cmds


def main():

    get_all_ai_shader()

"""
get all ai shaders of the scene
plug some stuff different
change some values on the shader


"""


def get_all_ai_shader():
    aiAmbientOcclusion_fix = create_ambient_occulusion_node()

    all_objects = cmds.ls()
    for object in all_objects:
        nodeType = cmds.nodeType(object)
        if nodeType == 'aiStandardSurface':
            print object, nodeType
            cmds.connectAttr('%s.outColor' % aiAmbientOcclusion_fix, '%s.baseColor' % object, force=True)
        if nodeType == 'alSurface':
            print object, nodeType
            cmds.connectAttr('%s.outColor' % aiAmbientOcclusion_fix, '%s.diffuseColor' % object, force=True)


def create_ambient_occulusion_node():
    aiAmbientOcclusion_fix = cmds.createNode('aiAmbientOcclusion', n='aiAmbientOcclusion_fix')
    # todo: add shading group to be able to see the shader probably connected within the hypershade
    #ai_sg = cmds.createNode('shadingEngine', n='aiAmbientOcclusion_fix_sg')
    #cmds.connectAttr('%s.outColor' % aiAmbientOcclusion_fix, '%s.surfaceShader' % ai_sg, force=True)

    # set samples to 9
    cmds.setAttr('aiAmbientOcclusion_fix.samples', 9)

    return aiAmbientOcclusion_fix













"""
import maya.cmds as cmds

def currentSelectionPolygonal(obj):

    shapeNode = cmds.listRelatives(obj, shapes=True)
    nodeType = cmds.nodeType(shapeNode)

    if nodeType == "mesh":
        return True

    return False

def checkSelection():
    selectedObjs = cmds.ls(selection=True)

    if (len(selectedObjs) < 1):
        cmds.error('Please select an object')

    lastSelected = selectedObjs[-1]

    isPolygon = currentSelectionPolygonal(lastSelected)

    if (isPolygon):
        print('FOUND POLYGON')
    else:
"""