
def setup():
    size(400, 400)
    
def draw():
    if keyPressed:
        if key == 'a':
            background(0, 0, 0)
        else:
            background(200, 180, 120) # naranja suave
    else: 
        background(120, 180, 200)  # celeste suave
        
    stroke(200, 100, 0)    
    
    fill(30, 200, 100)
    circle(mouseX, mouseY, 50)
    fill(0,0,0)
    text("Holaaa", 30, 30)
    
    line(0, 20, 85, 30)
    stroke(126)
    line(85, 20, 85, 75)
    stroke(255)
    line(85, 75, 30, 75)
