from turtle import *

# Clase 7 - Turtle II

speed(0)

def izquierda():
    left(15)

def derecha():
    right(15)

def saltar(x,y):
    penup()
    goto(x,y)
    pendown()


lims = 330
def limites():
    x = xcor()
    y = ycor()
    if x < -lims:
        saltar(lims, y)
    if x > lims:
        saltar(-lims, y)
    if y < -lims:
        saltar(x, lims)
    if y > lims:
        saltar(x, -lims)

onkey(izquierda, 'a')
onkey(derecha, 'd')

listen()

# Game loop
while True:
    forward(10)
    limites()
