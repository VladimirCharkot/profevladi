# Crear una clase Sprite que reciba una lista de imgs y un dt y 
# reproduza las imágenes con una diferencia aprox de dt entre una y otra.

# Que pueda moverse a izquierda y derecha con las flechas, y que al 
# moverse en una u otra de estas direcciones se oriente adecuadamente.

imgs = []

def setup():
    imageMode(CENTER)
    size(400, 400)
    # Convertir en for loop:
    imgs.append(loadImage('elf/idle_1.png'))
    imgs.append(loadImage('elf/idle_2.png'))
    imgs.append(loadImage('elf/idle_3.png'))
    imgs.append(loadImage('elf/idle_4.png'))
    
pos = 0 
dt = 100
t = 0

def draw():
    background(200)
    global t
    global pos
    if millis() - t >= dt:
        t = millis()
        pos += 1
        pos %= len(imgs)
        
    image(imgs[pos], width/2, height/2, 64, 64)
