from functools import cache
from random import randint
from collections import Counter

reverso = {
    1: 6,
    2: 5,
    3: 4,
    4: 3,
    5: 2,
    6: 1
}

# @cache  # Probar y medir
def mejor_culeada(tirada, p_culos):
    
    # Cache
    memo = {('[]', 0): (0, [])}

    if p_culos > len(tirada):
        raise ValueError("No puede haber más culos que dados!")

    def dp(dados, culos):

        if culos == 0:
            return dados
        
        # dados = Counter(dados_lista)
        clave = str(sorted(dados))

        # Si esta combinación ya está cacheada, reutilizamos
        if (clave, culos) in memo:
            return memo[(clave, culos)]

        este_dado = dados[0]
        
        # Vemos qué puntaje queda cuando damos vuelta el dado actual
        tirada_1 = [reverso[este_dado]] + dp(dados[1:], culos - 1)
        puntaje_1, resto_1 = colectar(tirada_1)

        # Si hay más dados que culos, aún podemos elegir y comparar
        if len(dados) > culos:
          tirada_2 = [este_dado] + dp(dados[1:], culos)
          puntaje_2, resto_2 = colectar(tirada_2)

          # Primero, es preferible optar por la que deje resto cero
          if len(resto_1) == 0:
              return tirada_1
          if len(resto_2) == 0:
              return tirada_2

          # Si ninguna lo hace, elegir la que dé mejor puntaje 
          if puntaje_1 > puntaje_2:
            memo[(clave, culos)] = tirada_1
          else: 
            memo[(clave, culos)] = tirada_2

        # Sino, hay una sola tirada posible... todos los culos aplicados
        else:
          memo[(clave, culos)] = tirada_1

        # En lugar de devolver directamente, cacheamos y devolvemos desde cache
        return memo[(clave, culos)]

    return dp(tirada, p_culos)

def tirar_con_culos(n, culos):
    tirada_lista = tirar(n)
    tirada_elegida = mejor_culeada(tirada_lista, culos)
    p = puntaje(tirada_elegida)
    print(f'Tirada {str(tirada_lista):<15} con {culos} culos resuelta a {str(tirada_elegida):<15} con puntaje y resto {p}')
    return p

def tirar(n):
    return [randint(1,6) for _ in range(n)]

def puntaje(tirada_lista):
    return colectar(tirada_lista)
    

def colectar(tirada):
    
    tirada = Counter(tirada)
    puntaje = 0

    # Números que hayan salido de a 3 o más
    triplas = [ k for k, v in tirada.items() if v >= 3 and k != 1]
    
    # Si hay tres 1s contamos mil puntos
    if tirada[1] >= 3:
        puntaje += 1000
        tirada.update({1: -3})

    # Si hay tres de n contamos n * 100 puntos
    for n in triplas:
        puntaje += n * 100
        tirada.update({n: -3})

    # Sumamos los 1s y 5s que queden sueltos:
    unos = tirada[1]
    tirada[1] = 0
    cincos = tirada[5]
    tirada[5] = 0
    puntaje += unos * 100 + cincos * 50
    
    return puntaje, list(tirada.elements())

culos_a_cantar = {
    5: 2,
    4: 2,
    3: 1,
    2: 1,
    1: 0
}

def entrar():
    puntaje = 0
    dados = 5
    while puntaje < 750 and dados:
        puntos, resto = tirar_con_culos(dados, culos_a_cantar[dados])
        dados = len(resto)
        puntaje += puntos
        if puntos == 0:
            break
        if dados == 0:
            dados = 5
    if puntos == 0: return 0
    return puntaje

if __name__ == '__main__':
    p = entrar()
    if p:
        print(f'Entraste con {p} puntos')
    else:
        print(f'Seguí participando')
