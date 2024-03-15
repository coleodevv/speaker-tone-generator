import os;
import time;
import numpy;
import schedule;
import sounddevice as sd;
from scipy.io import wavfile

# if you need to recompile here pyinstaller terminal code : 
# PyInstaller --onefile  --hide-console=hide-early main.py


timeInterval = 25
fullpath = "C:\\Users\\Coleson\\desktop\\KrkFix\\5hzTone.wav"

# gets the sound file without the filepath good for directly working with file types  
def truncatePathToBase(path):
    return os.path.basename(path)
soundPathBase = truncatePathToBase(fullpath)

# create numpy array from wav.file
samplerate, numpyarray =wavfile.read(soundPathBase)

#lists all the availible devices on this pc 
# listDevices =sd.query_devices()
# for device in listDevices:
#     print(device)

def playTone():
    sd.play(numpyarray, samplerate=None, mapping=None,blocking=True,loop=False,device="(Focusrite USB Audio), Windows DirectSound")

#play tone every 25 minutes
schedule.every(timeInterval).minutes.do(playTone)
    
while True:
    schedule.run_pending()
    # when you sleep threads you are doing the same thing as await async meaning your blocking the execution of further code in the same thread until it finishes
    # thread.sleep && await random code() same thing except await is when the value returns while sleep is just a time interval
    time.sleep(1)




    



