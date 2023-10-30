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

g = {'F' : '+F--F+'}

def expandir(s, n):
    if n == 0:
        return s
    else:
        return ''.join([c if c not in g else expandir(g[c], n-1) for c in s])

arbol = expandir('F',5)
#print('Instrucciones a ejecutar:')
#print(arbol)

def saltar(p):
    penup()
    goto(p)
    pendown()

speed(0)
#tracer(0,0)
screensize(1000,5000)

p_inicial = Vec2D(0,-300)

saltar(p_inicial)
seth(90)

def dibujar(instrucciones, l):
    
    while instrucciones:

        # Consumo una instrucción:
        instruccion = instrucciones[0]
        instrucciones = instrucciones[1:]

        #print(instruccion)
        #sleep(0.2)
        
        if instruccion == 'F':
            forward(l)
        if instruccion == '+':
            left(45)
        if instruccion == '-':
            right(45)
        if instruccion == '{':
            p = pos()
            h = heading()
            instrucciones = dibujar(instrucciones, l * 0.7)
            saltar(p)
            setheading(h)
        if instruccion == '}':
            return instrucciones

dibujar(arbol, 15)
