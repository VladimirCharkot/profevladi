from turtle import *

pensize(3)
pencolor("white")
speed(9)

fillcolor((0.2, 0.5, 1.0))

def printxy():
    print (round (xcor()), round (ycor ()))

# Levantamos el lápiz, vamos 200px a la izq
# y lo apoyamos de nuevo
penup()
goto(-200, 0)
pendown()

# 10 veces:
for i in range(10):

    # Variamos el color
    fillcolor((0.1 * i, 0.5, 1.0))

    # Printeamos la posición
    printxy()
    
    # Iniciamos relleno
    begin_fill()
    circle(50)

    # Cerramos el relleno
    end_fill()

    # Levantamos el lápiz para avanzar 40
    penup()
    forward(40)
    pendown()

penup()
goto(-200, -200)
pendown()

# Lo que sigue es un copy-paste del anterior pero sin algunas cositas y con
# begin_fill y end_fill alrededor de todo el coso, en lugar de cada círculo.

pencolor("black")

begin_fill()
for i in range(10):
    circle(50)
    penup()
    forward(40)
    pendown()

end_fill()  
