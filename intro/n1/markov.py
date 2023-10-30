from random import randint
from time import sleep

# Clase 3 - Hola while

estado = 'soleado'

while True:

    print(estado)
    sleep(0.5)

    n = randint(1, 100)

    if estado == 'soleado':
        if n > 0 and n < 11:
            estado = 'lluvia'
        if n > 10 and n < 51:
            estado = 'nublado'
        if n > 50 and n < 101:
            estado = 'soleado'

    if estado == 'nublado':
        if n > 0 and n < 21:
            estado = 'lluvia'
        if n > 20 and n < 61:
            estado = 'nublado'
        if n > 60 and n < 101:
            estado = 'soleado'

    if estado == 'lluvia':
        if n > 0 and n < 51:
            estado = 'lluvia'
        if n > 50 and n < 91:
            estado = 'nublado'
        if n > 90 and n < 101:
            estado = 'soleado'
