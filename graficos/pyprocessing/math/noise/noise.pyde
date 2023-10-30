def setup():
    size(600, 600)

nx = 0
def draw():
    background(200)
    t = millis() / 20

    x = noise(float(t)/40) * width
    y = noise(float(t)/40 + 56539) * height

    c = t % 256 if t % 512 < 256 else 255 - t % 256
    
    fill(c)
    circle(x, y, 20)
    
