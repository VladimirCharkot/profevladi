barco = None

def setup():
    global barco
    barco = loadImage('barco.png')
    size(400, 400)

x = 100
y = 100

def draw():
    background(100)
    global x
    global y
    if keyPressed:
        if key == 'a':
            x -= 5
        if key == 'd':
            x += 5
    image(barco, x, y)
