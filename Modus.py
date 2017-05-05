'''
'''
import os
import sys
import threading
import time
from time import sleep
import datetime as dt
import ColorTemp
import KorrekturManager
import Breakpoint


class Modus():
    '''
    '''
    Benutzer=""
    erstelltam = None
    veraendertam = None
    intervall = None
    tags = []
    breakpoints = []
    Beschreibung = ""
    wechsel = True
    def __init__(self,name):
        '''
        '''
        self.name = name
        self.work = threading.Timer(1.0,self.korrektur)

    def filter_nearest_points(self,hour):
        diff = []
        for point in self.breakpoints:
            diff.append([point,abs(point.Zeit-hour)])
        diff.sort(key=lambda x:int(x[1]))
        return (diff[0][0],diff[1][0])

    def filter_nearest_points2(self,hour):
        pointN =(12,0)
        p2=0
        points = []
        for point in range(len(self.breakpoints)):
            if(abs(self.breakpoints[point].Zeit-hour)<pointN[0]):
                pointN = (abs(self.breakpoints[point].Zeit-hour),point)
        
        points.append(self.breakpoints[pointN[1]])
        if(pointN[1]==len(self.breakpoints)-1):
            p2=0
        if(pointN[1]==0):
            p2 = len(self.breakpoints)-1
        points.append(self.breakpoints[p2])
        return points

    def calculate_color_temp(self,hour,minutes=30):
        '''
        '''
        points = self.filter_nearest_points2(hour)
        minutes_n = minutes
        hour_diff = points[1].Zeit-points[0].Zeit
        prozent = 0
        if(hour_diff>1):
            minutes = hour_diff*60
            offset = (hour - points[0].Zeit)* 60 + dt.datetime.now().minute
            prozent = offset / float(minutes/100)
        else:
            prozent = float(minutes_n) / 60.0/100.0
        temp_diff = abs(points[1].Farbtemperatur-points[0].Farbtemperatur)
        temp = (temp_diff/100)*prozent + points[0].Farbtemperatur
        print(temp)
        return temp
    
    def get_Tags(self):
        tags_coll = ""
        for t in self.tags:
            tags_coll += " " +t.name
        return tags_coll

    def korrektur(self,hour=-1,minutes = 30):
        '''
        '''
        print("korrektur")
        if(hour==-1):
            hour = dt.datetime.now().hour
        kalvin = self.calculate_color_temp(hour,minutes)
        gamma = ColorTemp.kalvin_to_RGB(int(kalvin))
        KorrekturManager.set_color_Ramp(gamma)
        print("korrektur finished")

    def preview(self,sl=0.05):
        '''
        '''
        for hour in range(1,24):
            self.korrektur(hour=hour)
            print("Stunde",hour)
            sleep(sl)

    def getInfoForSave(self):
        Inf = {}
        Inf.update({})
        

'''def Test():
    print("Start")
    Breakpoints = []
    M = Modus("BeispielModus")
    Breakpoints.append(Breakpoint.Breakpoint(2000,9))
    Breakpoints.append(Breakpoint.Breakpoint(3000,10))
    Breakpoints.append(Breakpoint.Breakpoint(4000,12))
    Breakpoints.append(Breakpoint.Breakpoint(5000,15))
    Breakpoints.append(Breakpoint.Breakpoint(4000,18))
    Breakpoints.append(Breakpoint.Breakpoint(2000,20))
    Breakpoints.append(Breakpoint.Breakpoint(5500,22))
    M.breakpoints = Breakpoints
    print("Breakpoints gesetzt")
    print("Preview start")
    M.preview()
    print("finished")

Test()
'''
