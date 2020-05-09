from datetime import datetime

'''
initiate greeting sequence to be played on jarvis startup
'''
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


