from PySide import QtGui
from modeEditFrame import Ui_ModeNewEdit
import Modus
import Breakpoint
import tag

NAMEERR_MSG = "Wrong name format"
BREAKPOINTERR_MSG = "Wrong breakpoints count"
NAME_CONDITION = "Please conside the mode has to have a unique name. And it can't have no name."
BREAKPOINTS_CONDITION = "You must have at least 2 breakpoints and not more than 9."

class ModeView(QtGui.QFrame):
    mode = None
    DataUpdateMethod = None
    Forbidden_names = []
    def getTags(self):
        ret = []
        tags_text = self.ui.TagsTxt.toPlainText()
        tgs = tags_text.split(",")
        for i in tgs:
            if(i!=" "):
                ret.append(tag.Tag(str(i).lower().strip()))
        return ret

    def getbreakpoints(self):
        breakpoints = []
        for Belem in self.ui.breakpointElements:
            breakpoints.append(Breakpoint.Breakpoint(Belem.value(),Belem.time))
            print(Belem.value(),Belem.time)
        return breakpoints

    def check_name(self):
        name = self.ui.NameTxt.text()
        print(name)
        if(name.strip()==""):
            print("Hual")
            return False
        for forb in self.Forbidden_names:
            if(name.lower().strip()==forb.lower().strip()):
                print("HULA")
                return False
        return True

    def check_Breakpoints(self):
        length = len(self.ui.breakpointElements)
        if(length>=2 and length<=9):
            return True
        return False

    def check_conditions(self):
        if(self.check_name()!=True):
            self.show_message_box(NAMEERR_MSG,NAME_CONDITION)
            return False
        if(self.check_Breakpoints()!=True):
            self.show_message_box(BREAKPOINTERR_MSG,BREAKPOINTS_CONDITION)
            return False
        return True

    def show_message_box(self,title,text):
        msgbox = QtGui.QMessageBox(self)
        msgbox.setText(title)
        msgbox.setInformativeText(text)
        msgbox.exec_()
    
    def apply_changes(self):
        if(self.check_conditions()==True):
            self.mode = Modus.Modus(str(self.ui.NameTxt.text()))
            self.mode.tags = self.getTags()
            self.mode.Beschreibung = self.ui.DescriptionTxt.toPlainText()
            self.mode.breakpoints = self.getbreakpoints()
            self.DataUpdateMethod(self.mode)
            self.destroy()

    def cancel(self):
        self.destroy()

    def destroy(self):
        for pb in self.parent().children():
            try:
                pb.show()
            except:None
        self.setParent(None)

    def change_enabledButtons(self,isit):
        None
        
    def showBreakpoints(self):
        self.ui.visualizeBreakpoints(self.model.breakpoints)

    def addBreakpoint(self):
        if(len(self.ui.breakpointElements)<9):
            time = int(self.ui.BreakpointTime.time().hour())
            self.model.breakpoints.append(Breakpoint.Breakpoint(5500,time))
            self.showBreakpoints()
        else:
            self.ui.addBreakpointBtn.setEnabled(False)

    def clearBreakpoints(self):
        self.ui.deleteBreakpointElements()

    def deleteCurrentBreakpoint(self):
        self.ui.deleteCurrentBreakpoint()

    def __init__(self,model,allTags,inherit):
        self.model = model
        self.allTags = allTags
        self.inherit = inherit
        super(ModeView,self).__init__()
        self.build_ui()

    def build_ui(self):
        self.ui = Ui_ModeNewEdit()
        self.ui.setupUi(self)
        self.ui.CancelBtn.clicked.connect(self.cancel)
        self.ui.ApplyBtn.clicked.connect(self.apply_changes)
        self.ui.addBreakpointBtn.clicked.connect(self.addBreakpoint)
        self.ui.ClearAllBtn.clicked.connect(self.clearBreakpoints)
        self.ui.RemoveBreakpointBtn.clicked.connect(self.deleteCurrentBreakpoint)
        if(self.model.name==None):
            self.ui.deleteBreakpointElements()
            self.ui.NameTxt.setEnabled(True)
        else:
            self.ui.NameTxt.setText(self.model.name)
            if(self.inherit==False):
                self.ui.NameTxt.setEnabled(False)
            else:
                self.ui.NameTxt.setText("Some new Mode")
            self.ui.DescriptionTxt.setText(str(self.model.Beschreibung).strip())
            if(self.model.tags != []):
                tagS = ""
                for tag in self.model.tags:
                    tagS += str(tag.name)+", "
                self.ui.TagsTxt.setText(tagS)
        self.showBreakpoints()
        
