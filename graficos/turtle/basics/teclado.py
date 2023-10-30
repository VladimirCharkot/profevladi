from turtle import *
from random import randint

tracer(0, 0)

def circulito():
    goto(randint(-300, 300), randint(-300,300))
    update()

onkey(circulito, 'c')
listen()
