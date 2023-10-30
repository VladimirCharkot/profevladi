def setup():
    size(400, 400)

x = 0

def draw():
    global x
    x += 5
    
    background(200)
    
    if x > 400: 
        x = 0
        
    circle(x, 200, 50)
