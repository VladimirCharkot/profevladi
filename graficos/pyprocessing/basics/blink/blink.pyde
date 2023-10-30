from random import randint

# Los números de los colores pueden ir entre 0 y 255

def setup():
    size(600, 600)
    
def draw():
    v = randint(100, 200)
    background(120, v, 200)
    stroke(0, 0, 0)
    fill(130, 150, 170)
    circle(mouseX, mouseY, 50)
    stroke(60, 200, 120)
    line(100, 100, 300, 200)
    rect(300, 300, 200, 100)
    
def mouseClicked():
    print(mouseX, mouseY)
