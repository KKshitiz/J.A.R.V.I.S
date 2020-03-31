from pyowm import OWM
from datetime import datetime
#tells the weather
def weather(city):
    weather_say="Weather status in "+city+" is "
    owm=OWM('d4a9d6444f7784fc3c80cae78d414838') #enter your own apikey
    observation=owm.weather_at_place(city)
    w=observation.get_weather()
    # print(w.get_wind)
    status=str(w).rsplit(" ")[5]
   
    weather_say+=str(w.get_temperature('celsius')['temp'])+" celsius with "+status[status.rfind("=")+1:-1]
    weather_say+=". The average wind speed is "+str(w.get_wind()['speed'])+" kilometres per hour"
    weather_say+=" and the humidity is "+str(w.get_humidity())+" percent."
    return weather_say

#initiate greeting sequence
def greet():
    greet_text=""
    hour=int(datetime.now().hour)
    if hour>=0 and hour<12:
        greet_text="Good Morning Sir. "
    elif hour>=12 and hour<18:
        greet_text="Good Afternoon Sir. "
    else:
        greet_text="Good Evening Sir. "
    if hour>12:
        greet_text+="It's "+str(hour-12)+" "+str(datetime.now().minute)+" PM "+" now."
    else:
        greet_text+="It's "+str(hour)+" "+str(datetime.now().minute)+" AM "+" now."
    return greet_text
