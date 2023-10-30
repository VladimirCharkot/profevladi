# -*- coding: utf-8 -*-

abc = 'abcdefghijklmnñopqrstuvwxyzáéíóú'


def cesar(texto, n):
    cifrado = ''
    for c in texto:
        pos = abc.index(c)
        nueva_pos = pos + n
        cifrado += abc[nueva_pos]
    return cifrado



def escitala(texto, n):
    longitud_texto = len(texto)
    vueltas = int(longitud_texto / n) + 1
    longitud_cinta = vueltas * n
    cifrado = [' ' * longitud_cinta]
    i = 0
    for c in texto:
#        pos = int(i / ???)
 #       cifrado[]
        i += 1

print(cesar("lalala", 3))
