debug = True

def lerp(v0, v1, p):
    return v0 + (v1 - v0) * p

def setup():
    size(600,600)
    
# Ejercicio: usar la función mouseClicked() para 
# llevar el circulo desde donde se encuentra hasta 
# donde se clickeó, usando lerp 

x = 0
y = 0

anterior_x = 0
anterior_y = 0

proxima_x = 0
proxima_y = 0

t0 = 0
dt = 1000 * 1.

def draw():
    global x, y
    
    background(20)
    
    t = millis() / dt
    
    if t - t0 < 1.:
        x = lerp(anterior_x, proxima_x, t - t0)
        y = lerp(anterior_y, proxima_y, t - t0)

    circle(x, y, 50)
    
    if debug:
        text("x, y: {:.3f}, {:.3f}".format(x, y), 20, 20)
        text("t0: {:.3f}, t: {:.3f}, t - t0: {:.3f}".format(t0, t, t - t0), 20, 40)
        
def mouseClicked():
    global proxima_x, proxima_y, anterior_x, anterior_y, t0
    anterior_x, anterior_y = proxima_x, proxima_y
    proxima_x, proxima_y = mouseX, mouseY
    t0 = millis() / dt
    print(mouseX, mouseY)
