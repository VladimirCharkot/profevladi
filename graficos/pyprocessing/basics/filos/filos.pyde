from random import randint, choice

opciones = []  # Imágenes originales
cabecitas = [] # Tuplas con x, y, img

def setup():
    size(600,600)
    
    # Tan solo tienen que estar en la misma carpeta del script:
    spinoza = loadImage("Spinoza.png")
    heidegger = loadImage("Heidegger.png")
    wittgenstein = loadImage("Wittgenstein.png")
    peirce = loadImage("Peirce.png")
    hegel = loadImage("Hegel.png")
    
    # Lista que vamos a *leer* desde mouseClicked
    global opciones
    opciones = [spinoza, heidegger, wittgenstein, peirce, hegel]
    
    # Esto es para que las imgs salgan centradas:
    imageMode(CENTER)   


def draw():
    background(250)
    
    perspectiva(10)
        
    for x, y, img in cabecitas:
        image(img, x, y, 100, 100)
        
        
def mouseClicked():
    # Lista que vamos a *leer* desde draw
    global cabecitas
    cabecita_random = choice(opciones)
    cabecitas += [(mouseX, mouseY, cabecita_random)]
    
    
# Modularización is nice c: 
    
def perspectiva(n):
    d = width/10
    for r in range(n):
        line(d * r, 0, mouseX, mouseY)
    for r in range(n):
        line(0, d * r, mouseX, mouseY)
    for r in range(n):
        line(d * r, height, mouseX, mouseY)
    for r in range(n):
        line(width, d * r, mouseX, mouseY)
