from turtle import *
from time import sleep

tracer(0, 0)

penup()
goto(-300, 0)
pendown()

while True:
    circle(30)
    update()
    sleep(0.1)
    forward(5)
    clear()
