from random import choice
from diccionario import palabras

# Python 2 - Paradigmas

print(f"Seleccionando una de las {len(palabras)} disponibles...")

def posiciones(letra, palabra):
    ps = []
    for i in range(len(palabra)):
        if palabra[i] == letra:
            ps.append(i)
    return ps

def leer_letra():
    letra = input('Cuál letra? > ')
    while len(letra) != 1:
        letra = input('Cuál letra? > ')
    return letra

def rellenar(enigma, letra, posiciones):
    for p in posiciones:
        enigma = enigma[:p] + letra + enigma[p+1:]
    return enigma

intentos = 6
palabra = choice(palabras)
enigma = palabra[0].upper() + '_' * (len(palabra)-1)

while intentos > 0 and enigma.lower() != palabra.lower():
    print()
    print(enigma)
    print()
    print(f'{intentos} intentos...')
    letra = leer_letra()
    if letra in palabra:
        ps = posiciones(letra, palabra)
        enigma = rellenar(enigma, letra, ps)
    else:
        intentos -= 1

print()
if intentos > 0:
    print("Muy bien!")
    print(palabra.upper())
else:
    print("Mordiendo el polvo eh")
    print(f"Era {palabra.upper()}")
