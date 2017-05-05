'''
'''
import os
import sys
import Modus
import Astro
import threading
import tag

class SunnyMode(Modus.Modus):
    '''
    '''
    def __init__(self,lat,lon):
        self.name = "SunnyMode"
        self.breakpoints=Astro.SunProgressToBreakpoints(lon,lat)
        self.Beschreibung = "Der standart Sonnenmodus"
        self.tags.append(tag.Tag("Sonne"))
        self.tags.append(tag.Tag("standart"))
        self.tags.append(tag.Tag("nature"))
        self.work = threading.Timer(1.0,self.korrektur)
    
