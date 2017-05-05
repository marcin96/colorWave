'''
'''
import math
import ColorTemp


class Breakpoint():
    '''
    '''
    Beschreibung = ""
    def __init__(self,Farbtemperatur,Zeit):
        self.Farbtemperatur = int(Farbtemperatur)
        self.Zeit = Zeit

    def getTempInColor(self):
        N = ColorTemp.kalvin_to_RGB(self.Farbtemperatur)
        return (N[0]*2,N[1]*2,N[2]*2)
