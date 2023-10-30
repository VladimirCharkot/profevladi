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
        def fu(x): return f
    else:
        fu = f
    return lambda d: fu(d)


# Parametros
amp = 1024  # Base amplitude
sr = 44100  # Sampling Rate (fps)
timbre = [0.8, 0.7, 0.5, 0.5, 0.4, 0.4]      # Timbre
base_freq = 216
base_range = np.arange(-24, 37)
freqs = list(map(lambda p: base_freq * 2**(p/12), base_range))


length = 12  # Time (in s)
sample = sr * length  # Number of samples (fps * s)
x = np.arange(sample)


def wholeTone(x, f, v, s):
    # ts = [1.0,0.8,0.7,0.6,0.5,0.4,0.3]
    ts = [0.7, 0.3, 0.4, 0.5, 0.6, 0.2]  # Timbre
    r = 0
    for i, t in enumerate(ts):
        grade = i + 1
        r += pureTone(x, grade * f, v * t, s)
    return r


def pureTone(x, f, v, s):
    return v * np.sin(f * (np.pi * 2) * x / s)


def p1(x): return wholeTone(-x, 440, amp*4, sr)
def p2(x): return wholeTone(x, 660, amp*4, sr)

# a1 = lambda x: wholeTone(x, freqs[24], amp, sr)


def a1(x): return wholeTone(x, freqs[12], amp, sr)
def c1(x): return wholeTone(x, freqs[16], amp, sr)
def e1(x): return wholeTone(x, freqs[19], amp, sr)
def g1(x): return wholeTone(x, freqs[24], amp, sr)


def f1(x): return wholeTone(x, 108, amp, sr)  # La1
def f2(x): return wholeTone(x, 216, amp, sr)  # La2
def f3(x): return wholeTone(x, 324, amp, sr)  # Mi2
def f4(x): return wholeTone(x, 432, amp, sr)  # La3
def f5(x): return wholeTone(x, 540, amp, sr)  # Do#3
def f6(x): return wholeTone(x, 648, amp, sr)  # La4
def f7(x): return wholeTone(x, 756, amp, sr)


def la_puro(x): return pureTone(x, 440, amp, sr)


sound = [{}]


def soundz(t):
    s = t/sr
    r = 0.0
    if s >= 0 and s <= 10:
        r += p1(t)
    if s >= 2 and s <= 12:
        r += p2(t)
    return r

####### sine wave ###########
# y = 128*np.sin(omega * x)
# y = map(lambda t: a1(t) + c1(t) + e1(t) + g1(t), x)


y = map(lambda t: soundz(t), x)


def saveWave(y, nm='test-' + now + '.wav'):
    f = open(nm, 'wb')
    # Open as Signed 8-bit on Audacity - Watch Video for instructions
    for i in y:
        # print(i)
        f.write(struct.pack('h', int(i)))
    f.close()


saveWave(y)


PyAudio = pyaudio.PyAudio
p = PyAudio()
stream = p.open(format=p.get_format_from_width(1),
                channels=1,
                rate=sr,
                output=True)

data = b''
for v in y:
    data += np.float32(v).tostring()
stream.write(data)

stream.stop_stream()
stream.close()
p.terminate()
