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

def mercurio(t):
    saltar(120*cos(t - 0.5), 50*sin(t - 0.5))
    astro("grey", 10*sin(t-0.5)+20)  
        
def venus(t):
    saltar(190*cos(t * 0.5), 60*sin(t * 0.5))
    astro("brown", 15)
            
def tierra(t):
    saltar(230*cos(t*0.9 + 0.5), 140*sin(t*0.9 + 0.5))
    astro("dodgerblue2", 20)

def marte(t):
    saltar(310*cos(t - 0.4), 110*sin(t - 0.4))
    astro("red", 30)

def jupiter (t):
    saltar(360*cos(t + 0.5), 160*sin(t + 0.5))
    astro("darkorange3", 70)

def saturno (t):
    saltar(420*cos(t + 0.8), 200*sin(t + 0.8))
    astro("orange3", 50)

def urano (t):
    saltar(490*cos(t - 0.8), 220*sin(t - 0.8))
    astro("cyan4", 40)

def neptuno (t):
    saltar(550*cos(t + 0.4), 250*sin(t + 0.4))
    astro("dodgerblue3", 40)

def pluton (t):
    saltar(650*cos(t*0.4 + 0.5), 300*sin(t*0.4 + 0.5))
    astro("chocolate3", 20)


def saltar(x, y):
    penup()
    goto (x, y)
    pendown ()

from math import sin, cos

# ¿Cómo hacemos para cambiar dinámicamente el orden en que se dibujan?
# Este problema se llama z-index, por la idea de que aparece
# el eje z, el de la profundidad.

def solar_animado(t):
    pass
    # determinar cuáles son los planetas que quedan detrás del sol
    # determinar cuáles son los planetas que quedan delante
    # dibujar todos los planetas detrás
    # dibujar el sol
    # dibujar todos los planetas delante



def solar (t):
    sol (0, -45)
    mercurio(t)
    venus (t)
    tierra (t)
    marte (t)
    jupiter (t)
    saturno (t)
    urano (t)
    neptuno (t)
    pluton (t)
    update()

##solar()
    
from time import sleep
for i in range(600):
    clear()
    solar(i*0.1)
    sleep(0.1)
    
