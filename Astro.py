'''
'''
import sys
import os
import ephem
import datetime,time
from Breakpoint import *

SonnenKonstA = 3000
SonnenKonstM = 5500

def getDateTimeAsString():
    '''
    '''
    return str(datetime.datetime.now())

def create_observator(lon,lat):
    obs = ephem.Observer()
    obs.date = getDateTimeAsString()
    horizon = '-6'
    lat=str(lat);lon=str(lon)
    obs.lon = str(lon)
    obs.lat = str(lat)
    return obs

def getSunrise(obs):
    '''
    '''
    return obs.previous_rising(ephem.Sun(),use_center=True)

def getSunset(obs):
    '''
    '''
    return obs.next_setting(ephem.Sun(),use_center=True)

def getSunriseTime(obs):
    tmp = getSunrise(obs)
    ret = getTimefromStr(tmp)
    return str(ret[0])+":"+str(ret[1])

def getSunsetTime(obs):
    tmp = getSunset(obs)
    ret = getTimefromStr(tmp)
    return str(ret[0])+":"+str(ret[1])

def getTimefromStr(time):
    return (time.tuple()[3],time.tuple()[4])

def getHourFromStrTime(time):
    return time.tuple()[3]

def SunProgressToBreakpoints(lon,lat):
    '''
    '''
    Breakpoints = []
    obs = create_observator(lon,lat)
    sunriseHour = getHourFromStrTime(getSunrise(obs))
    sunsetHour = getHourFromStrTime(getSunset(obs))
    Breakpoints.append(Breakpoint(1000,sunriseHour-1))
    Breakpoints.append(Breakpoint(SonnenKonstA,sunriseHour))
    Breakpoints.append(Breakpoint(SonnenKonstA+500,sunriseHour+1))
    Breakpoints.append(Breakpoint(SonnenKonstM,12))
    Breakpoints.append(Breakpoint(SonnenKonstA+500,sunsetHour-1))
    Breakpoints.append(Breakpoint(SonnenKonstA,sunsetHour))
    Breakpoints.append(Breakpoint(SonnenKonstA-1000,sunsetHour+1))
    Breakpoints.append(Breakpoint(1000,sunsetHour+4))
    return Breakpoints
    
    
    
