from random import randint

def intercambiar(texto, i1, i2):
    p = min(i1, i2)
    s = max(i1, i2)
    nuevo = texto[:p] \
            + texto[s] + texto[p + 1:s] \
            + texto[p] + texto[s + 1:]
    return nuevo

    
def dislexia(texto):
    l = len(texto)
    i1 = randint(0, l - 1)
    i2 = randint(0, l - 1)
    if i1 == i2:
        return texto
    dislexiada = intercambiar(texto, i1, i2)
    return dislexiada


nombres = []

nombre = input('Ingresame un nombre: ')
while nombre != '':
    nombres += [nombre]
    nombre = input('Ingresame un nombre: ')

print()

for nom in nombres:
    print(f'Hola {dislexia(nom)}!')
    
