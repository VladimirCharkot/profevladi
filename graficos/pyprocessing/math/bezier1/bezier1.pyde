debug = True

def setup():
    size(600,600)

def plerp(punto0, punto1, p):
    x0, y0 = punto0
    x1, y1 = punto1
    return (x0 + (x1 - x0) * p, y0 + (y1 - y0) * p)

def pline(p1, p2):
    line(p1[0], p1[1], p2[0], p2[1])

def filtro(x):
    c1 = 1.70158;
    c2 = c1 * 1.525;
    return ((2 * x) ** 2  * ((c2 + 1) * 2 * x - c2)) / 2 if x < 0.5 \
      else (((2 * x - 2) ** 2) * ((c2 + 1) * (x * 2 - 2) + c2) + 2) / 2


pos = (100, 100)
p0 = (100, 100)
p1 = (300, 300)
p2 = (100, 500)

t0 = 0
dt = 10000 * 1.

def draw():
    global x, y, pos
    
    background(20)
    
    t = millis() / dt
    
    stroke(200)
    pline(p0, p1)
    pline(p1, p2)
    
    if t - t0 > 0 and t - t0 < 1.:
        #nt = filtro(t - t0)
        nt = t - t0
        pi1 = plerp(p0,   p1, nt)
        pi2 = plerp(p1,   p2, nt)
        pline(pi1, pi2)
        pos = plerp(pi1, pi2, nt)
        
    x, y = pos

    circle(x, y, 10)

    if debug:
        text("x, y: {:.3f}, {:.3f}".format(x, y), 20, 20)
        text("t: {:.3f}".format(t), 20, 40)
        
