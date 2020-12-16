import random
import maya.cmds as cmds


def scatter(item_to_scatter):
    """
    This scatters a given list of items

    Args:
         item_to_scatter: list of items to scatter.

    """

    for item in item_to_scatter:
        cmds.setAttr(item + '.translateX', random.randint(0, 100))
        cmds.setAttr(item + '.translateY', random.randint(0, 100))
        cmds.setAttr(item + '.translateZ', random.randint(0, 100))

        cmds.setAttr(item + '.scaleX', random.randint(0, 10))
        cmds.setAttr(item + '.scaleY', random.randint(0, 10))
        cmds.setAttr(item + '.scaleZ', random.randint(0, 10))


def create_items():
    items = []
    for i in range(50):
        cube = cmds.polyCube()[0]
        items.append(cube)
    return items


items = create_items()
scatter(item_to_scatter=items)
