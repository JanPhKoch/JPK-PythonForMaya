import maya.cmds as cmds
import maya.mel as mel


def transfer_weights(source_skin=None, selection=None):
    """
    Transfers weights from a given source_skin object to a given selection.

    :param source_skin: source_skin object to copy the weights from
    :param selection: Selection of geo objects to transfer the weights to
    :return:
    """

    if source_skin and selection:
        for destination_skin in selection:
            cmds.copySkinWeights(sourceSkin=source_skin, noMirror=True, destinationSkin=destination_skin)


def get_skincluster_from_selection(selection):
    """
    Gets the skincluster node for every item in a list selection

    :param selection: List of items to get the skincluster from
    :return: list_of_skins: A list of a skinclusters
    """
    list_of_skins = []

    for obj in selection:
        skincluster = mel.eval('findRelatedSkinCluster ' + obj)
        list_of_skins.append(skincluster)

    return list_of_skins


selection = cmds.ls(selection=True)
list_of_skins = get_skincluster_from_selection(selection)
transfer_weights(mel.eval('findRelatedSkinCluster ' + 'c_body_nowings_posed_mesh'), list_of_skins)
