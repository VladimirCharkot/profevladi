from random import randint as rd
from time import sleep
from turtle import *

# Clase 6

speed(9)

def dado(n):
    return rd(1,n)

def dados(cant, caras):
    dados = 0
    for i in range(cant):
        dados = dados + dado(caras)
    return dados


w, h = screensize()


x = -w
y = -h

penup()
goto(x, y)
pendown()

# Recibe un n entre 1 y 18 y devuelve entre 0 y h
def f(x):
    return x * h / 18

dx = 2

# Grafica una función, con x de 2 en 2
for i in range(int(2*w/dx)):
    piso = -h
    y = piso + f(rd(3, 18))
    goto(x,y)
    x = x + dx

x = -w
y = 0
penup()
goto(x, y)
pendown()

for i in range(int(2*w/dx)):
    piso = 0
    y = piso + f(dados(3, 6))
    goto(x,y)
    x = x + dx

sleep(5)
