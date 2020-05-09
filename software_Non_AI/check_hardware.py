from psutil import cpu_percent,sensors_battery,virtual_memory

'''
NOTE:
this module works for windows, linux, macos and is considered complete
if you want to add more hardware checking function first submit a PR
'''


'''
returns a string containing cpu usage
'''
def getcpuper(percpu=False):
    if percpu:
        cpu_say="The usages of cpu cores are "
        for x in cpu_percent(interval=1,percpu=percpu):
            cpu_say+=str(x)+", "
        cpu_say+="percent respectively"
    else:
        cpu_say="CPU usage is "+str(cpu_percent(interval=1,percpu=percpu))+" percent"
    print(cpu_say)
    return cpu_say



'''
returns a string containing battery info
'''
def getbattery():
    battery_say=""
    battery=sensors_battery()
    battery_say+=str(battery.percent)+" percent power left. "
    if battery.percent<30 and (not battery.power_plugged):
        battery_say+="running on emergency backup power. approximately "+str(battery.secsleft/60)+" minutes remaining."
    elif not battery.power_plugged:
        battery_say+=" approximately "+str(int(battery.secsleft/60))+" minutes remaining."
    else:
        battery_say+="plugged in, charging"
    print(battery_say)
    return battery_say
    


'''
returns a string containing ram usage details
'''
def getram():
    ram_say="System memory usage is "
    memory=virtual_memory()
    ram_say+=str(memory.percent)+" percent."
    if memory.percent>85:
        ram_say+=" System overload detected."
    else:
        ram_say+=" No overload detected"
    print(ram_say)
    return ram_say

