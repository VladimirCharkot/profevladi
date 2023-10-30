def setup():
    size(600, 600)
    
def draw():
    background(50)
    x = 100
    y = 100
    w = 200
    h = 150
    rect(x, y, w, h)
    
    if mouseX > x and mouseX < x + w and mouseY > y and mouseY < y + h:
        t = "Tocando"
    else:
        t = "No tocando"
        
    textSize(20)
    text(t, 20, height - 20)
