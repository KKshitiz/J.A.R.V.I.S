from datetime import date
from key import Key
from sys import path
# path.insert(1,'C:\\Users\\skili\\Documents\\GitHub\\J.A.R.V.I.S\\nlp')


#this misc feature is made for windows systems, some functions may not work


#this module handles basic media control features
def mute():
    try:
        Key.mute()
    except:
        return False

def volumeup():
    try:
        Key.volume_up()
    except:
        return False

def volumedown():
    try:
        Key.volume_down()
    except:
        return False

def volumemin():
    try:
        Key.volume_min()
    except:
        return False

def volumemax():
    try:
        Key.volume_max()
    except:
        return False

def setvolume(v):
    try:
        Key.volume_set(v)
    except:
        return False

def playpause():
    try:
        Key.playpause()
    except:
        return False

def prevtrack():
    try:
        Key.previoustrack()
    except:
        return False

def nexttrack():
    try:
        Key.nexttrack()
    except:
        return False

#now time for some browser controls
def browserback():
    try:
        Key.browserback()
    except:
        return False

def browsernext():
    try:
        Key.browsernext()
    except:
        return False

def browserhome():
    try:
        Key.browserhome()
    except:
        return False

def browserrefresh():
    try:
        Key.browserrefresh()
    except:
        return False

def browserfav():
    try:
        Key.browserfav()
    except:
        return False

def browserback():
    try:
        Key.nexttrack()
    except:
        return False

browserback()