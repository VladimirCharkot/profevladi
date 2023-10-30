from turtle import *
from random import randint

speed ("fastest")
shape ("turtle")
ancho, alto = screensize()

def circulo (c):
    fillcolor (c)
    penup ()
    goto (randint (-ancho/2, ancho/2),\
          randint (-alto/2, alto/2))
    begin_fill ()
    pendown ()
    circle (randint (10, 150))
    end_fill ()

colores = ['#F5EFE6', '#E8DFCA', '#AEBDCA', '#7895B2']
    
for a in range (20):
    for sahumerio in colores:
        circulo (sahumerio)
