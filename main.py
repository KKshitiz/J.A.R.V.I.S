import sys
sys.path.insert(1,'C:\\Users\\skili\\Documents\\GitHub\\J.A.R.V.I.S\\nlp')
from action_phrases import *
from playsounds import startPlayAudio
from text2speech import setupTts,startTts
from speech2text import startStt
sys.path.insert(1,'C:\\Users\\skili\\Documents\\GitHub\\J.A.R.V.I.S\\utility')
from miscutils import *
import sysutils
import googlecalendar
import random
from playmusic import *

#some variables
WAKE_CMD=wakeup
CITY="gorakhpur"
USERNAME="kshitiz"
#some variables



#function to return random value from a list

def randomize(l):
    return l[random.randint(0,len(l)-1)]



#initial startup sequence starts

def init():

    setupTts(250)
    startPlayAudio('jarvisworking.wav')
    startTts(miscutils.greet())
    startTts(miscutils.weather(CITY))
    startTts(googlecalendar.startCalendar(2))
    startTts("Call me again if you need me.")

#initial startup sequence ends here



#function to match commands
def matchCommand(CMD):

    if CMD in check_i:
        #to check if jarvis is on and working
        startTts(randomize(check_r))

    elif CMD in greet_i:
        #greetings like hello,hi
        startTts(randomize(greet_r))

    elif CMD in playmusic_i:
        # to play music
        startTts(randomize(playmusic_r))
        startPlaymusic()

    elif CMD in notes_i:
        #to take notes
        startTts(randomize(notes_r))
        notes=startStt()
        startNotes(notes)
        startTts(randomize(notes_r2))
    
    elif CMD in weather_i:
        #to check weather
        startTts(randomize(weather_r))
        city=startTts()
        startTts(weather(city))

    elif CMD in joke_i:
        #to tell a joke
        startTts(randomize(joke_r))
        startTts(startJoke())

    elif CMD in 
    return
#function ends here



#main function starts here

def startMain():

    #run the initial startup sequence
    init()

    #continually listen for wake up word
    while True:
        wake=startStt()
        print(wake)
        if wake in WAKE_CMD:
            CMD=startStt()
            matchCommand(CMD)
            
#main function ends here



#start jarvis by executing main fuction
if __name__ == "__main__":
    startMain()