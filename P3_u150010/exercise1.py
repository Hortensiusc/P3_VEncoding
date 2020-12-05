# Carlos Hortensius U150010

# Practice 3 Video Encoding Systems

import os
import subprocess

print('Welcome to Practice: Introduce the path where your video is located:\n')
path = input()
os.chdir(path)


print('Introduce the name of your video:\n')
video = input()

subprocess.call(['ffmpeg', '-ss', '0', '-i', video, '-t', '60', '-c', 'copy', 'BBB1Min.mp4'])

# Extract audio and pass it to mono
extract_audio = 'ffmpeg -i BBB1Min.mp4 -vn -acodec mp3 audio_BBB.mp3'
subprocess.call(extract_audio, shell=True)

to_mono = 'ffmpeg -i audio_BBB.mp3 -ac 1 audio_BBB_mono.mp3'
subprocess.call(to_mono, shell=True)

# Change bitrate of the audio
bit_rate = 'ffmpeg -i audio_BBB_mono.mp3 -b:a 20K audio_BBB_final.mp3'
subprocess.call(bit_rate, shell=True)

# Add subtitles
subtitles = 'ffmpeg -i BBB1Min.mp4 -vf subtitles=subtitles.srt BBB_Subtitles.mp4'
subprocess.call(subtitles, shell=True)

audio_fuera = 'ffmpeg -i BBB_Subtitles.mp4 -c copy -an no_audio_final.mp4'
subprocess.call(audio_fuera, shell=True)

# All together
final = 'ffmpeg -i no_audio_final.mp4 -i audio_BBB_final.mp3 -c:v mpeg4 -c:a mp3 output.mp4'
subprocess.call(final, shell=True)