barco = None

def setup():
    global barco
    barco = loadImage('barco.png')
    size(400, 400)
    print(barco.width, barco.height)
    #imageMode(CENTER)

x = 200
y = 200

def draw():
    background(100)
    global x
    global y
    w = barco.width
    h = barco.height
    
    if keyPressed:
        if key == 'a':
            x -= 5
        if key == 'd':
            x += 5
            
    image(barco, x, y, barco.width, barco.height)
    
    if mouseX > x and mouseX < x + w and mouseY > y and mouseY < y + h:
        t = "Tocando"
    else:
        t = "No tocando"
        
    textSize(20)
    text(t, 20, height - 20)
    
    text(str(x) + ", " + str(y), width - 100, height - 50)
    text(str(mouseX) + ", " + str(mouseY), width - 100, height - 20)
