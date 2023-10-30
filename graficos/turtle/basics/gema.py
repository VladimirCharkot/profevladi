from turtle import *
from time import sleep

# Clase 6 - Hola turtle

speed(9)

# Instrucción
def poligono(N, L):
    for i in range(N):
        forward(L)
        left(360 / N)

def gema(C, N, L):
    for i in range(C):
        poligono(N, L)
        left(360/C)

gema(12, 6, 50)
sleep(5)
