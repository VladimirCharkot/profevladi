def setup():
    size(400, 400)

x = 0

def draw():
    global x
    x += 5
    
    b = 255 * (mouseX / 400.0)
    
    background(200, 100, b)
    
    if x > 400: 
        x = 0
        
    circle(mouseY, x, 50)
