debug = True

def filtro1(x):
    return x * x * x

def filtro2(x):
    return -(cos(PI * x) - 1) / 2

def filtro3(x):
    c1 = 1.70158;
    c2 = c1 * 1.525;
    return ((2 * x) ** 2  * ((c2 + 1) * 2 * x - c2)) / 2 if x < 0.5 \
      else (((2 * x - 2) ** 2) * ((c2 + 1) * (x * 2 - 2) + c2) + 2) / 2
    
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
        pos = plerp(p0, p1, filtro3(t - t0))
        
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
