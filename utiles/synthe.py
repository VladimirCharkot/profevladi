# -*- coding: utf-8 -*-

import struct
import numpy as np
import math as mt
#import scipy
#from scipy import signal as sg
#import pyaudio
from functools import reduce
import wave as wv
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
timbre = [0.8,0.7,0.5,0.5,0.4,0.4]      # Timbre
timbre_2 = [0.8,0.1,0.1,0.01,0.01]

DEFAULT_TIMBRE = [1,0.5,0.333,0.25,0.2,0.166,0.143,0.125]

class Tone(object):
    """Has timbre i.e. harmonics. Builds waves with those harmonics
    catch my spanglish, chico"""
    
    def __init__(self, timbre):
        self.timbre = timbre
    
    def squareTone(self, f, v=lambda c: 1, p=lambda c: 0):
        st = []
        for i, tv in enumerate(self.timbre):
            if i>1 and i%2 == 1:
                st.append(Wave(lambda c: f(c)*(i+1), 
                               lambda c: v(c) * tv, 
                               lambda c: p(c)   
                               ))
        return reduce(lambda x,y: x+y, st)
    
    def triangTone(self, f, v=lambda c: 1, p=lambda c: 0):
        tt = []
        for i, tv in enumerate(self.timbre):
            if i>1 and i%2 == 0:
                tt.append(Wave(lambda c: f(c)*(i+1), 
                               lambda c: v(c) * tv, 
                               lambda c: p(c)   ))
        return reduce(lambda x,y: x+y, tt)
    
    def armonicTone(self, f, v=lambda c: 1, p=lambda c: 0):
        return Wave(f,v,p) + self.squareTone(f,v,p) + self.triangTone(f,v,p)

class Wave(object):
    """Puede ser o una senoidal parametrizada (fvp) o una suma de estas
    iwl = iwave list
    iwave = onda parametrizada no colapsada
    freq, vol y phase son funciones de un solo parámetro
    vol va de 0 a 1"""
    
    def __init__(self, f=None, v = lambda c: 1, p = lambda c: 0, iwl=[]):
        if f and not iwl:
            self.iwl = [self.iwave(f,v,p)]
        if iwl and not f:
            self.iwl = iwl
        if iwl and f:
            raise ValueError("Puedo construir una onda con freq o iwl pero no las dos!")
    
    def __str__(self):
        return str(self.iwl)
        
    def __add__(self, w):
        iwls = self.iwl + w.iwl
        return Wave(iwl=iwls)
        
    def collapse(self, d):
        """Recibe duración d (en segs) y devuelve una función onda,
        o sea f(t)=amplitud, determinada para esa duración"""
        def det_wave(t):
            det = t/d
            if det >= 0 and det < 1:
                wave = lambda t: sum([f(det)(t) for f in self.iwl])
            else:
                wave = lambda t: 0
            return wave(t)
        return det_wave
    
    def iwave(self, freq, vol, phase):
        """Recibe fvp, cada una de las cuales es una función
        de un solo parámetro c que va de 0.0 a 1.0 en el intervalo
        total en el que suena la onda (y que se determina al 'colapsarla')
        e.g. freq(c) = 432 + 432*c, freq(c) = 432, vol(c) = c*0.4, etc
        De esta manera los parámetros son variables"""
        def iw(c):
            return lambda t: vol(c) * np.sin(phase(c) + freq(c) * (np.pi * 2) * t)
        return iw

