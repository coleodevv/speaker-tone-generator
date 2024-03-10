import winsound;
import os;
import time;
import schedule;

# if you need to recompile here pyinstaller terminal code : 
# PyInstaller --onefile  --hide-console=hide-early main.py


timeInterval = 25
fullpath = "C:\\Users\\Coleson\\desktop\\KrkFix\\5hzTone.wav"


# gets the sound file without the filepath good for directly working with file types  
def truncatePathToBase(path):
    return os.path.basename(path)

soundPathBase = truncatePathToBase(fullpath)

# After a beta test it works like a dream!! we just have to make sure it runs every 30 mins and starts the process at pc start
def playTone():
    winsound.PlaySound(soundPathBase,0)

#play tone every 25 minutes
schedule.every(timeInterval).minutes.do(playTone)
    
while True:
    schedule.run_pending()
    # when you sleep threads you are doing the same thing as await async meaning your blocking the execution of further code in the same thread until it finishes
    # thread.sleep && await random code() same thing except await is when the value returns while sleep is just a time interval
    time.sleep(1)





    



