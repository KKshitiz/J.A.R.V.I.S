import sys
sys.path.insert(1,'C:\\Users\\skili\\Documents\\GitHub\\J.A.R.V.I.S\\nlp')
from playsounds import startPlayAudio
from text2speech import setupTts,startTts
from speech2text import startStt
sys.path.insert(1,'C:\\Users\\skili\\Documents\\GitHub\\J.A.R.V.I.S\\utility')
import miscutils
import sysutils
import googlecalendar

#initial startup sequence
def init():
    setupTts(250)
    startPlayAudio('jarvisworking.wav')
    startTts(miscutils.greet())
    startTts(miscutils.weather("gorakhpur"))
    startTts(googlecalendar.startCalendar(2))
    startTts("Call me again if you need me.")


#main function
def startMain():
    init()
    s= startStt()
    if "jarvis" in s:
        startPlayAudio('jarvislistening.wav')
        startTts(startStt())


if __name__ == "__main__":
    startMain()