class Synthe(object):
    sr = 0
    amp = 0
    freqs = []
    
    def __init__(self, sample_rate=44100, base_amplitude=4096):
        self.sr = sample_rate
        self.amp = base_amplitude
        #self.base_freq = base_freq
        #self.notes = self.tessitura()
        
    def tessitura(self):
        """Builds a dictionary with keys and associated frecuencies
        por ahora está al pedo"""
        notes = {}
        base_range = np.arange(-24,37)
        freqs = list(map(lambda p: self.base_freq * 2**(p/12), base_range))
        major_keys = ['A','As','B','C','Cs','D','Ds','E','F','Fs','G','Gs']
        i=0
        for f in freqs:
            notes[major_keys[i%12]+str(i//12)] = f
            i += 1 
        return notes
    
    def pureTone(self, f, v, p):
        # goodol' plain freq, vol, phase. testing
        return lambda t: v * np.sin(p + f * (np.pi * 2) * t)

    def determineWave(self, frame):
        """recibe un frame y devuelve wave(t)
        #frame = {'b' : 1.0, 'e' : 2.5, 'f' : lambda}"""
        b = frame['b']
        e = frame['e']
        w = frame['w']
        d = e - b
        collapsed = w.collapse(d)
            
        def det_wave(t):
            return collapsed(t-b)
        
        return det_wave
    
    def thread(self, frames):
        """Recibe una lista de frames [{w: wave, b: begin, e: end}]
        y plancha todas esas ondas en una sola lista para exportar"""
        ws = []
        for fr in frames: 
            ws.append(self.determineWave(fr))
            
        def wave(t):
            r = 0.0
            for dw in ws: 
                r += dw(t)
            return r*self.amp
        return wave
    
    def save(self, wave, end, start = 0.0, name = 'test-NOW.wav'):
        print("Generating wav...")
        nm = name.replace('NOW', dt.datetime.now().strftime('%Y.%m.%d-%H.%M.%S'))
        length = end - start    ## Tiempo (en s)
        sample = self.sr * length    ## Muestras (fps * s)
        trail = np.arange(sample) / self.sr + start
        sound = map(wave, trail)
        self.writeFile(sound, nm)
        
    def writeFile(self, wav, nm = 'test-' + now + '.wav'):
        print("Saving...")
        f = wv.open(nm, 'wb')
        f.setframerate(self.sr)
        f.setnchannels(1)
        f.setsampwidth(2) #16-bit = 65536
        output = []
        ## Open as Signed 8-bit on Audacity
        for i in wav:
            output.append(struct.pack('h',int(i)))
        	#f.write(struct.pack('h',int(i)))
        f.writeframes(b''.join(output))
        f.close()

#Crear objeto synthe. Esto básicamente agarra las ondas que creamos
#y las pone en un archivo wav
snt = Synthe() 

#Crear ondas. Cada onda recibe f, v y p, que son
#frecuencia, volumen y fase. No tienen que ser valores sino funciones que 
#dependen de un parámetro c que va de 0 a 1, y que refleja la 'altura'
#en el tiempo de la onda (0 es al comienzo, 0.5 a la mitad, 1 al final, etc). 
#De manera que si se quiere una onda con freq 440 en todo el intervalo 
#se indica 'lambda c: 440', que sería una función que devuelve 440 
#para cualquier valor de c; si se quiere que suba el volumen a medida que 
#la onda suena, se indica lambda c: c, lo que hace que el volumen vaya de 0 a 1
#a medida que la onda suena. Me explico?
A432 = Wave(f=lambda c: 432, v=lambda c: 4 if c<0.5 else 4*(2-c*2))
#A432 con volumen 4 que dropea a 0 después de la mitad del timelapse
E648 = Wave(f=lambda c: 648-(108*c), v=lambda c: 4*c)
#E648 con frecuencia que baja a 432. Debiera ser 648-(216*c), algo anda mal...
A432i = Wave(f=lambda c: 432, v=lambda c: 4*(1-c))
#A432 con fade

#Luego se indexan los tiempos en que se quiere que suenen las ondas
#b es para begin, e para end, w para wave, de manera que 
#{'w':E648, 'b':1.0, 'e': 4.0} indica "hacer sonar E648 desde el segundo 1
#hasta el segundo 4". El programa se encarga de "encajar" el intervalo de 
#0 a 1 de c con el intervalo de 1 a 3 de t
mysong = [{'w':A432, 'b':0.0, 'e': 3.0},
          {'w':E648, 'b':1.0, 'e': 4.0},
          {'w':A432i, 'b':4.0, 'e': 6.0}]

#Finalmente, se guarda el archivo llamando al método save, que guarda 
#una onda de n segundos. Para convertir el índice en una onda se utiliza
#el método thread.
snt.save(snt.thread(mysong), 6, name='variable_params.wav')

#Otro ejemplo. La función quadPulse varía el volumen de manera que 
#resulte un pulso.
quadPulse = lambda c: 1-4*(0.5-c)**2
pulse432 = Wave(f=lambda c: 432, v=quadPulse)
pulse544 = Wave(f=lambda c: 544, v=quadPulse)
pulse648 = Wave(f=lambda c: 648, v=quadPulse)
s=[]
l = 12
for i in range(l):
    p = i * (1)
    s.append({'w':pulse432, 'b':p, 'e':p+0.2})
for i in range(int(l/(3/2))):
    p = i*(3/2)
    s.append({'w':pulse648, 'b':p, 'e':p+0.2})
for i in range(int(l/(5/8))):
    p = i*(5/8)
    s.append({'w':pulse544, 'b':p, 'e':p+0.2})
snt.save(snt.thread(s), l, name='pulses.wav')







#PyAudio = pyaudio.PyAudio
#p = PyAudio()
#stream = p.open(format = p.get_format_from_width(1), 
#                channels = 1, 
#                rate = sr, 
#                output = True)

#data = b''
#for v in y:
#    data += np.float32(v).tostring()
#stream.write(data)

#stream.stop_stream()
#stream.close()
#p.terminate()