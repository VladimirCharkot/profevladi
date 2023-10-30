from turtle import *
from random import randint, choice

speed(0)
seth(90)
color("#285078", "#a0c8f0")

comandos = []

def generar_comandos(cantidad):
    cmds = []
    for i in range(cantidad):
        cmd = choice(['arr','abj','izq','der'])
        cmds.append(cmd)
    return cmds

def comandar(cmds):
    for cmd in cmds:
        if cmd == 'arr':
            arr()
        if cmd == 'abj':
            abj()
        if cmd == 'izq':
            izq()
        if cmd == 'der':
            der()

def circulo(radio):
    begin_fill()
    circle(radio)
    end_fill()

def saltar_a_random():
    penup()
    goto(randint(-200,200), randint(-200,200))
    pendown()

onkey(lambda: circulo(25), 'c')
onkey(lambda: circulo(50), 'v')
onkey(lambda: circulo(70), 'b')

def arr():
    sety(ycor() + 10)
    comandos.append('arr')
    
def abj():
    sety(ycor() - 10)
    comandos.append('abj')
    
def izq():
    setx(xcor() - 10)
    comandos.append('izq')
    
def der(): 
    setx(xcor() + 10)
    comandos.append('der')

onkey(arr, 'w')
onkey(izq, 'a')
onkey(abj, 's')
onkey(der, 'd')

onkey(lambda: print(comandos),'f')

onkey(lambda: forward(10), 'Up')
onkey(lambda: left(15), 'Left')
onkey(lambda: backward(10), 'Down')
onkey(lambda: right(15), 'Right')


onkey(saltar_a_random, 'r')

listen()


