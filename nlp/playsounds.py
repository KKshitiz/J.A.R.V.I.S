from pyaudio import PyAudio
from wave import open

#here specify the sounds asset path
asset_path="C:\\Users\\skili\\Documents\\GitHub\\J.A.R.V.I.S\\assets\\sounds\\"

#this module receives audio files in wav format and plays them
def startPlayAudio(filename):
    filename=asset_path+filename
    chunk=1024
    wf=open(filename,'rb')
    pa=PyAudio()

    stream=pa.open(format=pa.get_format_from_width(wf.getsampwidth()),channels=wf.getnchannels(),rate=wf.getframerate(),output=True)
    data_stream=wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream=wf.readframes(chunk)

    stream.close()
    pa.terminate()


#plays starting audio
def startAudio():
    startPlayAudio('start.wav')

#plays ending audio
def endAudio():
    startPlayAudio('end.wav')

if __name__ == "__main__":
    startAudio()