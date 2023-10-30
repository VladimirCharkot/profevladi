imagen = None

def setup():
    global imagen
    size(600, 600)
    imagen = loadImage('mariposa.png')

def draw():
    image(imagen, 100, 100)
    
def mouseClicked():
    background(250, 200, 150)
    image(imagen, mouseX, mouseY)
    
