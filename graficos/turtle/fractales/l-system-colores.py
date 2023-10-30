from turtle import *
from time import sleep

# Alfabeto: A, B
# Axioma: A
# Gramática:
#   A -> AB
#   B -> A

g = {'A' : 'AB',
     'B' : 'A'}

g = {'F' : 'FF+{+F-F-F}-{-F+F+F}'}

#g = {'F' : 'F+{-F-F}-{+F+F}'}

def expandir(s, n):
    if n == 0:
        return s
    else:
        return ''.join([c if c not in g else expandir(g[c], n-1) for c in s])

niveles = 4
arbol = expandir('F',niveles)
#print('Instrucciones a ejecutar:')
#print(arbol)

def saltar(p):
    penup()
    goto(p)
    pendown()

speed(0)
tracer(0,0)
screensize(1000,5000)

p_inicial = Vec2D(0,-300)

saltar(p_inicial)
seth(90)

colores = ['#30A2FF', '#00C4FF', '#CD1818', '#E55807', '#7E1717', '#5C8984', '#545B77', '#374259']

def dibujar(instrucciones, l, nivel):

    pencolor(colores[nivel])
    
    while instrucciones:

        # Consumo una instrucción:
        instruccion = instrucciones[0]
        instrucciones = instrucciones[1:]

        #print(instruccion)
        #sleep(0.2)
        
        if instruccion == 'F':
            forward(l)
        if instruccion == '+':
            right(25)
        if instruccion == '-':
            left(25)
        if instruccion == '{':
            p = pos()
            h = heading()
            instrucciones = dibujar(instrucciones, l * 0.7, nivel + 1)
            saltar(p)
            setheading(h)
        if instruccion == '}':
            return instrucciones

dibujar(arbol, 100/niveles, 0)
