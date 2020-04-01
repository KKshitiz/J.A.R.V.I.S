import sys
sys.path.insert(1,'C:\\Users\\skili\\Documents\\GitHub\\J.A.R.V.I.S\\nlp')
from action_phrases import *
from playsounds import startPlayAudio
from text2speech import setupTts,startTts
from speech2text import startStt
sys.path.insert(1,'C:\\Users\\skili\\Documents\\GitHub\\J.A.R.V.I.S\\utility')
import miscutils
import sysutils
import googlecalendar
import random

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
        startTts(randomize(check_r))
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
            startPlayAudio('jarvislistening.wav')
            CMD=startStt()
            matchCommand(CMD)
            
#main function ends here



#start jarvis by executing main fuction
if __name__ == "__main__":
    startMain()