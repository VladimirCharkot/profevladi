def setup():
    size(600,600)
    background(200)

t = 0
def draw():
    clear()
    background(200)
    translate(300, 300)
    global t
    t += 0.02
    
    x = 120 * cos(t)
    y = 60 * sin(t)
    s = 25 * sin(t - PI) + 50
    c = 25 * sin(t - PI) + 220
    fill(c)
    circle(x, y, s)
