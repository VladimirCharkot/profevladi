from turtle import *

tracer (0,0) #dibuja automaticamente?
bgcolor ("black")

# Refactor:
# Reescritura de un código que no
# impacta la ejecución, generalmente
# hecha para mantenimiento del código.

def astro(color, tamanio):
    pencolor (color)
    fillcolor (color)
    pensize (6)
    begin_fill()
    circle (tamanio)
    end_fill ()


def sol(x, y):
    saltar(x,y)
    astro("yellow", 90)

def mercurio(x, y):
    saltar(x,y)
    astro("grey", 20)
    
def venus(x, y):
    saltar(x,y)
    astro("brown", 15)
            
def tierra(x, y):
    saltar(x,y)
    astro("dodgerblue2", 20)

def marte(x, y):
    saltar(x,y)
    astro("red", 30)

def jupiter (x, y):
    saltar(x,y)
    astro("darkorange3", 70)

def saturno (x, y):
    saltar(x,y)
    astro("orange3", 50)

def urano (x, y):
    saltar(x,y)
    astro("cyan4", 40)

def neptuno (x, y):
    saltar(x,y)
    astro("dodgerblue3", 40)

def pluton (x, y):
    saltar(x,y)
    astro("chocolate3", 20)


def saltar(x, y):
    penup()
    goto (x, y)
    pendown ()

from math import sin, cos

def solar ():
    sol (0, -45)
    mercurio (10, -20)
##    mercurio(120*cos(t), 50*sin(t))
    venus (30,-130)
    tierra (90,-190)
    marte (-100, -250)
    jupiter (-300,-300)
    saturno (320,320)
    urano (-290, 320)
    neptuno (300,-290)
    pluton (400,-10)
    update()

solar()
##from time import sleep
##for i in range(100):
##    clear()
##    solar(i*0.1)
##    sleep(0.1)
    
