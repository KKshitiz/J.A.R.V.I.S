"""
consists of intents and the responses for actionable phrases

Actionable phrases are phrases on which jarvis needs to take some action rather than just conversing.

This section has to be hard coded for responses and their intents as they perform specific actions.
Therefore, the more the alternatives to responses and intents, the better JARVIS will perform. Be as verbose as possible.
for intents --> suffix with "_i"
for responses --> suffix with "_r"

if the action has intermediate conversations, the secondary suffix should denote the level
example:
greet_i=["hello"]
greet_r=["hi how are you"]
greet_i2=["i am fine"]
greet_r2=["how's your day going"]

"""
wakeup=["jarvis","hey jarvis"]

#generic yes/no intents to be said by user
affirmative_i=["yes","yep","sure","do it","just do it","go for it","go on","yeah","ya"]
negative_i=["no","nope","stop","don't do it","wait","give me some time","let me think"]

#generic yes/no responses to be spoken by jarvis
affirmative_r=["yes sir","doing it for you","working on it","i am on it, sir","ok, i'll do it"]
negative_r=["sorry sir! i have not been programmed to do so","i am unable to do it, sir"]

#standby check
check_i=["are you awake","are you up","are you there","are you dead","are you alive yet","are you alive","daddy's home","wake up","wake up daddy's home"]
check_r=["at your service, sir","i'm here, sir","for you sir, always","i am feeding on electricity already","consuming memory, sir","welcome home, sir"]

#greet
greet_i=["hey","hi","yo","howdy","hola","hello","helloo"]
greet_r=["hello, jarvis here, how are you ","hi, nice to meet you!","hello, how can i help you ","hi, i am jarvis","jarvis here, how can i help you "]

#to play music
playmusic_i=["turn up the heat","play some music","party time","i think the atmosphere is a little tensed","let's do some work","it's showtime","play music"]
playmusic_r=["playing music","on it sir","ok sir"]+affirmative_r

stopmusic_i=["stop music"]
pausemusic_i=["pause","pause music"]
unpausemusic_i=["unpause","unpause music"]

#to shutdown the system
shutdown_i=["shut down","nuke it","time to go to sleep","go to sleep","go get some rest"]
shutdown_r=["are you sure ","system will shut down. do you want to continue ","all functions will suspend. continue?"]

#to capture screenshot
screenshot_i=["take screenshot","capture the screen","save the screen","capture it"]
screenshot_r=["name ?","what should be the name ?","filename ?","what should be the filename, sir ?","what shall i name it  sir ?"]
screenshot_i2=["anything you wish","you decide","decide yourself","i don't know","anything"]
screenshot_r2=["capturing screen for reference","screen saved","stored it in my database"]

#joke commands
joke_i=["tell me a joke","do you have a joke for me","amuse me","make me laugh","i am feeling sad","tell a joke"]
joke_r=["here we go","joke time","hear me carefully","hear out","here's a programmer joke for you"]

#to check system status
battery_i=["check battery usage","check battery health","check battery","battery status","power status","check battery status","check system battery"]
ram_i=["check virtual memory","ram usage","check ram usage","memory usage","check memory usage"]
cpu_i=["check cpu usage","check cpu health","cpu usage"]
cpu_r=["would you like to know usage for all cpu cores ","Sir, shall I enumerate the usages of all the cores"]

#to take notes
notes_i=["make a note", "write this down", "remember this", "type this"]
notes_r=["what would you like to write","what would you like to remember"]
notes_r2=["noted","i've made a note of it","saved it in the notes directory"]

#to check weather
weather_i=["check weather","what's the weather","how's the sky","do i need to carry an umbrella","how about a picnic"]
weather_r=["which city would you like to check?"]

#to exit jarvis
self_destruct=["close","quit","self destruct",""]

#mute
mute_i=["shut up","mute","sounds off"]