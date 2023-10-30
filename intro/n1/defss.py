# Definicion de funciones
#
# Así como existen funciones como chr() o int(),
# que reciben unos valores y devuelven otros,
# también podemos definir las nuestras, con
# código propio.
#
# Una función es básicamente un tramo de código
# con nombre, entrada y salida.
#
# def nombre_funcion(entrada1, entrada2, ...):
#    {código}
#    return expresión


def es_par(numero):
    resto = numero % 2
    par = resto == 0
    return par

print('Es 564296419 par?')
print(es_par(564296419))

print('Es 520370584 par?')
print(es_par(520370584))


def jeringozo(frase):
    nueva = ''
    for letra in frase:
        if letra in 'aeiou':
            nueva = nueva + letra + 'p' + letra
        else:
            nueva = nueva + letra
    return nueva

print()
print('Ingresá una frase:')
frase = input()
print(jeringozo(frase))


def contar_lineas(texto):
    cantidad = 1
    for letra in texto:
        if letra == '\n':
            cantidad = cantidad + 1 
    return cantidad


import random

def tramboliko(texto):
    nuevo = ''
    for letra in texto:
        if letra in 'aeiou':
            nuevo = nuevo + random.choice('aeiou')
        else:
            nuevo = nuevo + letra
    return nuevo

print()
print('Ingresá una frase:')
frase = input()
print(tramboliko(frase))
