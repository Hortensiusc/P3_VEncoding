# Carlos Hortensius U150010

# Practice 3 Video Encoding Systems

import os
import subprocess
from functions import broadcasting


print('Welcome to Practice: Introduce the path where your video is located:\n')
path = input()
os.chdir(path)

print('Introduce the name of your video:\n')
video = input()

# We first need to read the video and audio codecs of the video that we have, and then see in which one of
# the broadcasting standarts that we have in theory class it can fit

'''
cmd = 'ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=nw=1:nk=1 %s ' %video
video_codec = subprocess.call(cmd, shell=True)

cmd = 'ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=nw=1:nk=1 %s ' %video
audio_codec = subprocess.call(cmd, shell=True)

print(video_codec, ' and ', audio_codec) 
''' #First I tried this, but I couldn't save the name of the codecs 
# that appeared in the terminal in a python variable of type string

cmd = 'ffprobe -show_streams -select_streams v:0 %s > infovideo.txt' %video
subprocess.call(cmd, shell=True)
cmd = 'ffprobe -show_streams -select_streams a:0 %s > infoaudio.txt' %video
subprocess.call(cmd, shell=True)

with open("infovideo.txt") as f:
    video_codecc = f.readlines()[2]
    f.close()


with open("infoaudio.txt") as f:
    audio_codecc = f.readlines()[2]


long = len(video_codecc)
video_codec =  str(video_codecc[11:long-1])
audio_codec =  str(audio_codecc[11:long-2])


# Find which ones suits
broadcasting(video_codec, audio_codec)

cmd = 'rm infovideo.txt'
subprocess.call(cmd, shell=True)
cmd = 'rm infoaudio.txt'
subprocess.call(cmd, shell=True)
