from turtle import *

colormode(255)
speed(0)

rojo = 0
largo = 20
pensize(5)

for i in range(40):
    
    pencolor(rojo, 100, 100)

    forward(largo)
    right(45)

    rojo += 5
    largo += 3


