import random

def rolar_dados(n, dado):
    l = []
    for i in range(n):
        tirada = random.randint(1,dado)
        l.append(tirada)
    l.sort()
    return l


def tirar(tirada):
    componentes = tirada.split('d')
    cantidad = int(componentes[0])
    dado = int(componentes[1])
    resultados = rolar_dados(cantidad, dado)
    return resultados

for i in range(3):
    print('Lanzando bola de fuego', i, '...')
    daño_bola_de_fuego = sum(tirar('3d6'))
    print(daño_bola_de_fuego, 'puntos de daño')
