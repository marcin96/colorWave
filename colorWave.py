import getpass
import Astro
import ModiIO
import SunnyMode
import KorrekturManager
import datetime as dt
import ColorTemp
import sched
import threading
import time
import Modus

class ColorWave(threading.Thread):
    Sunrise = None
    Sunset = None
    User = None
    Time = None
    lon = None
    lat = None
    current_mode = None
    normal_color_temp = None
    modes = []
    running = False
    hour = dt.datetime.now().hour
    condition = threading.Condition()
    lock = threading.Lock()
    intervall=1.0
    timefunc = None
    def __init__(self,start_Settings):
        self._update_funcs = []
        self.start_Settings = start_Settings
        self.lon = start_Settings.lon
        self.lat = start_Settings.lat
        self.normal_colo_temp = start_Settings.normal_color_temp
        self.load_Modes(start_Settings.modus_path)
        self.modes.append(SunnyMode.SunnyMode(self.lon,self.lat))
        self.User = getpass.getuser()
        self.start_Settings.subscribe_update_func(self.update_from_source)
        threading.Thread.__init__(self)
        self.deamon=True

    def update_from_source(self):
        self.lon = self.start_Settings.lon
        self.lat = self.start_Settings.lat
        self.normal_colo_temp = self.start_Settings.normal_color_temp
        self.modes = []
        self.modes.append(SunnyMode.SunnyMode(self.lon,self.lat))
        self.load_Modes(self.start_Settings.modus_path)
        self.User = getpass.getuser()
        self.update()
        
    def calculate_Astro(self):
        obs = Astro.create_observator(self.lon,self.lat)
        self.Sunrise = Astro.getSunriseTime(obs)
        self.Sunset = Astro.getSunsetTime(obs)

    def load_Modes(self,path):
        self.modes = []
        self.root,self.tree = ModiIO.readXML(path)
        for mode in ModiIO.readModis(self.root):
            self.modes.append(mode)

    def deleteMode(self,mode_name):
        ModiIO.remove_Modus(mode_name,self.root,self.tree,self.start_Settings.modus_path)
        self.modes.remove(self.getModeByName(mode_name))

    def update_Mode(self,Mode):# Can also mean add
        ModiIO.update_Modus(self.root,self.tree,self.start_Settings.modus_path,Mode)
        print("update finished")
        self.load_Modes(self.start_Settings.modus_path)
        self.update()

    def getAllTags(self):
        tags = []
        for m in self.modes:
            for t in m.tags:
                if(t.name not in tags):
                    tags.append(t.name)
        return tags

    def getAllModeNames(self):
        names = []
        for mode in self.modes:
            names.append(mode.name)
        return names

    def create_EmptyMode(self):
        return Modus.Modus(None)

    def getModeByName(self,mode_name):
        for mode in self.modes:
            if(mode.name==mode_name):
                return mode
        return None

    def filterModesBySearch(self,search_text):
        m_name = []
        for m in self.modes:
            if(search_text.lower().strip() in m.name.lower().strip()):
                m_name.append(m.name)
        return m_name

    def getModesByTag(self,tag_name):
        modes = []
        for m in self.modes:
            for t in m.tags:
                if(t.name==tag_name):
                    modes.append(m.name)
        return modes

    def start_Mode(self):
        with self.condition:
            self.runnning = True
            self.condition.notify()

    def stop_Mode(self):
        with self.condition:
            self.runnning = False
            self.condition.notify()

    def run(self):
        print("start")
        while True:
            self.Time = str(dt.datetime.now().hour)+":"+str(dt.datetime.now().minute)
            self.hour = dt.datetime.now().hour
            self.current_mode.korrektur(self.hour)
            print("korrigiert")
            time.sleep(self.intervall)
            with self.lock:
                self.timefunc()
            with self.condition:
                if self.running==False:
                    self.condition.wait()
            
    
    def resetColorTemperature(self):
        '''
        '''
        KorrekturManager.set_color_Ramp(ColorTemp.kalvin_to_RGB(int(self.start_Settings.normal_color_temp)),angleichen=True)

    def setFixColorTemp(self,colorTemp):
        '''
        '''
        KorrekturManager.set_color_Ramp(ColorTemp.kalvin_to_RGB(colorTemp),angleichen=False)

    def get_Location(self):
        return str(self.lon)+","+str(self.lat)

    def setMode(self,mode_name):
        self.current_mode = self.getModeByName(mode_name)

    def subscribe_update_func(self, func):
        if func not in self._update_funcs:
            self._update_funcs.append(func)

    def unsubscribe_update_func(self, func):
        if func in self._update_funcs:
            self._update_funcs.remove(func)

    def update(self):
        for func in self._update_funcs:
            func()

    def update_Time(self):
        self.timefunc()

    def setUpColorWave(self,Mode_name):
        self.calculate_Astro()
        self.setMode(Mode_name)
        self.update()

    
        
