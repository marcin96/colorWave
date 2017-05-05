from PySide import QtGui
from mainFrame import Ui_MainWindow

class viewManager(QtGui.QMainWindow):
    
    contentFrame = None
    current_view = None
    def setNewView(self,view):
        self.current_view = view
        self.current_view.ui.setParent(self.contentFrame)
        self.current_view.show()
        
    def __init__(self):
        super(viewManager,self).__init__()
        self.build_ui()
        self.contentFrame = self.ui.getContentFrame()

    def build_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
