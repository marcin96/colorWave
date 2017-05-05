from PySide import QtGui
from mainContentframe import Ui_MainView
from ModelsView import ModelsView
from settingsView import settingsView
import helpwindow

class MainView(QtGui.QMainWindow):

    edit_show_func = None
    Konstant_mode = False
    def set_Sunset(self,sunset):
        self.ui.Sunsetlbl.setText("Sunset: "+str(sunset))

    def set_Sunrise(self,sunrise):
        self.ui.Sunriselbl.setText("Sunrise: "+str(sunrise))

    def set_User(self,user):
        self.ui.Userlbl.setText("User: "+str(user))

    def set_Location(self,location):
        self.ui.Locationlbl.setText("Location: "+str(location))

    def set_Modes(self,mode_names):
        self.ui.ModusViewBox.clear()
        self.ui.ModusViewBox.addItems(mode_names)

    def set_normal_color_temp(self,temp):
        self.ui.ColoTemplbl.setText("normal Color Temp: "+str(temp)+"K")

    def set_Mode_View(self,mode):
        self.ui.visualizeBreakpoints(mode.breakpoints)
        self.ui.modusTagsLbl.setText("Tags: "+mode.get_Tags())
        print(mode.Beschreibung,mode.get_Tags())
        self.ui.modusDescriptionlbl.setText("Description: "+str(mode.Beschreibung).strip())

    def start_Mode(self):
        self.ui.startModusBtn.setEnabled(False)
        self.ui.stopModusBtn.setEnabled(True)
        self.ui.ModusViewBox.setEnabled(False)
        self.ui.SettingsBtn.setEnabled(False)
        self.ui.EditModesBtn.setEnabled(False)
        self.ui.setKonstantTempBtn.setEnabled(False)
        self.model.running = True
        self.model.start_Mode()

    def stop_Mode(self):
        self.ui.startModusBtn.setEnabled(True)
        self.ui.stopModusBtn.setEnabled(False)
        self.ui.ModusViewBox.setEnabled(True)
        self.ui.ModusViewBox.setEnabled(True)
        self.ui.SettingsBtn.setEnabled(True)
        self.ui.EditModesBtn.setEnabled(True)
        self.ui.previewModusBtn.setEnabled(True)
        self.ui.setKonstantTempBtn.setEnabled(True)
        self.ui.stopModusBtn.setText("Stop")
        self.model.running = False
        self.model.stop_Mode()
        self.model.resetColorTemperature()

    def preview_Mode(self):
        self.ui.previewModusBtn.setEnabled(False)
        self.ui.startModusBtn.setEnabled(False)
        self.ui.ModusViewBox.setEnabled(False)
        self.model.current_mode.preview()
        self.model.resetColorTemperature()
        self.ui.startModusBtn.setEnabled(True)
        self.ui.ModusViewBox.setEnabled(True)
        self.ui.previewModusBtn.setEnabled(True)

    def startKonstantTemp(self):
        if(self.Konstant_mode==False):
            self.ui.startModusBtn.setEnabled(False)
            self.ui.stopModusBtn.setEnabled(False)
            self.ui.previewModusBtn.setEnabled(False)
            self.ui.ModusViewBox.setEnabled(False)
            self.Konstant_mode=True
            self.ui.setKonstantTempBtn.setText("stop Konstant")
            m_ax = self.model.start_Settings.maxTemp
            m_in = self.model.start_Settings.minTemp
            normal = self.model.start_Settings.normal_color_temp
            self.ui.show_Konstant_Controls(m_in,m_ax,normal)
        else:
            self.Konstant_mode = False
            self.ui.startModusBtn.setEnabled(True)
            self.ui.previewModusBtn.setEnabled(True)
            self.ui.ModusViewBox.setEnabled(True)
            self.ui.setKonstantTempBtn.setText("set Konstant")
            self.ui.hide_Konstant_Controls()
            self.model.resetColorTemperature()

    def setKonstantTemp(self):
        self.model.setFixColorTemp(self.ui.konstantModeSlider.value())
        

    def mode_changed(self):
        mode_name = self.ui.ModusViewBox.currentText()
        self.model.setMode(mode_name)
        self.set_Mode_View(self.model.current_mode)

    def showEditModesView(self):
        modesView =  ModelsView(self.model)
        modesView.build_ui()
        for pb in self.ui.centralWidget.children():
            try:
                pb.hide()
            except:None
        modesView.setParent(self.ui.centralWidget)
        modesView.show()

    def showHelp(self):
        helpwindow.show()

    def showSettingsView(self):
        setView = settingsView(self.model.start_Settings,self.model.getAllModeNames(),self)
        setView.build_ui()
        for pb in self.ui.centralWidget.children():
            try:
                pb.hide()
            except:None
        setView.setParent(self.ui.centralWidget)
        setView.show()

    def __init__(self,model,control):
        self.model = model
        self.control = control
        super(MainView,self).__init__()
        self.build_ui()
        self.model.subscribe_update_func(self.update_ui_from_model)
        self.model.timefunc = self.update_time

    def build_ui(self):
        self.ui = Ui_MainView()
        self.ui.setupUi(self)
        self.ui.startModusBtn.clicked.connect(self.start_Mode)
        self.ui.stopModusBtn.clicked.connect(self.stop_Mode)
        self.ui.previewModusBtn.clicked.connect(self.preview_Mode)
        self.ui.setKonstantTempBtn.clicked.connect(self.startKonstantTemp)
        self.ui.ModusViewBox.currentIndexChanged.connect(self.mode_changed)
        self.ui.EditModesBtn.clicked.connect(self.showEditModesView)
        self.ui.konstantModeSlider.valueChanged.connect(self.setKonstantTemp)
        self.ui.SettingsBtn.clicked.connect(self.showSettingsView)
        self.ui.startModusBtn.setEnabled(False)
        self.ui.ModusViewBox.setEnabled(False)
        self.ui.SettingsBtn.setEnabled(False)
        self.ui.EditModesBtn.setEnabled(False)
        self.ui.setKonstantTempBtn.setEnabled(False)
        self.ui.previewModusBtn.setEnabled(False)
        self.ui.actionHelp.triggered.connect(self.showHelp)

    def update_time(self):
        self.ui.TimeLbl.setText(str(self.model.Time))

    def update_ui_from_model(self):
        self.set_Sunset(self.model.Sunset)
        self.set_Sunrise(self.model.Sunrise)
        self.set_User(self.model.User)
        self.set_Location(self.model.get_Location())
        self.set_normal_color_temp(self.model.normal_colo_temp)
        self.set_Modes(self.model.getAllModeNames())
        self.set_Mode_View(self.model.current_mode)
        
        
