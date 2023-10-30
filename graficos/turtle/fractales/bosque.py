from turtle import *
from random import random, randint

speed(0)
seth(90)

def randentre(n1, n2):
    return random() * abs(n2-n1) + min(n1,n2)

def saltar(x,y):
    penup()
    goto(x, y)
    pendown()

a = 20
da = 55
def arbol(l, n=3):
    forward(l)
    na1 = a + randentre(-da/n, da/n)
    na2 = a + randentre(-da/n, da/n)
    if n == 1:
        forward(-l)
        return
    else:
        left(na1)
        arbol(l * randentre(0.5, 0.8), n-1)
        right(na1)
        right(na2)
        arbol(l * randentre(0.5, 0.8), n-1)
        left(na2)
    forward(-l)


saltar(-250, -90)
arbol(randint(40, 90), 7)
saltar(-150, -90)
arbol(randint(40, 90), 7)
saltar(-50, -90)
arbol(randint(40, 90), 7)
saltar(0, -90)
arbol(randint(40, 90), 7)
saltar(50, -90)
arbol(randint(40, 90), 7)
saltar(150, -90)
arbol(randint(40, 90), 7)
saltar(200, -90)
arbol(randint(40, 90), 7)
