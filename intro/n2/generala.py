import random

def rolar_dados(n):
    l = []
    for i in range(n):
        tirada = random.randint(1,6)
        l.append(tirada)
    l.sort()
    return l

    
def es_escalera(tirada):
    return (tirada == [1, 2, 3, 4, 5]) or ( tirada == [ 2, 3, 4, 5, 6] ) or ( tirada == [1, 3, 4, 5, 6] )


def es_foul(tirada):
    dos_primeros_iguales = tirada[0] == tirada[1]
    tres_primeros_iguales = dos_primeros_iguales and tirada[1] == tirada[2]
    dos_ultimos_iguales = tirada[4] == tirada[3]
    tres_ultimos_iguales = dos_ultimos_iguales and tirada[2] == tirada[3]
    return (dos_primeros_iguales and tres_ultimos_iguales) or (tres_primeros_iguales and dos_ultimos_iguales)

def es_poker(tirada):
    cuatro_primeros_iguales = tirada[0] == tirada[1] and tirada[1] == tirada[2] and tirada[2] == tirada[3]
    cuatro_ultimos_iguales = tirada[4] == tirada[1] and tirada[1] == tirada[2] and tirada[2] == tirada[3]
    return cuatro_primeros_iguales or cuatro_ultimos_iguales


