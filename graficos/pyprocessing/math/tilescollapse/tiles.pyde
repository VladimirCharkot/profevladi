from itertools import product
from random import choice

tes = {}
tiles = None

def rotar_imagen(lado, img, angulo):
    pg = createGraphics(lado, lado)
    pg.beginDraw()
    pg.imageMode(CENTER)
    pg.translate(lado / 2, lado / 2)
    pg.rotate(angulo)
    pg.image(img, 0, 0, lado, lado)
    pg.endDraw()
    return pg

def rotar_lista(lista, n):
    return lista[-n:] + lista[:-n]

def setup():
    global tiles
    size(600, 600)
    
    Tile.tileset = tes
    Tile.tam = 60
    
    # Tileset
    print('Creando tileset...')
    tes['v'] = {'img' : loadImage('v.png'), 'conf' : [0,0,0,0]}
    t = loadImage('t.png')
    for i in range(4):
        tes['t{}'.format(i)] = {'img' : rotar_imagen(Tile.tam, t, i * PI/2.0), 'conf' : rotar_lista([1,1,0,1], i)}  # izq, arr, dcha, abajo
    print(tes)

    # Tiles
    print('Creando tiles...')
    filas, columnas = height / Tile.tam, width / Tile.tam
    tiles = [[None for h in range(filas)] for w in range(columnas)]
    for x, y in product(range(columnas), range(filas)):
        tiles[x][y] = Tile(x, y)
    print('Setup finalizado!')
    
def draw():
    background(100)
    filas, columnas = height / Tile.tam, width / Tile.tam
    for x, y in product(range(columnas), range(filas)):
        # print('Dibujando tile {}, {}'.format(x, y))
        tiles[x][y].dibujar()
    
    
class Tile: 
    # {'id1' : {'img' : img1, 'conf': [...]}, 'id2': {'img' : img2, 'conf': [...]}, ...}
    tileset = {}
    tam = 20
    alto = 0
    ancho = 0
    
    def __init__(self, x, y):
        if not Tile.tileset:
            print('No hay tileset seteado!')
        self.x = x
        self.y = y
        self.estado = 'indeterminado'
        self.determinado = None
        self.posibilidades = Tile.tileset.keys()
        self.rlado = next(n for n in range(10) if n ** 2 > len(self.posibilidades))
        self.angulo = 0
        if x + 1 > Tile.ancho:
            Tile.ancho = x + 1
        if y + 1 > Tile.alto: 
            Tile.alto = y + 1
        
    ###########
    # Dibujo: #
    ###########
    def dibujar(self):
        self.dibujar_base()
        if self.estado == 'determinado':
            self.dibujar_determinado()
        if self.estado == 'determinando':
            self.dibujar_determinando()
        if self.estado == 'indeterminado':
            self.dibujar_posibilidades()
        
    def dibujar_base(self):
        noFill()
        strokeWeight(1)
        w = Tile.tam
        fill(200)
        rect(self.x * w, self.y * w, w, w)
        
    def dibujar_determinado(self):
        pushMatrix()
        imageMode(CENTER)
        translate(self.x * Tile.tam + Tile.tam / 2, self.y * Tile.tam + Tile.tam / 2)
        rotate(self.angulo * PI/2.0)
        image(self.tileset[self.determinado]['img'], 0, 0, Tile.tam, Tile.tam)
        imageMode(CORNER)
        popMatrix()
    
    def dibujar_posibilidades(self):
        fill(200)
        w = self.tam / self.rlado
        for i, k in enumerate(self.posibilidades):
            x = i % self.rlado
            y = i / self.rlado
            image(Tile.tileset[k]['img'], self.x * self.tam + x * w + 3, self.y * self.tam + y * w + 3, w - 5, w - 5)
                
    ###########
    # Estado: #
    ###########
        
    def elegir(self, posibilidad=None):
        if posibilidad:
            self.determinado = posibilidad
        else:
            self.determinado = choice(self.posibilidades)
        self.estado = 'determinando'
        self.posibilidades = []

    def colapsar(self):
        self.estado = 'determinado'
        self.propagar()
        
    def propagar(self):
        print(Tile.ancho, Tile.alto)
        vecinos = [(self.x, (self.y - 1) % Tile.alto),
                   ((self.x + 1) % Tile.ancho, self.y),
                   (self.x, (self.y + 1) % Tile.alto),
                   ((self.x - 1) % Tile.ancho, self.y)]
        print(list(enumerate(vecinos)))
        for i, vecino in enumerate(vecinos):
            vx, vy = vecino
            tiles[vx][vy].informar(Tile.tileset[self.determinado]['conf'][i], (i + 2) % 4)
            
    def informar(self, valor, lado):
        self.posibilidades = [p for p in self.posibilidades if Tile.tileset[p]['conf'][lado] == valor]
        
    def click(self, x, y):
        if self.estado == 'indeterminado':
            print('Eligiendo...')
            ix = x / (Tile.tam / self.rlado) 
            iy = y / (Tile.tam / self.rlado) 
            i = ix + iy * self.rlado
            if i < len(self.posibilidades):
                self.elegir(self.posibilidades[i])
                self.colapsar()
            else:
                self.elegir()
                self.colapsar()
            return
            


def mouseClicked():
    tx = mouseX / Tile.tam
    ty = mouseY / Tile.tam
    print('Clickeado tile {}, {}'.format(tx, ty))
    tiles[tx][ty].click(mouseX % Tile.tam, mouseY % Tile.tam)
