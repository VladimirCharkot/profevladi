def setup():
    size(600, 600)
    pintar()

nx = 0
    
def mouseMoved():
    print(str(int(noise(mouseX) * 255)), 200, 200)
    
def pintar():
    loadPixels()
    for py in range(width): 
        for px in range(height):
            nx = noise(px/float(width) * mouseX)
            pixels[px + py * width] = color(px, py, nx*255)
    updatePixels()
