# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 12:09:23 2017

@author: https://thehackerdiary.wordpress.com/2017/06/09/it-is-ridiculously-easy-to-generate-any-audio-signal-using-python/
"""

import struct
import numpy as np
import scipy
from scipy import signal as sg
import pyaudio
import datetime as dt
now = dt.datetime.now().strftime('%Y%m%d-%H%M%S')


def fargs(f):
    # Recibe funcion o valor f y 
    # devuelve funcion de un argumento
    # que aplica o devuelve f
    if not type(f) == type(lambda x: x):
        fu = lambda x: f
    else:
        fu = f
    return lambda d: fu(d)

# Parametros
amp = 1024                              ## Base amplitude
sr = 44100                              ## Sampling Rate (fps)
timbre = [0.8,0.7,0.5,0.5,0.4,0.4]      # Timbre
base_freq = 216
base_range = np.arange(-24,37)
freqs = list(map(lambda p: base_freq * 2**(p/12), base_range))



length = 6                         ## Time (in s)
sample = sr * length               ## Number of samples (fps * s)
x = np.arange(sample)

def wholeTone(x, f, v, s):
    #ds = [1.0,0.8,0.7,0.6,0.5,0.4,0.3]
    ts = [0.7,0.3,0.4,0.5,0.6,0.2] # Timbre
    r = 0
    for i, t in enumerate(ts):
        grade = i + 1
        r += pureTone(x, grade * f, v * t, s)
    return r

def pureTone(x, f, v, s):
    return v * np.sin(f * (np.pi * 2) * x / s)

def fifth(i):
    return lambda x: wholeTone(x, freqs[i], amp, sr) + wholeTone(x, freqs[i+7], amp, sr)

def major(i):
    return lambda x: fifth(x) + wholeTone[i+4]

def minor(i):
    return lambda x: fifth(x) + wholeTone[i+3]

#a1 = lambda x: wholeTone(x, freqs[24], amp, sr)
a1 = lambda x: wholeTone(x, freqs[12], amp, sr)
c1 = lambda x: wholeTone(x, freqs[16], amp, sr)
e1 = lambda x: wholeTone(x, freqs[19], amp, sr)
g1 = lambda x: wholeTone(x, freqs[24], amp, sr)


f1 = lambda x: wholeTone(x, 108, amp, sr) #La1
f2 = lambda x: wholeTone(x, 216, amp, sr) #La2
f3 = lambda x: wholeTone(x, 324, amp, sr) #Mi2
f4 = lambda x: wholeTone(x, 432, amp, sr) #La3
f5 = lambda x: wholeTone(x, 540, amp, sr) #Do#3
f6 = lambda x: wholeTone(x, 648, amp, sr) #La4
f7 = lambda x: wholeTone(x, 756, amp, sr) #

def soundz(t):
    s = t/sr
    r = 0.0
    if s >= 0 and s <= 6: r += a1(t)
    if s >= 0 and s <= 3: r += c1(t)
    if s >= 3 and s <= 6: r += e1(t)
    return r

####### sine wave ###########
#y = 128*np.sin(omega * x)
#y = map(lambda t: a1(t) + c1(t) + e1(t) + g1(t), x)
y = map(lambda t: soundz(t), x)



def saveWave(y, nm = 'test-' + now + '.wav'):
    f = open(nm,'wb')
    ## Open as Signed 8-bit on Audacity - Watch Video for instructions
    for i in y:
    	#print(i)
    	f.write(struct.pack('h',int(i)))
    f.close()

saveWave(y,'Maj-La3.wav')


PyAudio = pyaudio.PyAudio
p = PyAudio()
stream = p.open(format = p.get_format_from_width(1), 
                channels = 1, 
                rate = sr, 
                output = True)

data = b''
for v in y:
    data += np.float32(v).tostring()
stream.write(data)

stream.stop_stream()
stream.close()
p.terminate()