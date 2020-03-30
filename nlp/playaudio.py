import pyaudio
import wave


#this module receives audio files in wav format and plays them
def startPlayAudio(filename):
    chunk=1024
    wf=wave.open(filename,'rb')
    pa=pyaudio.PyAudio()

    stream=pa.open(format=pa.get_format_from_width(wf.getsampwidth()),channels=wf.getnchannels(),rate=wf.getframerate(),output=True)
    data_stream=wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream=wf.readframes(chunk)

    stream.close()
    pa.terminate()


#plays starting audio
def startAudio():
    startPlayAudio('C:\\Users\\skili\\Documents\\GitHub\\Actroid2.0\\nlp\\assets\\start.wav')


#plays ending audio
def endAudio():
    startPlayAudio('C:\\Users\\skili\\Documents\\GitHub\\Actroid2.0\\nlp\\assets\\end.wav')

if __name__ == "__main__":
    startAudio()