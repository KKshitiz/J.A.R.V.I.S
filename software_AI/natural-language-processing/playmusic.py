from pygame import mixer
from os import listdir
from random import randint

def startPlaymusic(asset_path):
    files=listdir(asset_path)
    mixer.init()
    mixer.music.load(asset_path+"\\"+files[randint(0,len(files)-1)])
    mixer.music.play()

def stopMusic():
    mixer.music.stop()

def pauseMusic():
    mixer.music.pause()
    
def unpauseMusic():
    mixer.music.unpause()