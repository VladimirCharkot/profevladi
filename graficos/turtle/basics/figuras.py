from turtle import *

# Veníamos de hacer:
##for n in range(36):
##    forward(50)
##    left(60)
##
##goto(0, 0)

speed(0)


def triangulo(cuanto):
    for i in range(3):
        forward(cuanto)
        left(120)

for i in range(36):
    triangulo(i * 3)
    left(10)


def coso(cantidad):
    for i in range(cantidad):
        forward(i * 2)
        left(120)

penup()
goto(-100, -100)
pendown()
coso(100)

penup()
goto(100, -100)
pendown()
coso(50)

penup()
goto(-100, 100)
pendown()
coso(150)

penup()
goto(100, 100)
pendown()
coso(100)
