from random import randint

def tirada(dados):
    lista = dados.split('d')
    cantidad = int(lista[0])
    caras = int(lista[1])
    suma = 0
    for i in range(cantidad):
        suma += randint(1, caras)
    return suma

def muestreo(dados):
    lista = dados.split('d')
    cantidad = int(lista[0])
    caras = int(lista[1]) 
    muestras = [0] * (cantidad * caras + 1)
    for i in range(10000):
        muestras[tirada(dados)] += 1
    return muestras

def grafico(muestras, ancho=80):
    tope = max(muestras)
    for muestra in muestras:
        cant = int(ancho * muestra / tope)
        print('#' * cant)