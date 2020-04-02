from pygame import mixer  # Load the popular external library
asset_path="C:\\Users\\skili\\Documents\\GitHub\\J.A.R.V.I.S\\assets\\music\\"

def startPlaymusic():
    mixer.init()
    mixer.music.load(asset_path+"T.N.T..mp3")
    mixer.music.play()