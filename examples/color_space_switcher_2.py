import maya.cmds as cmds


def switch_color_space(shadertype, shader_connections_to_fix, colorspace='sRGBin'):
    """
    Switches the color space of all objects found within the maya scene. Only the provided connections will be switched
    to the provided colorspace attribute.

    WARNING: Currently this script only goes 2 layers deep from the shader node!

    Args:
        shader_connections_to_fix: list of shader connections of type "aiStandardSurface" to switch the colorSpace for
        colorspace: string of colorspace attribute to switch to.
    Returns:

    """
    all_shader = sorted(set(cmds.ls(
        [mat for item in cmds.ls(type='shadingEngine') for mat in cmds.listConnections(item) if
         cmds.sets(item, q=True)], materials=True)))

    none_specified_shaders = []

    for shader in all_shader:
        if cmds.nodeType(shader) == shadertype:
            for connection in shader_connections_to_fix:
                all_connections = cmds.listConnections(shader + '.' + connection, source=True, skipConversionNodes=True)

                _set_colorspace_for(all_connections, colorspace)
        else:
            cmds.warning('None aiStandardSurface Shader found. Please replace following shader with a'
                         ' aiStandardSurface = {}'.format(shader))
            none_specified_shaders.append(shader)

    # TODO show all none ai shader


def _show_none_specified_shader_warning(shadertype, none_specified_shaders):
    window_id = 'shader_warnings_window'
    if cmds.window(window_id, exists=True):
        cmds.deleteUI('shader_warnings_window')
        cmds.windowPref('shader_warnings_window', remove=True)
    cmds.window(window_id, title='Unwanted Shader', iconName='Unwanted Shader', widthHeight=(400, 350))
    cmds.frameLayout(label='None specified shaders found that are not from type > {} <'.format(shadertype))

    for bad_shader in none_specified_shaders:
        # TODO create fancy gui item for each bad_shader
        cmds.text(bad_shader)

    cmds.showWindow(window_id)
    return


def _set_colorspace_for(all_connections, colorspace):
    if all_connections:
        print('bla')
        for connection_source in all_connections:
            if cmds.objExists(connection_source + '.colorSpace'):
                cmds.setAttr(connection_source + '.colorSpace', colorspace, type='string')
            else:

                _set_colorspace_for(cmds.listConnections(connection_source, source=True, skipConversionNodes=True),
                                    colorspace)


if __name__ == '__main__':  # pragma: no cover
    switch_color_space('aiStandardSurface', ['metalness', 'specularRoughness'], colorspace='sRGBin')
