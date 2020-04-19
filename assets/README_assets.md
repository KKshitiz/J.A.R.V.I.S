# Assets
## This directory shall contain the following sub-directories
- images
  - contains image assets used in the whole project
- music
  - contains music files to be played by jarvis when using play music command
  - place your music files here to be made accessible by jarvis
  - only .mp3 format files supported currently
- notes
  - jarvis stores the notes in this directory which are saved during its execution
  - the notes are saved in .txt format with a file name that includes its creation time and date
- sounds
  - sound assets to be used by jarvis during its execution
  - place your sound files here and then include it in the code to played
  - to include it in code use the startPlayaudio() fuction and pass the filename.mp3 as parameter
  - only .wav files supported currently
- screenshots
  - jarvis stores the screenshots in this folder captured during its execution
  - files are saved in .png format with filename as given by the user
  - if filename is not provided jarvis uses a random integer as the file name