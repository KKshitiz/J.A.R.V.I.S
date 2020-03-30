import speech_recognition as sr
from playaudio import *

#this module converts speech2text


def startStt(lang='en-in'):
    r=sr.Recognizer()
    print("Listening")
    startAudio()

    with sr.Microphone() as source:
        print("Say something")
        r.pause_threshold=1      #Represents the minimum length of silence (in seconds) that will register as the end of a phrase

        r.adjust_for_ambient_noise(source,duration=0.2)
        audio=r.listen(source)

    endAudio()
    speech=""

    try:
        speech=r.recognize_google(audio,language=lang)
        print("Speech:",speech)
        return speech
    except sr.UnknownValueError:
        speech="Sorry! Couldn't understand"
        print("Sorry! Couldn't understand")
        return speech
    except sr.RequestError as e:
        print("Could not process request")
        speech="Could not process request"
        return speech

if __name__ == "__main__":
    startStt()