from turtle import *

speed('fastest')
pensize(3)

def serpentina():

    largo = 25
    corto = 10

    for i in range(20):
        for j in range(2):
            forward(largo)
            left(90)
        for j in range(2):
            forward(corto)
            left(90)


def crucecita():
    largo = 45
    corto = 10

    for i in range(4):
        for j in range(2):
            forward(largo)
            left(90)
            
            forward(corto)
            left(90)
            forward(corto)
            left(90)
            
        forward(largo)
        left(90)
    

def firulete():

    largo = 65
    corto = 15

    a1 = 15
    a2 = 2 * a1
    a3 = 180 - a2

    left(a1)

    for i in range(10):
        forward(largo)

        right(a2)
        forward(corto)
        right(a3)
        forward(corto)
        right(a2)
        
        forward(largo)

        left(a2)
        forward(corto)
        left(a3)
        forward(corto)

        left(a2)

def saltar(x, y):
    penup()
    goto(x, y)
    pendown()










saltar(-200, -200)
serpentina()

saltar(-100, 100)
crucecita()

saltar(100, -200)
firulete()
