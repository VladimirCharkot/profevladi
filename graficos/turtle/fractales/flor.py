from turtle import *
from math import sin, cos, pi

def jump(x,y):
    penup()
    goto(x,y)
    pendown()

def flor(lv, r):
    if lv == 0:
        return
    circle(r)
    centro = position()
    cx = centro[0]
    cy = centro[1]
    for i in range(6):
        angulo = i * pi/3
        nx = cx + r * cos(angulo)
        ny = cy + r * sin(angulo)
        #print(f'Jumping {nx}, {ny}')
        jump(nx, ny)
        flor(lv-1, r)
    update()
        

tracer(0, 0)
flor(3, 50)
