from turtle import *

def saltar(p):
    penup()
    goto(p)
    pendown()

def recordar():
    return pos(), heading()

def reestablecer(p, h):
    saltar(p)
    seth(h)

def rama(l):
    if l < 5:
        return
    else:
        forward(l)
        p, h = recordar()
        right(40)
        rama(l * 0.7)
        reestablecer(p, h)
        left(30)
        rama(l * 0.78)


speed(0)
tracer(0,0)
p_inicial = Vec2D(0,-300)
saltar(p_inicial)
seth(90)

rama(100)
