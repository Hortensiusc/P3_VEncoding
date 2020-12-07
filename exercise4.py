# Carlos Hortensius U150010

# Practice 3 Video Encoding Systems

import os
import subprocess
import random
from functions import *


video_codecs = ['mpeg2', 'h264', 'avs', 'avs+']
audio_codecs = ['ac3', 'dra', 'acc', 'mp2', 'mp3']

video_codec = random.choice(video_codecs)
audio_codec = random.choice(audio_codecs)

print('Your video codec is ', video_codec, ' and your audio codec is ', audio_codec, '\n')


broadcasting(video_codec, audio_codec)

