debug = False

def setup():
    size(600,600)

def plerp(punto0, punto1, p):
    x0, y0 = punto0
    x1, y1 = punto1
    return (x0 + (x1 - x0) * p, y0 + (y1 - y0) * p)

def pline(p1, p2):
    line(p1[0], p1[1], p2[0], p2[1])

def filtro(x):
    return -(cos(PI * x) - 1) / 2

def filtro(x):
    return 8 * x * x * x * x if x < 0.5 else 1 - (-2 * x + 2) ** 4 / 2


pos = (100, 100)
p0 = (100, 100)
p1 = (300, 300)
p2 = (100, 500)
p3 = (500, 500)

t0 = 1
dt = 1000 * 2.

def draw():
    global x, y, pos
    
    background(20)
    
    t = millis() / dt
    
    stroke(200)
    if debug: 
        pline(p0, p1)
        pline(p1, p2)
        pline(p2, p3)
        
    if t - t0 > 0 and t - t0 < 1.:
        nt = filtro(t - t0)
        pi1 = plerp(p0,   p1, nt)
        pi2 = plerp(p1,   p2, nt)
        pi3 = plerp(p2,   p3, nt)
        pii1 = plerp(pi1, pi2, nt)
        pii2 = plerp(pi2, pi3, nt)
        pos = plerp(pii1, pii2, nt)
        if debug:
            pline(pi1, pi2)
            pline(pi2, pi3)
            pline(pi1, pi2)
        
    x, y = pos

    circle(x, y, 50)

    if debug:
        text("x, y: {:.3f}, {:.3f}".format(x, y), 20, 20)
        text("t: {:.3f}".format(t), 20, 40)

    
