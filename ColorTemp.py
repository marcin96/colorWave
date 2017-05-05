'''
'''
import math

def c_spektrum(func):
    '''
    '''
    def right_range(fakt):
        color = func(fakt)
        if(color>255):return 255
        if(color<0):return 0
        return int(color)
    return right_range

@c_spektrum
def __calc_blue(fakt):
    '''
    '''
    if(fakt >= 66):
        return 255
    if(fakt <=19):
        return 0
    return 138.5177312231 * math.log(fakt-10)-305.0447927307

@c_spektrum
def __calc_green(fakt):
    '''
    '''
    if(fakt <=66):
        green = 99.4708025861 * math.log(fakt) - 161.119581661
        return green
    return 288.1221695283 * (math.pow(fakt-60,-0.0755148492))

@c_spektrum
def __calc_red(fakt):
    '''
    '''
    if(fakt <=66):
        return 255
    return 329.698727446 * (math.pow(fakt-60,-0.1332047592))

def __calc_fakt(kalvin):
    '''
    '''
    return kalvin/100

def kalvin_to_RGB(kalvin):
    '''
    '''
    if(isinstance(kalvin,int) and kalvin > 0):
        fakt = __calc_fakt(kalvin)
        rgb = (__calc_red(fakt)/2,__calc_green(fakt)/2,__calc_blue(fakt)/2)
        return rgb
    raise ValueError("WRONG format for color temperature")

#print(kalvin_to_RGB(1000))
