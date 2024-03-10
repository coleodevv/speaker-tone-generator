The reason that the wav file plays without crashing. 
as seen by log of 
[11228] LOADER: ERROR python

it was unable to find the wav file pyinstaller does not bundle the sound or large files into the exe. 

Solution is place the large files like wav. etc in the same directory as the exe. 

This solves the load error and the program is able to load the wav