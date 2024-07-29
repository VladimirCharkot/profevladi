a = 0.7

class Pelota: 
    
    def __init__(self, ts, colors):
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.r = 15
        self.teclas = ts
        self.colors= colors
        
    def dibujar(self):
        r, g, b = self.colors
        fill(r, g, b)
        circle(self.x, self.y, self.r)
        
    def update(self):
        self.leer_teclas()
        self.acelerar()
        self.friccion()
        self.limites()
        
    def friccion(self):
        self.vx /= 1.02
        self.vy /= 1.02
        
    def acelerar(self):
        self.x += self.vx
        self.y += self.vy
        
    def leer_teclas(self):
        if keyPressed:
            if key == self.teclas[0]:
                self.vy -= a
            if key == self.teclas[1]:
                self.vx -= a
            if key == self.teclas[2]:
                self.vy += a
            if key == self.teclas[3]:
                self.vx += a
                
    def limites(self):
        # Que rebote en los bordes en
        # lugar de entrar por el opuesto
        if self.x > width:
            self.x = 0
        if self.y > height:
            self.y = 0  
        if self.x < 0:
            self.x = width
        if self.y < 0:
            self.y = height  
    

p1 = None
p2 = None

def setup():
    global p1
    global p2
    size(600,600)
    
    # Al llamar al nombre de la clase se ejecuta su 
    # método __init__, que devuelve un objeto de esa clase
    p1 = Pelota(['w','a','s','d'], (11,57,150))
    p2 = Pelota(['i','j','k','l'], (200,47,170))
    
    
def draw():
    background(180)
    p1.update()
    p1.dibujar()
    p2.update()
    p2.dibujar()
