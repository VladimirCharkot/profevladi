from turtle import *
from random import randint

colormode(255)
rojo = 0
pensize(3)

while True:
    pencolor(rojo, 100, 100)
    rojo += 5

    if rojo > 255:
        rojo = 0
    
    forward(2)
    giro = randint(-5, 5)
    left(giro)

    if xcor() > 300:
        setx(-300)

    if ycor() > 300:
        sety(-300)
