from turtle import *


# Configuración
bgcolor('#16208e')
fillcolor('#0d9193')
pencolor('white')
pensize(3)
speed(0)


# Primitivas
def saltar(x,y):
    penup()
    goto(x,y)

def circulo():
    seth(0)
    sety(ycor() - r)
    pendown()
    begin_fill()
    circle(r)
    end_fill()
    penup()
    sety(ycor() + r)



# Directivas

r = 15
def marcador(x, y):
    saltar(x,y)
    circulo()

def ruta(p0, p1):
    x1, y1 = p0
    x2, y2 = p1
    saltar(x1, y1)
    seth(0)
    left(towards(x2, y2))
    forward(r)
    pendown()
    forward(distance(x2,y2) - r)
    penup()
    forward(r)



def dibujar_mapa(puntos, conexiones):
    for p in puntos:
        marcador(p[0], p[1])
    for c in conexiones:
        ruta(c[0], c[1])


# Modelo

def dibujar(mapa):
    puntos = []
    for nombre in mapa:
        puntos += [mapa[nombre]['posicion']]
    conexiones = []
    for este_nombre in mapa:
        este_lugar = mapa[este_nombre]
        for otro_nombre in este_lugar['caminos']:
            otro_lugar = mapa[otro_nombre]
            conexiones += [(este_lugar['posicion'],
                            otro_lugar['posicion'])]
    dibujar_mapa(puntos, conexiones)
    p = puntos[0]
    saltar(p[0], p[1])
    speed(4)
    

mapa = {
'hogar'     : {
    'caminos'   : ['bosque', 'rio'],
    'posicion'  : (-200, 0)
    },
'bosque'    : {
    'caminos'   : ['hogar', 'aldea'],
    'posicion'  : (-100, 70)
    },
'aldea'     : {
    'caminos'   : ['montaña', 'bosque', 'rio'],
    'posicion'  : (50, 30)
    },
'rio'       : {
    'caminos'   : ['hogar', 'aldea'],
    'posicion'  : (0, -50)
    },
'montaña'   : {
    'caminos'   : ['aldea'],
    'posicion'  : (140, 0)
    }
}

dibujar(mapa)
