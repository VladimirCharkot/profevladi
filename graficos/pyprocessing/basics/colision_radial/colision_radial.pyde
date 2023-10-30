x = 0
y = 0

def setup():
    size(600, 600)
    global x
    global y
    x = width/2
    y = height/2
    
def draw():
    background(0)
    global x
    global y

    v = 5 
    if keyPressed:
        if key == 'a':
            x -= 5
        if key == 'd':
            x += 5
    
    diam = 150
    circle(x, y, diam)
    
    d = dist(x, y, mouseX, mouseY)
    
    textSize(30)
    text(str(d), 20, 40)
    
    if d < diam/2: 
        t = "Tocando"
    else: 
        t = "No tocando"
        
    text(t, 20, height - 40)
