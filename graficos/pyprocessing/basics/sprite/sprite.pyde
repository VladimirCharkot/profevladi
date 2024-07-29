# Crear una clase Sprite que reciba una lista de imgs y un dt y 
# reproduza las imágenes con una diferencia aprox de dt entre una y otra.

# Que pueda moverse a izquierda y derecha con las flechas, y que al 
# moverse en una u otra de estas direcciones se oriente adecuadamente.

class Sprite:
    
    def __init__(self, imgs):
        self.pos = 0
        self.dt = 100
        self.imgs = imgs
        self.t = 0
    
    def dibujar(self):
        print(self.pos)
        print(len(self.imgs))
        imagen = self.imagenes[self.pos]
        print(imagen)
        image(imagen, width/2, height/2, 64, 64)
        print('lelele')
        
    def tick(self):
        if millis() - self.t >= self.dt:
                self.t = millis()
                self.pos += 1
                self.pos %= len(self.imgs)
                
                
imgs = []

s = None

def setup():
    imageMode(CENTER)
    size(400, 400)
    
    # Convertir en for loop:
    imgs.append(loadImage('elf/idle_1.png'))
    imgs.append(loadImage('elf/idle_2.png'))
    imgs.append(loadImage('elf/idle_3.png'))
    imgs.append(loadImage('elf/idle_4.png'))

    global s
    s = Sprite(imgs)
    
pos = 0 
dt = 100
t = 0

def draw():
    background(200)
    s.tick()
    s.dibujar()
