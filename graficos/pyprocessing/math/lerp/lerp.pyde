debug = True

def lerp(v0, v1, p):
    return v0 + (v1 - v0) * p

def setup():
    size(600,600)
    
# Ejercicio: usar la función mouseClicked() para 
# llevar el circulo desde donde se encuentra hasta 
# donde se clickeó, usando lerp 

def draw():
    background(20)
    u = mouseX / float(width)
    v = mouseY / float(height)
    dt = 1000 * 1.
    t = millis() / dt
    
    circle(lerp(400, 100, t % 1.), lerp(100, 500, t % 1.), 50)
    
    fill(lerp(100, 200, t % 1.))
    circle(500, 100, 75)
    fill(255)
    
    if debug:
        text("u, v: {:.3f}, {:.3f}".format(u, v), 20, 20)
        text("t: {:.3f}".format(t), 20, 40)
        
def mouseClicked():
    print(mouseX, mouseY)
