import maya.cmds as cmds
#from rigging import create_cntrl_on_selected


cmds.window(title='create joints along curve')
cmds.rowColumnLayout(nr=2)
cmds.text(l='joint amount:')
joint_countIF = cmds.intField(v=5)
cmds.button(l="create", w=150, c="main()")
cmds.showWindow()


def main():
    joint_list = create_jnt_along_curve()
    root = get_lowest_jnt(joint_list)
    parent_joints(root, joint_list)
    #orient_joints(root)
    #create_cntrl_on_selected.auto_rig_parent_constraint('cntrl')


def create_jnt_along_curve():
    selected_curve = cmds.ls(sl=True)[0]
    joint_count = cmds.intField(joint_countIF, q=True, v=True)

    print joint_count

    prev_jnt = ''
    root = ''

    joint_list = []

    for i in range(0, joint_count):
        curve = cmds.select(cl=True)
        jnt = cmds.joint()
        motionpath = cmds.pathAnimation(jnt, c=selected_curve, fractionMode=True)
        cmds.cutKey(motionpath + ".u", time=())
        cmds.setAttr(motionpath + ".u", i * (1.0 / (joint_count - 1)))

        cmds.delete(jnt + '.tx', icn=True)
        cmds.delete(jnt + '.ty', icn=True)
        cmds.delete(jnt + '.tz', icn=True)
        cmds.delete(motionpath)

        joint_list.append(jnt)

        # if i == 0:
        #    prev_jnt = jnt
        #    root = jnt
        #    continue

        # cmds.parent(jnt, prev_jnt)
        # prev_jnt = jnt

    # cmds.joint(root, e=True, oj="xyz", sao= "yup", ch=True, zso=True)

    return joint_list


def parent_joints(root, joint_list):
    joint_list_smaller = [joint for i, joint in enumerate(joint_list) if i < root['index']]
    joint_list_bigger = [joint for i, joint in enumerate(joint_list) if i > root['index']]

    prev_jnt = ''

    for i, jnt in reversed(list(enumerate(joint_list_smaller))):
        if i == (len(joint_list_smaller) - 1):
            prev_jnt = root['name']

        cmds.parent(jnt, prev_jnt)
        prev_jnt = jnt

    prev_jnt = ''

    for i, jnt in enumerate(joint_list_bigger):
        if i == 0:
            prev_jnt = root['name']

        cmds.parent(jnt, prev_jnt)
        prev_jnt = jnt


def get_lowest_jnt(joint_list):
    lowest_ty = ''
    lowest_jnt = {'index': 0,
                  'name': ''}
    for i, jnt in enumerate(joint_list):
        ty = cmds.getAttr(jnt + '.ty')

        if i == 0:
            lowest_ty = ty

        if lowest_ty > ty:
            lowest_ty = ty
            lowest_jnt['index'] = i
            lowest_jnt['name'] = jnt

    return lowest_jnt

