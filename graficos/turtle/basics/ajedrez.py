from turtle import *

speed(0)

def cuadradito(lado, el_color):
    fillcolor(el_color)
    begin_fill()
    for i in range(4):
        forward(lado)
        right(90)
    end_fill()

def dibujar_tablero(lado):
    pos_inicial = position()
    x_inicial = pos_inicial[0]
    y_inicial = pos_inicial[1]
    
    for j in range(8):
        penup()
        goto(x_inicial, y_inicial-j*lado)
        pendown()
        for i in range(8):
            cuadradito(lado, 'black' if (i+j) % 2 == 0 else 'white')
            forward(lado)


l = 50
goto(-4*l, 4*l)
dibujar_tablero(l)

# dibujar_tablero(30)   # hardcodeado


