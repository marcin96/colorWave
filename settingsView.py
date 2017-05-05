from PySide import QtGui,QtCore
from settingsFrame import Ui_SettingsView
import os.path

COORDINATES_MSG = "The Coordinates are wrong"
COORDINATES_CONDITION = "Please fill in Longitude and Latitude corectly"
PATH_MSG = "The Paths are korrupt"
PATH_CONDITION = "Please check if the Modes and log Path exists."

class settingsView(QtGui.QFrame):

    def __init__(self,model,mode_names,previus):
        self.model = model
        self.previus = previus
        self.mode_names = mode_names
        super(settingsView,self).__init__()

    def isNumeric(self,number):
        try:
            float(number)
            return True
        except ValueError:
            return False

    def checkCoordinates(self):
        lon = self.ui.longTxt.text()
        lat = self.ui.latTxt.text()
        if(lon.strip()=="" or lat.strip()==""):
            return False
        if(self.isNumeric(lon)==False or self.isNumeric(lat)==False):
            return False
        return True

    def doesFileExist(self,File):
        return os.path.isfile(File)

    def checkPaths(self):
        modes_path = self.ui.ModePathTxt.text()
        log_path = self.ui.LogFilePathTxt.text()
        if(self.doesFileExist(modes_path)==False or
           self.doesFileExist(log_path)==False):
            return False
        return True

    def checkConditions(self):
        if(self.checkCoordinates()==False):
            self.show_message_box(COORDINATES_MSG,COORDINATES_CONDITION)
            return False
        if(self.checkPaths()==False):
            self.show_message_box(PATH_MSG,PATH_CONDITION)
            return False
        return True

    def update(self):
        if(self.checkConditions()==True):
            self.model.configWrite.add_section(self.model.user)
            self.model.setConfigValue(self.model.user,"modus_path",self.ui.ModePathTxt.text())
            self.model.setConfigValue(self.model.user,"log_file",self.ui.LogFilePathTxt.text())
            self.model.setConfigValue(self.model.user,"normal_color_temp",self.ui.normalTempSlider.value())
            self.model.setConfigValue(self.model.user,"lon",self.ui.longTxt.text())
            self.model.setConfigValue(self.model.user,"lat",self.ui.latTxt.text())
            self.model.setConfigValue(self.model.user,"start_mode",self.ui.startModeBox.currentText())
            self.model.setConfigValue(self.model.user,"maxtemp",self.ui.MaxTempN.value())
            self.model.setConfigValue(self.model.user,"mintemp",self.ui.MinTempN.value())
            self.model.update_settings()
            self.destroy()

    def destroy(self):
        for pb in self.parent().children():
            try:
                pb.show()
            except:None
        self.setParent(None)

    def show_message_box(self,title,text):
        msgbox = QtGui.QMessageBox(self)
        msgbox.setText(title)
        msgbox.setInformativeText(text)
        msgbox.exec_()

    def change_normal_color_temp(self):
        self.ui.normalColorTmpLbl.setText(str(self.ui.normalTempSlider.value())+"K")

    def build_ui(self):
        self.ui = Ui_SettingsView()
        self.ui.setupUi(self)
        self.ui.CancelBtn.clicked.connect(self.destroy)
        self.ui.ApplyBtn.clicked.connect(self.update)
        self.ui.longTxt.setText(self.model.lon)
        self.ui.latTxt.setText(self.model.lat)
        self.ui.MaxTempN.setValue(int(self.model.maxTemp))
        self.ui.MinTempN.setValue(int(self.model.minTemp))
        self.ui.ModePathTxt.setText(self.model.modus_path)
        self.ui.normalTempSlider.setMaximum(int(self.model.maxTemp))
        self.ui.normalTempSlider.setMinimum(int(self.model.minTemp))
        self.ui.normalTempSlider.setValue(int(self.model.normal_color_temp))
        self.ui.normalTempSlider.valueChanged.connect(self.change_normal_color_temp)
        self.ui.LogFilePathTxt.setText(self.model.logfile)
        for mode_name in self.mode_names:
            if(mode_name!=self.model.current_mode):
                self.ui.startModeBox.addItem(mode_name)
        self.ui.startModeBox.insertItem(0,self.model.current_mode)
        self.ui.startModeBox.setCurrentIndex(0)
        
        
