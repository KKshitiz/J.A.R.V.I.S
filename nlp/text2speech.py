import pyttsx3 #pip install pyttsx3

engine=pyttsx3.init()
def setupTts(rate=180,volume=1.0):

    #configure rate
    print("Current speaking rate="+str(engine.getProperty('rate')))
    engine.setProperty('rate',rate)
    print("Updated speaking rate="+str(engine.getProperty('rate')))
    #configure volume
    print("Current volume="+str(engine.getProperty('volume')))
    engine.setProperty('volume',volume)
    print("Current volume="+str(engine.getProperty('volume')))
    #configure voice
    voices=engine.getProperty('voices')
    print(voices)
    engine.setProperty('voices',voices[0].id)   #male voice
    # engine.setProperty('voices',voices[1].id)   #female voice

def startTts(text):
    engine.say(text)
    print("saying:"+text)
    engine.runAndWait()

if __name__ == "__main__":
    setupTts(170,1.0)
    startTts("You are not authorized to access this area!")