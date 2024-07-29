from typing import Dict, List, Tuple
from itertools import groupby, takewhile, product
import re
import os

import nltk
from nltk.corpus import cess_esp, stopwords
from collections import Counter

stopwords_es = set(stopwords.words('spanish'))

def normalizar(palabras):
  tokens = []
  for palabra in palabras: 
    limpio = re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚüÜ\s]', '', palabra)
    if limpio:
      tokens.append(limpio.lower())
  return set(tokens)

def load_freqs(topn, stopwords):
  # nltk.download('cess_esp')
  palabras = cess_esp.words()
  palabras_normalizadas = [token.lower() for token in palabras if token.isalpha() and token.lower() not in stopwords]
  palabras_frecuencias = Counter(palabras_normalizadas)
  return palabras_frecuencias.most_common(topn)

dirname = os.path.dirname(__file__)
path_frecuencias = os.path.join(dirname, 'wordlist_preloaded.csv')
path_diccionario = os.path.join(dirname, 'castellano.txt') 


def read_frecuencias():
  with open(path_frecuencias, 'r') as f:
    sin_headers = f.readlines()[4:]
    sin_stopwords_aprox = sin_headers[200:]
    duplas = []
    for l in sin_stopwords_aprox:
      palabra, freq = l.split(',')
      dupla = (palabra.replace('"', ''), int(freq.strip())) 
      duplas.append(dupla)
    puntajes = {}
    for w, p in duplas:
      puntajes[w] = p
  return puntajes

# puntajes = read_frecuencias()
puntajes = load_freqs(2000, stopwords_es)

vocales = 'aeiou'

consonantes = ['b', 'c', 'ca', 'ce', 'ci', 'co', 'cu', 'd', 'f', 'g', 'ch', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'qu', 'r', 's', 't', 'v', 'z']

# 0 -> r
# 1 -> d, t
# 2 -> n
# etc...
colgadero = [
    ['r', 'rr'],
    ['d', 't'],
    ['n', 'ñ'],
    ['m'],
    ['c', 'k', 'qu', 'ca', 'co', 'cu', 'cá', 'có', 'cú'],
    ['l', 'll'],
    ['z', 's', 'ce', 'ci', 'cé', 'cí'],
    ['f', 'j'],
    ['g', 'ch'],
    ['b', 'v', 'p']
]


# Proceso de decodificar

def solo_consonantes(texto):
  pares = [a+b for a,b in zip(texto, texto[1:] + ' ')]
  return [a+b if a+b in consonantes else a for a, b in pares if a+b in consonantes or a in consonantes]

def indice(consonante):
    return next(i for i, lista in enumerate(colgadero) if consonante in lista)

def decodificar(texto):
    return ''.join([str(indice(consonante)) for consonante in solo_consonantes(texto)])


# Preprocesamos el diccionario
def mapear_diccionario(diccionario):

  mapa: Dict[str, List[str]] = {}
  pares = sorted([(palabra, decodificar(palabra))
                  for palabra in diccionario],
                  key=lambda p: p[1]
          )
  for k, g in groupby(pares, key=lambda p: p[1]):
      mapa[k] = [p[0] for p in list(g)]
  return mapa

def leer_diccionario():
  with open(path_diccionario) as f:
    diccionario = []
    for l in f.readlines():
      diccionario.append(l.strip())
  return diccionario
      
# mapa = mapear_diccionario(leer_diccionario()) 
mapa = mapear_diccionario([palabra for palabra, puntaje in puntajes]) 

# Viaje recursivo
def combinaciones_posibles(num):
    if num == '':
        return []
    candidatas = list(takewhile(
        lambda n: n in mapa,
        [num[:i+1] for i in range(len(num))]
    ))
    if not candidatas:
        return []
    posibilidades = []
    # return [[candidata] if candidata == num else [[candidata] + siguiente for siguiente in combinaciones_posibles(num[len(candidata):])] for candidata in candidatas]
    for candidata in candidatas:
        if candidata == num:
            posibilidades += [[candidata]]
        else:
            siguientes = combinaciones_posibles(num[len(candidata):])
            for siguiente in siguientes:
                posibilidades += [[candidata] + siguiente]
    return posibilidades

pagina = 100
def sugerencias(num):
    def sugerir(l): # Más viaje recursivo
        if len(l) == 1:
            return mapa[l[0]]
        else:
            subs = sugerir(l[1:])
            return [f'{a} {b}' for a, b in product(mapa[l[0]], subs)]
    sugerencias = []
    for lista in combinaciones_posibles(num):
        sugerencias += sugerir(lista)
    puntajeadas = [(frase, sum([puntajes[w] if w in puntajes else 0 for w in frase.split(" ")])) for frase in sugerencias]
    descendientes = sorted(puntajeadas, key=lambda s: -s[1])
    return [sugerencia for (sugerencia, puntaje) in descendientes[:pagina]]


if __name__ == '__main__':
    print('\n'.join(sugerencias('5739')))
    # while True:
    #     n = input("Ingresá número > ")
    #     print("Sugerencias: ")
    #     for s in sugerencias(n):
    #         print("-", s)
