from random import randint

barco   = {'x' : 200, 'y' : 200, 'w' : 0, 'h' : 0, 'img': None}
bandera = {'x' : 20,  'y' : 20,  'w' : 0, 'h' : 0, 'img': None}
banderas = 0

def setup():
    print('Iniciando setup...')
    barco['img'] = loadImage('barco.png')
    barco['w'] = barco['img'].width
    barco['h'] = barco['img'].height
    bandera['img'] = loadImage('bandera.png')
    bandera['w'] = bandera['img'].width
    bandera['h'] = bandera['img'].height
    size(400, 400)
    print('Setup listo')

def draw():
    global banderas
    background(100)
    
    print('Leyendo teclado...')
    if keyPressed:
        if key == 'a':
            barco['x'] -= 5
        if key == 'd':
            barco['x'] += 5
        if key == 'w':
            barco['y'] -= 5
        if key == 's':
            barco['y'] += 5
    
    print('Dibujando imágenes')
    image(barco['img'], barco['x'], barco['y'], barco['w'], barco['h'])
    image(bandera['img'], bandera['x'], bandera['y'], bandera['w'], bandera['h'])

    print('Chequeando colision con bandera')
    if colisionRectRect(barco, bandera):
        banderas += 1
        bandera['x'] = randint(0, width)
        bandera['y'] = randint(0, height)

    textSize(20)
    text(str(banderas), 20, height - 20)

    
def colisionRectPunto(r, x, y):
    return x > r['x'] \
       and x < r['x'] + r['w'] \
       and y > r['y'] \
       and y < r['y'] + r['h']
    
def colisionRectRect(r1, r2):
    return colisionRectPunto(r1, r2['x']          , r2['y'])\
        or colisionRectPunto(r1, r2['x'] + r2['w'], r2['y'])\
        or colisionRectPunto(r1, r2['x']          , r2['y'] + r2['h'])\
        or colisionRectPunto(r1, r2['x'] + r2['w'], r2['y'] + r2['h'])

    
