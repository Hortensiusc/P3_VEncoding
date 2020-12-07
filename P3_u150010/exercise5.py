# Carlos Hortensius U150010

# Practice 3 Video Encoding Systems

import random
from functions import *

class P3:
    video_codecs = ['mpeg2', 'h264', 'avs', 'avs+']
    audio_codecs = ['ac3', 'dra', 'acc', 'mp2', 'mp3']
    video_codec = random.choice(video_codecs)
    audio_codec = random.choice(audio_codecs)

