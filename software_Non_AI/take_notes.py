import subprocess
from datetime import datetime

#saves the note in notes folder and displays them
def startNotes(text,path):
    date =datetime.now()
    file_name=path+str(date).replace(":","-")+"-note.txt"
    with open(file_name,"w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe",file_name])
