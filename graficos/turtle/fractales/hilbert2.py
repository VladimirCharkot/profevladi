from turtle import *

def hilbert(lv, direccion, step):
    if lv == 0:
        return
    
    right(direccion)
    hilbert(lv-1, -direccion, step)
    
    forward(step)
    left(direccion)
    hilbert(lv-1, direccion, step)
    
    forward(step)
    hilbert(lv-1, direccion, step)
    
    left(direccion)
    forward(step)
    hilbert(lv-1, -direccion, step)
    right(direccion)

# Posición inicial
penup()
goto(-20*(2**3-1), 20*(2**3-1))
pendown()

hilbert(3, 90, 20)
