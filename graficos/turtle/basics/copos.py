from turtle import *

pensize(2)
speed(0)
bgcolor('dark blue')
color('white')
tracer(0, 0)    # apagar animacion

def poligono(l, n=4):
    for k in range(n):
        forward(l)
        left(360/n)

def copo(l, copias=4, n=4):
    for k in range(copias):
        poligono(l, n)
        left(360/copias)

copias = 6
lados = 6
longitud = 100

def actualizar():
    print(f"{copias} copias de {lados} lados")
    clear()
    copo(longitud, copias, lados)
    update()

def unladomas():
    global lados
    lados += 1
    actualizar()

def unladomenos():
    global lados
    lados -= 1
    actualizar()

def unomas():
    global copias
    copias += 1
    actualizar()

def unomenos():
    global copias
    copias -= 1
    actualizar()


onkey(unomas,'d')
onkey(unomenos,'a')
onkey(unladomas,'w')
onkey(unladomenos,'s')

copo(longitud, copias, lados)
update()

listen()

# traducir
