from functools import partial
import random
import maya.cmds as cmds
import pymel.core as pm


class MayaAssetDuplicator:
    def __init__(self):
        self._create_window()

    def _create_window(self):
        # Quick and dirty maya.cmds gui because i was to lazy to build a proper one with qt

        window_id = 'Maya Asset Duplicator'
        if cmds.window(window_id, exists=True):
            cmds.deleteUI(window_id)
            cmds.windowPref(window_id, remove=True)
        window = cmds.window(window_id, title='Maya Asset Duplicator', widthHeight=(350, 350))
        cmds.frameLayout(label='Options:')
        cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, 200), (2, 50), (3, 100)])
        cmds.text(label='Duplicate selected Asset : ')
        self.duplicator_tf = cmds.textField('duplicator_tf')
        cmds.text(label=' times.')
        cmds.setParent('..')

        cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[(1, 350)])
        cmds.setParent('..')
        cmds.separator()

        cmds.button(label='D U P L I C A T E', h=50, command=partial(self._get_user_input),
                    backgroundColor=[random.random(), random.random(), random.random()])
        cmds.separator()

        cmds.showWindow(window)

    def _get_user_input(self, *args):
        """
        Wrapper / helper function when used with the maya gui _create_window to get the user input
        and parse it to the duplicator.
        """
        amount = int(cmds.textField(self.duplicator_tf, query=True, text=True))
        selection = cmds.ls(selection=True)

        if len(selection) > 1:
            raise Exception("To much selected. Please select just one asset!")

        selection = selection[0]

        try:
            print('test')
        except Exception as e:
            print(e)

        self.duplicate_asset(selection, amount)

    def identify_asset_typ(self, asset):
        """
        Helper function to identify how to handle a specific asset based on the way it was imported.
        """
        # reference
        reference_node = cmds.referenceQuery(asset, isNodeReferenced=True)
        if reference_node:
            if ':' in asset:
                ref_namespace = asset.split(':')[0]
            else:
                ref_namespace = ':'
            return {'type': 'reference', 'reference_node': cmds.referenceQuery(asset, rfn=True),
                    'namespace': ref_namespace}

    def duplicate_asset(self, asset, amount):
        """
        Duplicates the given asset by the given amount based on the identified asset typ.

        Args:
            asset: Asset selection user input.
            amount: int amount user input to duplicate the asset by.

        Returns:

        """
        asset_typ = self.identify_asset_typ(asset)

        node_type = asset_typ["type"]
        reference_node = asset_typ["reference_node"]
        reference_namespace = asset_typ["namespace"]

        for i in range(amount):

            if node_type == 'reference':
                # simple duplicate the reference. get the path from the node and create a new reference with it.

                reference_path = cmds.referenceQuery(reference_node, filename=True)

                pm.system.createReference(
                    reference_path,
                    loadReferenceDepth="all",
                    mergeNamespacesOnClash=False,
                    namespace=reference_namespace,
                )


if __name__ == '__main__':
    MayaAssetDuplicator()


class MyException(Exception):
    pass