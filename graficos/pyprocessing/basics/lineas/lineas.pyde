def setup():
    size(600, 600)

def draw():
    background(100)
    n = 10
    
    d = width/n
    
    for r in range(n):
        line(d * r, 0, mouseX, mouseY)
    for r in range(n):
        line(0, d * r, mouseX, mouseY)
    for r in range(n):
        line(d * r, height, mouseX, mouseY)
    for r in range(n):
        line(width, d * r, mouseX, mouseY)
