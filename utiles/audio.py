# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 20:30:53 2017

@author: usuario
"""

import math        #import needed modules
import pyaudio     #sudo apt-get install python-pyaudio

PyAudio = pyaudio.PyAudio     #initialize pyaudio

#See https://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 256000     #number of frames per second/frameset.      

FREQUENCY = 440     #Hz, waves per second, 261.63=C4-note.
LENGTH = 1     #seconds to play sound

if FREQUENCY > BITRATE:
    BITRATE = FREQUENCY+100

frames = int(BITRATE * LENGTH)
RESTFRAMES = frames % BITRATE
data = ''

def theWave(t):
    return str( int( math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128 ) )


#generating wawes
for x in range(frames):
 data = data + theWave(x)

for x in range(RESTFRAMES): 
 data = data + chr(128)

p = PyAudio()
stream = p.open(format = p.get_format_from_width(1), 
                channels = 1, 
                rate = BITRATE, 
                output = True)

stream.write(data)
stream.stop_stream()
stream.close()
p.terminate()