# import datetime
# import wikipedia    #pip install wikipedia
# import webbrowser
# import os
# import smtplib
# import sys
# sys.path.insert(1,'C:\\Users\\skili\\Documents\\GitHub\\Actroid2.0\\nlp')
# from text2speech import *
# import pyjokes      #pip install pyjokes
import pyowm        #pip install pyowm



# #function to execute as soon as actroid starts
# def greet():
#     greet_text=""
#     hour=int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         greet_text="Good Morning!"
#     elif hour>=12 and hour<18:
#         greet_text="Good Afternoon!"
#     else:
#         greet_text="Good Evening!"
#     greet_text+=" I am Actroid. How may I help you?"
#     startTts(greet_text)

# #function to take a query and search on wikipedia
# def wiki(query):
#     startTts('Searching wikipedia for '+query)
#     print('Searching wikipedia for '+query)
#     try:
#         result=wikipedia.summary(query,sentences=2)
#         startTts('According to Wikipedia, '+result)
#         #print('According to Wikipedia, '+result)
#     except:
#         startTts("Sorry couldn't find any result for "+query+" on Wikipedia")
#         #print("Sorry couldn't find any result for "+query+" on Wikipedia")


# #tells a random programming joke everytime
# def joke():
#     joke=pyjokes.get_joke()
#     startTts(joke)
#     #print("Joke:"+joke)

# #tells the weather
def weather(city):
    owm=pyowm.OWM('d4a9d6444f7784fc3c80cae78d414838') #enter your own apikey
    observation=owm.weather_at_place(city)
    w=observation.get_weather()
    print(w)
    w.get_wind()
    w.get_humidity()
    w.get_temperature('celsius')

weather("california")
# #opens app from system
# #add programs acc to convenience
# def openApp(appname):
#     try:
#         if "chrome" == appname:
#             startTts("Opening "+appname)
#             os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
#             return
#         elif "word"==appname:
#             startTts("Opening "+appname)
#             os.startfile('path')
#             return
#         elif "excel"==appname:
#             startTts("Opening "+appname)
#             os.startfile('path')
#             return
#         elif "command prompt"==appname:
#             startTts("Opening "+appname)
#             os.startfile('path')
#             return
#         elif "edge"==appname:
#             startTts("Opening "+appname)
#             os.startfile('path')
#             return
#     # except:
#     #     startTts("Application not available on system")

