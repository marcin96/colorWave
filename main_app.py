import sys
from PySide import QtGui
import colorWave
import MainController
import mainView
import mainContentView
import IpToLocation
import ConfigParser
from ConfigParser import NoSectionError
import getpass
from requests import get

SETTINGS_MSG = "Settings file corrupt or missing."
SETTINGS_COND = """Please make sure that the settings file ist existing,
for further information look into the help funktion."""
MODES_MSG = "Modes file corrupt or missing."
MODES_COND = """Please make sure that the modes file is existing, for further information
look into the help function"""

class Settings(object):
    lon = None
    lat = None
    location = None
    current_mode = None
    modus_path = None
    normal_color_temp = None
    maxTemp = None
    minTemp = None
    logfile = None
    config = None
    configWrite = None
    _update_funcs = []
    def __init__(self,settings_path,user):
        self.user = user
        self.settings_path = settings_path

    def ConfigSectionMap(self,Config,section):
        '''
        '''
        dict1 = {}
        options = Config.options(section)
        print(options)
        for option in options:
            try:
                dict1[option] = Config.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1

    def setConfigValue(self,section,value_name,value):
        self.configWrite.set(section,str(value_name),str(value))

    def subscribe_update_func(self, func):
        if func not in self._update_funcs:
            self._update_funcs.append(func)

    def unsubscribe_update_func(self, func):
        if func in self._update_funcs:
            self._update_funcs.remove(func)

    def update(self):
        for func in self._update_funcs:
            func()

    def load_settings(self):
        self.config = ConfigParser.ConfigParser()
        self.configWrite = ConfigParser.SafeConfigParser()
        self.config.read(self.settings_path)
        self.modus_path= self.ConfigSectionMap(self.config,self.user)['modus_path']
        self.logfile = self.ConfigSectionMap(self.config,self.user)['log_file']
        self.normal_color_temp = self.ConfigSectionMap(self.config,self.user)['normal_color_temp']
        self.lon = self.ConfigSectionMap(self.config,self.user)['lon']
        self.lat = self.ConfigSectionMap(self.config,self.user)['lat']
        self.current_mode = self.ConfigSectionMap(self.config,self.user)['start_mode']
        self.maxTemp = self.ConfigSectionMap(self.config,self.user)['maxtemp']
        self.minTemp = self.ConfigSectionMap(self.config,self.user)['mintemp']

    def update_settings(self):
        '''
        '''
        fp = open(self.settings_path,"w")
        self.configWrite.write(fp)
        fp.close()
        self.load_settings()
        self.update()

class App(QtGui.QApplication):
    def __init__(self, settings,sys_argv):
        super(App, self).__init__(sys_argv)
        self.settings = settings
        self.show_main_view()

    def show_main_view(self):
        self.model = colorWave.ColorWave(self.settings)
        self.main_view = mainContentView.MainView(self.model,None)
        self.main_view.setFixedSize(846,408);
        self.main_view.build_ui()
        self.main_view.show()
        self.main_view.setWindowTitle("colorWave")
        self.main_view.setWindowIcon(QtGui.QIcon('colorWave.ico'))
        self.model.setUpColorWave(self.settings.current_mode)
        self.model.running=True
        self.model.start()

def exit_application(app):
    app.exec_()
    app.model.stop_Mode()
    app.model.resetColorTemperature()
    exit()

def show_message_box(title,text):
    try:
        app = QtGui.QApplication(sys.argv)
    except RuntimeError:
        None
    msgbox = QtGui.QMessageBox()
    msgbox.setText(title)
    msgbox.setInformativeText(text)
    msgbox.show()
    msgbox.exec_()
    try:
        sys.exit(app.exec_())
    except UnboundLocalError:
        None

def main():
    user = getpass.getuser()
    settings = Settings("settings.ini",user)
    try:
        settings.load_settings()
        app = App(settings,sys.argv)
    except NoSectionError:
        show_message_box(SETTINGS_MSG,SETTINGS_COND)
    except IOError:
        show_message_box(MODES_MSG,MODES_COND)

    sys.exit(exit_application(app))

if __name__ == '__main__':
    main()
