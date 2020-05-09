from pyowm import OWM


''''
OWN api to return weather data
'''
def weather(city):
    weather_say="Weather status in "+city+" is "
    try:
        owm=OWM('d4a9d6444f7784fc3c80cae78d414838') #enter your own apikey
        observation=owm.weather_at_place(city)
        w=observation.get_weather()
        # print(w.get_wind)
        status=str(w).rsplit(" ")[5]
    
        weather_say+=str(w.get_temperature('celsius')['temp'])+" celsius and the sky is "+status[status.rfind("=")+1:-1]
        weather_say+=". The average wind speed is "+str(w.get_wind()['speed'])+" kilometres per hour"
        weather_say+=" and the humidity is "+str(w.get_humidity())+" percent."
    except:
        weather_say+="unavailable."
    return weather_say

