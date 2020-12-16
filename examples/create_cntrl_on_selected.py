import maya.cmds as cmds


def auto_rig_parent_constraint(copy_cntrl):
    """
    This function takes a given curve and copies + connects it with (parent-constraint) list of objects.

    :copy_cntrl: cntrl that should be copied + connect with all objects within the object_list
    :return:
    """
    selection = cmds.ls(selection=True)
    object_list = cmds.listRelatives(selection, allDescendents=True)

    for object in object_list:
        cntrl = cmds.duplicate(copy_cntrl)
        point_constraint = cmds.pointConstraint(object, cntrl)
        cmds.delete(point_constraint)
        cmds.makeIdentity(cntrl, apply=True, translate=True)
        cmds.DeleteHistory(cntrl)
        cmds.parentConstraint(cntrl, object, maintainOffset=True)


auto_rig_parent_constraint('cntrl')


def function(text, zahl):
    """

    :param text: text als string
    :param zahl: zahl als int
    :return:
    """