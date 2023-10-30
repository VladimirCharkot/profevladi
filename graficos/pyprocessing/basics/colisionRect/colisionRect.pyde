from random import randint

panda = None
bambu = None

def setup():
    size(400, 400)
    global panda
    global bambu
    panda = loadImage('Pink_Monster.png')
    bambu = loadImage('bambu.png')
    
panda_x = 100
panda_y = 100

bambu_x = 200
bambu_y = 200

def draw():
    background(155)
    global panda_x
    global panda_y 
    global bambu_x
    global bambu_y
    
    if keyPressed:
        if key == 'd': 
            panda_x += 5
        if key == 'a':
            panda_x -= 5
        if key == 'w':
            panda_y -= 5
        if key == 's':
            panda_y += 5
            
    image(panda, panda_x, panda_y)
    image(bambu, bambu_x, bambu_y)
    
    tocando = colisionPuntoRect(panda_x, panda_y, bambu_x, bambu_y, bambu.width, bambu.height) or colisionPuntoRect(panda_x + panda.width, panda_y, bambu_x, bambu_y, bambu.width, bambu.height) or colisionPuntoRect(panda_x, panda_y + panda.height, bambu_x, bambu_y, bambu.width, bambu.height) or colisionPuntoRect(panda_x + panda.width, panda_y + panda.height, bambu_x, bambu_y, bambu.width, bambu.height)
        
    if tocando: 
        bambu_x = randint(0, width - bambu.width)
        bambu_y = randint(0, height - bambu.height)
        text('Tocando', 10, 10)
    else:
        text('No tocando', 10, 10)
        
    text(str(mouseX) + ', ' + str(mouseY), 10, height - 20)
    
def colisionPuntoRect(x, y, rx, ry, rw, rh):
    if  x > rx and x < rx + rw and \
        y > ry and y < ry + rh:
        return True
    else:
        return False
        
