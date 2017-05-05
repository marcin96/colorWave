from PySide import QtGui
from modelsframe import Ui_Models_View
from ModeView import ModeView

class ModelsView(QtGui.QFrame):
    def showModes(self):
        for mode in self.model.modes:
            self.ui.ModesList.addItem(mode.name)

    def Filer(self):
        None

    def add_Mode(self):
        self.showModeAddView()

    def Edit_Mode(self):
        if(self.ui.ModesList.currentItem().text()!="SunnyMode"):
            self.showEditView()

    def Remove_Mode(self):
        if(self.ui.ModesList.currentItem().text()!="SunnyMode"):
            self.model.deleteMode(self.ui.ModesList.currentItem().text())
            self.ui.ModesList.takeItem(self.ui.ModesList.currentRow())

    def getAllModeNames(self):
        names = []
        for mode in self.model.modes:
            names.append(mode.name)
        return names

    def showModeView(self,mode,inherit=False):
        modeView = ModeView(mode,self.model.getAllTags(),inherit)
        modeView.DataUpdateMethod = self.model.update_Mode
        names = self.getAllModeNames()
        if(mode.name==""):
            modeView.Forbidden_names = names
        else:
            names.remove(mode.name)
            modeView.Forbidden_names = names
        for pb in self.parent().children():
            try:
                pb.hide()
            except:print(pb)
        modeView.setParent(self.parent())
        modeView.show()
        self.setParent(None)

    def showModeAddView(self):
        self.showModeView(self.model.create_EmptyMode())

    def showEditView(self):
        self.showModeView(self.model.getModeByName(self.ui.ModesList.currentItem().text()))

    def inherit(self):
        self.showModeView(self.model.getModeByName(self.ui.ModesList.currentItem().text()),inherit=True)

    def change_enabledButtons(self,isit):
        self.ui.RemoveModeBtn.setEnabled(isit)
        self.ui.EditModeBtn.setEnabled(isit)
        self.ui.InheritBtn.setEnabled(isit)
        
    def handleButtonVisibility(self):
        self.change_enabledButtons(True)

    def search(self):
        self.ui.ModesList.clear()
        for mode in self.model.filterModesBySearch(self.ui.SearchModeTxt.text()):
            self.ui.ModesList.addItem(mode)
        self.change_enabledButtons(False)

    def filterByTags(self):
        self.ui.ModesList.clear()
        if(self.ui.TagsComboBox.currentText()=="<All>"):
            self.showModes()
            return
        for mode in self.model.getModesByTag(self.ui.TagsComboBox.currentText()):
            self.ui.ModesList.addItem(mode)
        self.change_enabledButtons(False)

    def destroy(self):
        for pb in self.parent().children():
            try:
                pb.show()
            except:None
        self.setParent(None)

    def __init__(self,model):
        self.model = model
        super(ModelsView,self).__init__()
        self.build_ui()

    def build_ui(self):
        self.ui = Ui_Models_View()
        self.ui.setupUi(self)
        self.ui.addModeBtn.clicked.connect(self.add_Mode)
        self.ui.RemoveModeBtn.clicked.connect(self.Remove_Mode)
        self.ui.EditModeBtn.clicked.connect(self.Edit_Mode)
        self.change_enabledButtons(False)
        self.ui.BackBtn.clicked.connect(self.destroy)
        self.ui.SearchModeTxt.textChanged.connect(self.search)
        self.ui.TagsComboBox.addItem("<All>")
        self.ui.TagsComboBox.addItems(self.model.getAllTags())
        self.ui.TagsComboBox.currentIndexChanged.connect(self.filterByTags)
        self.ui.ModesList.itemSelectionChanged.connect(self.handleButtonVisibility)
        self.ui.InheritBtn.clicked.connect(self.inherit)
        self.showModes()
