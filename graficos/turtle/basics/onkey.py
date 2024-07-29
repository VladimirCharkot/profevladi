from turtle import *
from random import randint

speed(0)
pencolor('red')

def r():
    goto(randint(1,500)-250, randint(1,500)-250)

onkey(r, 'r')

listen()
mainloop()

