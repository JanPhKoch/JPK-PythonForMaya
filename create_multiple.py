import maya.cmds as cmds


class Cubecreator(object):
    use = None

    @classmethod
    def showUI(cls, uiFile):
        win = cls(uiFile)
        win.create()
        return win

    def __init__(self, filePath):
        Cubecreator.use = self
        self.window = 'Cubecreator_window'
        self.cube_amount = 'cube_amount'
        self.uiFile = filePath

    def create(self, verbose=False):
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window)

        self.window = cmds.loadUI(uiFile=self.uiFile, verbose=verbose)

        cmds.showWindow(self.window)

    def createBtnCmd(self, *args):

        ctrlPath = '|'.join([self.window, 'centralwidget', self.cube_amount])

        amount = int(cmds.textField(ctrlPath, q=True, text=True))

        for x in range(amount):
            cmds.polyCube()


win = Cubecreator(r'C:\develop\maya_for_python\create_multiple.ui')

win.create(verbose=True)
