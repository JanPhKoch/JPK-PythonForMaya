import maya.cmds as cmds
import pymel.core as pm
import time


def fix_shape_names():
    start = time.time()
    top_nodes = cmds.ls(assemblies=True)

    for node in top_nodes:
        children = pm.listRelatives(node, ad=True)

        for transform in children:
            if pm.nodeType(transform) == 'transform':
                shape = transform.getShape()
                if shape and shape != transform + 'Shape':
                    cmds.rename(str(shape), transform + 'Shape')

    end = time.time()
    print ('!Info: The renaming took: {} seconds.'.format(end-start))


if __name__ == "__main__":
    fix_shape_names()
