import maya.cmds as cmds
import pymel.core as pm
import time


def fix_shape_names():
    start = time.time()
    selection = cmds.ls(selection=True)

    for node in selection:
        children = cmds.listRelatives(node, ad=True)

        for shape in children:
            if 'Shape' in shape:
                if shape == node + 'ShapeDeformed':
                    print shape
                else:
                    print 'delete me' + shape
                    cmds.delete(shape)

    end = time.time()
    print ('!Info: The renaming took: {} seconds.'.format(end - start))


def strip_deformed():
    start = time.time()
    selection = cmds.ls(selection=True)

    for node in selection:
        children = cmds.listRelatives(node, ad=True)

        for shape in children:
            if 'Shape' in shape:
                if shape == node + 'ShapeDeformed':
                    cmds.rename(shape, shape[:-8])

    end = time.time()
    print ('!Info: The renaming took: {} seconds.'.format(end - start))


if __name__ == "__main__":
    fix_shape_names()
    strip_deformed()
