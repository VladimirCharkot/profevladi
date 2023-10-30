from turtle import *
from random import randint
from math import cos, sin, radians, hypot

speed(0)


# Cómo dibujar un brazo que llegue
# hasta l unidades por delante
def brazo(l, a = 15):
    rads = radians(a)
    h = (l/2) / cos(rads)
    left(a)
    forward(h)
    right(2*a)
    forward(h)
    left(a)



# Calcula h - Trigonometría!
def hipot(a, ady):
    rads = radians(a)       # Convertimos grados a radianes...
    h = (ady/2) / cos(rads) # ...porque cos recibe radianes
    return h


def rio(l, n):
    # Ángulo al azar
    a = randint(-20,20)
    left(a)
    h = hipot(a, l)
    if n == 0:
        forward(h)
        right(2*a)
        forward(h)
    else:
        rio(h, n-1)
        right(2*a)
        rio(h, n-1)
    left(a)






# Averigua que l hay que pasarle
# a rio para llegar hasta (x, y)
def rio_hasta(x,y):
    seth(towards(x, y))
    long = hypot(x - xcor(),
                 y - ycor())    # Pitágoras!
    rio(long, 5)


def saltar(x,y):
    penup()
    goto(x,y)
    pendown()

# Dibuja un polígono
def poligono(puntos):
    p = puntos[0]
    saltar(p[0], p[1])
    pendown()
    for punto in puntos:
        goto(punto[0], punto[1])
    goto(p[0], p[1])

# Igual que un polígino, pero
# dibuja ríos en lugar de líneas
def continente(puntos):
    begin_fill()    # Empezar relleno
    p = puntos[0]
    saltar(p[0], p[1])
    pendown()
    for punto in puntos[1:]:
        rio_hasta(punto[0], punto[1])
    rio_hasta(p[0], p[1])
    end_fill()      # Cerrar relleno


##bgcolor('#226987')  # Color de fondo - Oceano

isla1 = [[0,0], [200,-20], [160,-200], [20,-160]]   # Lista de puntos
isla2 = [[-200,200], [100,100], [-100, 50]]         # Cada punto es una lista
isla3 = [[-180,-160], [-40,-50], [-50, -200]]       # de dos elementos [x,y]

##fillcolor('SpringGreen4')   # Color de relleno
##pencolor('#874f24')         # Color de trazo


# Comentá lo siguiente si querés probar
# otras cosas usando estas funciones
##continente(isla1)
##continente(isla2)
##continente(isla3)
##
### Esto dibuja un río solo:
bgcolor('SpringGreen4')
pencolor('#226987')
pensize(2)

saltar(-200, 0)
rio(400, 5)
