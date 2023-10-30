debug = True

def plerp(punto0, punto1, p):
    x0, y0 = punto0
    x1, y1 = punto1
    return (x0 + (x1 - x0) * p, y0 + (y1 - y0) * p)

def setup():
    size(600,600)

pos = (0, 0)
p0 = (0, 0)
p1 = (0,0)

t0 = 0
dt = 1000 * 1.

def draw():
    global x, y, pos
    
    background(20)
    
    t = millis() / dt
    
    if t - t0 < 1.:
        pos = plerp(p0, p1, t - t0)
        
    x, y = pos

    circle(x, y, 50)

    if debug:
        text("x, y: {:.3f}, {:.3f}".format(x, y), 20, 20)
        text("t: {:.3f}".format(t), 20, 40)
        
def mouseClicked():
    global p0, p1, t0
    p0 = p1
    p1 = (mouseX, mouseY)
    t0 = millis() / dt
    print(mouseX, mouseY)
