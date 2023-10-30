from itertools import product

class floatMap:
    
    def __init__(self, ranges):
        self.ranges = ranges #: [(0.1, 'valor'), (0.3, 'valor2')]
        
    def pick(self, v):
        ultimo = 0
        for cota, valor in self.ranges:
            if v >= ultimo and v <= cota:
                return valor
            ultimo = cota

terrenos = floatMap([(0.2, '#0d2f56'), (0.4, '#2c80e0'), (0.5, '#f2f4ad'), (0.7, '#76e05c'), (0.85, '#594608'), (1, '#e5e5e5')])

l = 5
def cuadrado(x, y):
    rect(x * l, y * l, l, l)
    
def setup():
    size(600, 600)
    
s = 0.0025

pos = [0,0]
v = 5

def draw():
    
    if keyPressed and key == 'a':
        pos[0] -= v
    if keyPressed and key == 'd':
        pos[0] += v
    if keyPressed and key == 'w':
        pos[1] -= v
    if keyPressed and key == 's':
        pos[1] += v
        
    px, py = pos
    for x, y in product(range(width / l), range(height / l)):
        n = noise((px + x) * s, (py + y) * s)
        c = terrenos.pick(n)
        if not(n):
            print('Sin valor para {}'.format(n))
            continue
        fill(c)
        cuadrado(x, y)
        
def mouseMoved():
    global s
    s = 0.001 + (mouseY / float(height)) * 0.25
    print(s)
    
