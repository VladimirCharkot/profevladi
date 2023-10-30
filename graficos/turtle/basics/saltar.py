from turtle import *
from random import randint

speed(0)

def circulo_random(r, col):
    eq = randint(-300, 300)
    yg = randint(-300, 300)
    saltar(eq, yg)
    fillcolor(col)
    begin_fill()
    circle(r)
    end_fill()

def saltar(x, y):
    penup()
    goto(x, y)
    pendown()

for i in range(50):
    r1 = randint(10, 30)
    r2 = randint(10, 30)
    r3 = randint(10, 30)
    r4 = randint(10, 30)
    circulo_random(r1, '#F7C8E0')
    circulo_random(r2, '#DFFFD8')
    circulo_random(r3, '#B4E4FF')
    circulo_random(r4, '#95BDFF')
