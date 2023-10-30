from turtle import *

penup()
goto(0, -200)
seth(90)
pendown()
speed(0)

a = 20
def arbol(l, n=3):
    forward(l)
    if n == 1:
        forward(-l)
        return
    else:
        left(a)
        arbol(l * 0.7, n-1)
        right(2*a)
        arbol(l * 0.7, n-1)
        left(a)
    forward(-l)

arbol(150, 8)
