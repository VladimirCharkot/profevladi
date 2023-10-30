from turtle import *

def cuadrado(zapatilla):
    for i in range(4):
        forward(zapatilla)
        left(90)
        
cuadrado(80)
penup()
goto(-200, -200)
pendown()
cuadrado(400)
