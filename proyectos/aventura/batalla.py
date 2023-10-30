from random import randint

# Clase 8 - Diccionarios

def posicion(c, texto):
    for i in range(len(texto)):
        if texto[i] == c:
            return i

def lanzar(cuantos, caras):
    suma = 0
    for i in range(cuantos):
        suma += randint(1, caras)
    return suma

def tirada(dados):
    d = posicion('d', dados)
    n = int(dados[:d])
    c = int(dados[d+1:])
    return lanzar(n, c)

def atacar(pj1, pj2):
    daño = tirada(pj1['atk']) + pj1['acumulado']
    pj2['hp'] -= daño
    if pj2['hp'] < 0:
        pj2['hp'] = 0
    pj1['acumulado'] = int(pj1['acumulado'] / 2)

def acumular(pj):
    pj['acumulado'] += 3
    pj['acumulado'] = int(1.3 * pj['acumulado'])


def batalla(pj1, pj2):
    print(f"{pj1['nombre']} ({pj1['hp_max']}HP) y {pj2['nombre']} ({pj2['hp_max']}HP) se trenzan en batalla")
    print()

    while pj1['hp'] > 0 and pj2['hp'] > 0:
        # Se asume que pj1 es el usuario
        accion = input("Qué vas a hacer? (a)tacar, a(c)umular, (e)scapar > ")
        if accion == 'a':
            atacar(pj1, pj2)
        if accion == 'c':
            acumular(pj1)
        if accion == 'e':
            if randint(1,100) < 80:
                break

        atacar(pj2, pj1)

        print(f"{pj1['nombre']}: {pj1['hp']}HP (+{pj1['acumulado']}atk)")
        print(f"{pj2['nombre']}: {pj2['hp']}HP")


    if pj1['hp'] == 0 and pj2['hp'] == 0:
        print("Empate")
        return 0
    elif pj1['hp'] > 0 and pj2['hp'] > 0:
        print("Escapaste...")
        return 2
    elif pj1['hp'] > 0:
        print(f"Ganó {pj1['nombre']}")
        return -1
    else:
        print(f"Ganó {pj2['nombre']}")
        return 1


jugador = {'nombre' : 'Melián', 'hp_max' : 105, 'hp' : 105, 'atk' : '3d6', 'acumulado': 0}
enemigo = {'nombre' : 'Fermín', 'hp_max' : 140, 'hp' : 140, 'atk' : '3d4', 'acumulado': 0}
