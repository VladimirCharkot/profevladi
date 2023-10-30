import random
import math
import itertools

f = open('castellano.txt', encoding='utf8')
contenido_archivo = f.read()
f.close()

diccionario = contenido_archivo.split('\n')


def buscar_anagrama(palabra):
    l = list(palabra)
    for i in range(1000):
        random.shuffle(l)
        intento = ''.join(l)
        #print('Intentando', intento)
        if intento in diccionario:     
            return intento
    return 'Nada'


def buscar_anagrama_l(palabra):
    l = list(palabra)
    permutaciones = itertools.permutations(palabra)
    encontrada = []
    for perm in permutaciones:
        intento = "".join(perm)
        if intento in diccionario and intento not in encontrada:
            encontrada.append(intento)

    return encontrada



