import winsound;
import os;
import emoji;

freq = 300
durationMs = 3000

fullpath = "C:\\Users\\Coleson\\desktop\\KrkFix\\main.py\\5hzTone.wav"
base = os.path.basename(fullpath)








# gets the sound file without the filepath good for directly working with file types  
def truncatePathToBase(path):
    return os.path.basename(path)

soundPathBase = truncatePathToBase(fullpath)




# After a beta test it works like a dream!! we just have to make sure it runs every 30 mins and starts the process at pc start
print(emoji.emojize("Currently playing wav file :speaker_high_volume:"))
winsound.PlaySound(soundPathBase,0)