import pyglet
from pyglet.shapes import Line
from math import sin, cos, pi
from pyglet.window import key

window = pyglet.window.Window()
batch = pyglet.graphics.Batch()
ls = []

def linea(x0, y0, l, a):
    return Line(x0, y0, x0 + l * sin(a), y0 + l * cos(a), batch=batch)


def abanico(x0, y0, a0, a, l):
    return [linea(x0, y0, l, a0 - a),   # Linea izquierda
            linea(x0, y0, l, a0 - 0),   # Linea centro
            linea(x0, y0, l, a0 + a)]   # Linea derecha


def arbol(x0, y0, a0, n, a, l):
    if n == 0:
        return abanico(x0, y0, a0, a, l)
    else:
        [li, lc, ld] = abanico(x0, y0, a0, a, l)
        return [li, lc, ld] +\
               arbol(li.x2, li.y2, a0 - a, n - 1, a, l / 2) +\
               arbol(lc.x2, lc.y2, a0 - 0, n - 1, a, l / 2) +\
               arbol(ld.x2, ld.y2, a0 + a, n - 1, a, l / 2)



cx = window.width / 2
cy = window.height / 2
angulo = 0

ls = arbol(cx, 150, 0, 6, angulo, 100)

@window.event
def on_key_press(symbol, modifiers):
    global ls
    global angulo
    if symbol == key.DOWN:
        angulo -= pi/18
    if symbol == key.UP:
        angulo += pi/18
    ls = arbol(cx, 150, 0, 6, angulo, 100)
    
@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()
