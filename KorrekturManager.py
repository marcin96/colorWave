'''
'''

from ctypes import *
import numpy, sys, platform, ctypes, ctypes.util
import logging
from logging.config import fileConfig
from time import sleep

#DLLS
user = windll.LoadLibrary("c:\\windows\\system32\\user32.dll")
h = user.GetDC(0)
gdi = windll.LoadLibrary("c:\\windows\\system32\\gdi32.dll")

#Globale Konstanten
MAXIMUM = int(255)
MINIMUM = int(0)
RAMPSIZE= 256
RAMPDIM = 3
MAXRAMPELEM=65545

def __get_color_Ramp_Gamma():
    '''
    '''
    ramp = numpy.empty((3,256),dtype=numpy.uint16)
    success = windll.gdi32.GetDeviceGammaRamp(h,ramp.ctypes)
    return (ramp[0][1]-128,ramp[1][1]-128,ramp[2][1]-128)

def __build_color_Ramp(rgb):
    '''
    '''
    f_ramp = numpy.empty((RAMPDIM,RAMPSIZE),dtype=numpy.uint16)
    for dimension in range(RAMPDIM):
        for element in range(0,256):
            f_ramp[dimension][element]= __filtere(numpy.uint16(element) * (numpy.uint16(rgb[dimension]) + numpy.uint16(128)))
    logging.debug(f_ramp)
    return f_ramp

def __filtere(colorInf):
    '''
    Begrentzt das Maximum der Kurve.
    '''
    if(colorInf>MAXRAMPELEM):
        return MAXRAMPELEME
    return colorInf

def __korrekt_rgb(rgb,difference,step,steps):
    r_ch = float(difference[0])/float(steps)
    g_ch = float(difference[1])/float(steps)
    b_ch = float(difference[2])/float(steps)
    rgb = (int(round(rgb[0]+r_ch*step,0)),int(round(rgb[1]+g_ch*step,0)),int(round(rgb[2]+b_ch*step,0)))
    #print(rgb)
    return rgb

def __get_rgb_difference(rgb,top):
    return (rgb[0]-top[0],rgb[1]-top[1],rgb[2]-top[2])

def __get_steps_to_korrektion(difference):
    k = difference[0]
    for i in list(difference):
        if(abs(i)>abs(k)):
            k = abs(i)
    return k

def set_color_Ramp(rgb,angleichen=True,delay=False,intervall=0.1):
    '''
    '''
    old_Ramp_RGB = __get_color_Ramp_Gamma()
    #print("Old",old_Ramp_RGB)
    new_Ramp = __build_color_Ramp(rgb)
    if(angleichen):
        r_diff = __get_rgb_difference(rgb,old_Ramp_RGB)
        steps = __get_steps_to_korrektion(r_diff)
        #print("diff",r_diff)
        #print("steps",steps)
        for step in range(steps):
            korr_Ramp = __build_color_Ramp(__korrekt_rgb(old_Ramp_RGB,r_diff,step,steps))
            #print(step)
            windll.gdi32.SetDeviceGammaRamp(h,korr_Ramp.ctypes)
            if(delay):sleep(intervall)
    windll.gdi32.SetDeviceGammaRamp(h,new_Ramp.ctypes)
    
#print("start")
#set_color_Ramp((127,118,111))
#set_color_Ramp((100,80,20))
#set_color_Ramp((126, 113, 13))
#set_color_Ramp((127,118,111))
#print("finished")
