barco = None
bandera = None

def setup():
    global barco
    global bandera
    barco = loadImage('barco.png')
    bandera = loadImage('bandera.png')
    size(400, 400)
    print('Setup listo')

x = 200
y = 200

xbandera = 20
ybandera = 20

def draw():
    background(50, 100, 200)
    global x
    global y
    w = barco.width
    h = barco.height

    if keyPressed:
        if key == 'a':
            x -= 5
        if key == 'd':
            x += 5
        if key == 'w':
            y -= 5
        if key == 's':
            y += 5

    image(barco, x, y, w, h)
    image(bandera, xbandera, ybandera, bandera.width, bandera.height)

    if colisionRectPunto(x, y, w, h, mouseX, mouseY):
        t = "Tocando mouse"
    else:
        t = "No tocando mouse"
        
    if colisionRectRect(x, y, w, h, xbandera, ybandera, bandera.width, bandera.height):
        t2 = "Colision"
    else:
        t2 = "No colision"

    textSize(20)
    text(t, 20, height - 20)
    text(t2, 20, height - 50)

    
def colisionRectPunto(rx, ry, rw, rh, px, py):
    if px > rx and px < rx + rw and py > y and py < ry + rh:
        return True
    else:
        return False
    
def colisionRectRect(r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h):
    if colisionRectPunto(r1x, r1y, r1w, r1h, r2x, r2y):
        return True
    if colisionRectPunto(r1x, r1y, r1w, r1h, r2x + r2w, r2y):
        return True
    if colisionRectPunto(r1x, r1y, r1w, r1h, r2x, r2y + r2h):
        return True
    if colisionRectPunto(r1x, r1y, r1w, r1h, r2x + r2w, r2y + r2h):
        return True
    return False
    
