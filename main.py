import setup
from action_phrases import *
from playsounds import startPlayAudio
from text2speech import setupTts,startTts
from speech2text import startStt
import take_screenshot
import tell_joke
import take_notes
import power_options
import greet_startup
import get_weather
import check_hardware
import wolfram
import google_calendar
import random
from playmusic import *

'''
global variables to be used by jarvis
'''
asset_path="C:\\Users\\skili\\Documents\\GitHub\\J.A.R.V.I.S\\assets"
WAKE_CMD="jarvis"
CITY="gorakhpur"
USERNAME="kshitiz"
INIT_SEQ=True



'''
function to return random value from a list
used in returning random responses from response list stored in action_phrases.py
'''
def randomize(l):
    return l[random.randint(0,len(l)-1)]



'''
initial startup sequence - runs when jarvis starts
include anything and everything that jarvis might need during its execution and needs to be initialized once
this will make jarvis smooth during execution and the api call time gets reduced significantly

like : setting up connection for api calls
'''
def init():

    setupTts(250)
    wolfram.setupWolfram()
    google_calendar.setupCalendar()
    startPlayAudio('jarvisworking.wav')
    startTts(greet_startup.greet())
    startTts(get_weather.weather(CITY))
    startTts(google_calendar.startCalendar(2))
    startTts("Call me again if you need me.")



'''
dedicated functions to match intents and return response
'''
def matchCommand(CMD):

    #to check if jarvis is on and working
    if CMD in check_i:
        startTts(randomize(check_r))

    #greetings like hello,hi
    elif CMD in greet_i:  
        startTts(randomize(greet_r))

    elif CMD in playmusic_i:
        # to play music
        startTts(randomize(playmusic_r))
        startPlaymusic(asset_path+"\\music")

    elif CMD in stopmusic_i:
        stopMusic()

    elif CMD in pausemusic_i:
        pauseMusic()

    elif CMD in unpausemusic_i:
        unpauseMusic()

    elif CMD in notes_i:
        #to take notes
        startTts(randomize(notes_r))
        notes=startStt()
        take_notes.startNotes(notes,asset_path+"\\notes")
        startTts(randomize(notes_r2))
    
    elif CMD in weather_i:
        #to check weather
        startTts(randomize(weather_r))
        city=startStt()
        startTts(get_weather.weather(city))

    elif CMD in joke_i:
        #to tell a joke
        startTts(randomize(joke_r))
        startTts(tell_joke.startJoke())

    elif CMD in battery_i:
        #checks battery status
        startTts(check_hardware.getbattery())

    elif CMD in ram_i:
        #checks ram
        startTts(check_hardware.getram())

    elif CMD in cpu_i:
        #checks cpu
        startTts(randomize(cpu_r))
        allcore=startStt()
        if allcore in affirmative_i:
            startTts(check_hardware.getcpuper(True))
        else:
            startTts(check_hardware.getcpuper(False))
    
    elif CMD in shutdown_i:
        #shutdown
        startTts(randomize(shutdown_r))
        ans=startStt()
        if ans in affirmative_i:
            power_options.shutdown()

    elif CMD in screenshot_i:
        #capture screenshot
        startTts(randomize(screenshot_r))
        name=startStt()
        if name in screenshot_i2:
            take_screenshot.takeScreenshot(str(random.randint(0,99999)),asset_path+"\\screenshots")
        else:
            take_screenshot.takeScreenshot(name,asset_path+"\\screenshots")
        startTts(randomize(screenshot_r2))

    elif CMD in mute_i:
        mute()

    elif wolfram.startWolfram(CMD) is None:
        startTts("sorry sir, i cannot understand you")

    else:
        wolfram.startWolfram(CMD)

    

#function ends here



#main function starts here

def startMain():

    #run the initial startup sequence
    if INIT_SEQ:
        init()

    #continually listen for wake up word
    while True:
        wake=startStt()
        # if WAKE_CMD in wake:
        CMD=wake.replace(WAKE_CMD,"").strip()
        matchCommand(CMD)
            
#main function ends here



#ensures that jarvis starts when the file is executed by executing main fuction
if __name__ == "__main__":
    startMain()