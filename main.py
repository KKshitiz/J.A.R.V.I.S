import sys
sys.path.insert(1,'C:\\Users\\skili\\Documents\\GitHub\\J.A.R.V.I.S\\nlp')
from playsounds import startPlayAudio
from text2speech import setupTts,startTts
sys.path.insert(1,'C:\\Users\\skili\\Documents\\GitHub\\J.A.R.V.I.S\\utility')
import miscutils
import sysutils

#main function
def startMain():
    setupTts(250)
    startPlayAudio('jarvisworking.wav')
    startTts(miscutils.greet())
    startTts(miscutils.weather("gorakhpur"))
    startTts("Call me again if you need me.")

if __name__ == "__main__":
    startMain()