from turtle import *
from random import randint

speed(0)
pen({'pencolor':'red'})

def hola():
    print("Hola")

def r():
    goto(randint(1,500)-250, randint(1,500)-250)

onkey(hola,'Up')
onkey(r, 'r')

def mandalita(longitud): 
    for chancleta in range(20):
        for sahumerio in range(24):
            forward(longitud)
            right(15)
        right(18)

listen()
mandalita(10)
mainloop()

