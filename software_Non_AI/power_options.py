import os

'''
this module controls power functions
NOTE: only works for windows system
'''
def shutdown():
    os.system("shutdown /s /t 1")

def restart():
    os.system("shutdown /r /t 1")

def shutdowntsec(t):
    os.system("shutdown /s /t "+str(t))

def restarttsec(t):
    os.system("shutdown /r /t "+str(t))