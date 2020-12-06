# Carlos Hortensius U150010

# Practice 3 Video Encoding Systems


def broadcasting(video_c, audio_c):
    a_codecs_dvb = ['ac3', 'acc', 'mp3']
    a_codecs_isdb = ['acc']
    a_codecs_atsc = ['ac3']
    a_codecs_dtmb = ['ac3', 'dra', 'acc', 'mp2', 'mp3']

    vcodecs_dvb = ['mpeg2', 'h264']
    vcodecs_isdb = ['mpeg2', 'h264']
    vcodecs_atsc = ['mpeg2', 'h264']
    vcodecs_dtmb = ['mpeg2', 'h264', 'avs', 'avs+']

    prove = 0

    if (audio_c in a_codecs_dvb) and (video_c in vcodecs_dvb):
        print('Your video fits in the DVB Broadcasting standarts')
        prove = 1

    if (video_c in vcodecs_isdb) and (audio_c in a_codecs_isdb):
        print('Your video fits in the ISDB Broadcasting standarts')
        prove = 1

    if (video_c in vcodecs_atsc) and (audio_c in a_codecs_atsc):
        print('Your video fits in the ATSC Broadcasting standarts')
        prove = 1

    if (video_c in vcodecs_dtmb) and (audio_c in a_codecs_dtmb):
        print('Your video fits in the DTMB Broadcasting standarts')
        prove = 1

    if prove == 0:
        print('ERROR')

    return 