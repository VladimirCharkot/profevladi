
def setup():
    xoff = 0.0
    background(204)
    for i in range(1000):
        xoff = xoff + .01
        n = noise(xoff) * width
        line(n, 0, n, height)
    
noiseScale = 0.02
def draw():
    background(0)
    for x in range(width):
        noiseVal = noise((mouseX + x) * noiseScale, mouseY * noiseScale)
        stroke(noiseVal * 255)
        line(x, mouseY + noiseVal * 80, x, height)
