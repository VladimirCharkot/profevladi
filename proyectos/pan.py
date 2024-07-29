from time import time

def cerca(n, objetivo):
    return abs(objetivo - n) < 0.1

class Bowl:
    # Poner harina y sal, mezclar,
    # agregar levadura aceite y agua, mezclar
    
    def __init__(self):
        self.harina = 0
        self.agua = 0
        self.aceite = 0
        self.levadura = 0
        self.sal = 0

        self.bien_salado = False
        self.bien_mezclado = False

    def agregar(self, material, cantidad):
        if material == 'harina':
            self.harina += cantidad
        if material == 'agua':
            self.agua += cantidad
        if material == 'aceite':
            self.aceite += cantidad
        if material == 'levadura':
            self.levadura += cantidad
        if material == 'sal':
            self.sal += cantidad
        self.proporcion = self.agua / self.harina
        

    def mezclar(self):
        # Mezclando polvos
        if self.agua == 0 and self.aceite == 0 and self.harina > 0 and self.sal > 0:
            self.bien_salado = True
        # Tiene agua
        if self.agua > 0:
            if self.aceite > 0 and cerca(self.proporcion, 0.7) and self.levadura > 0:
                self.bien_mezclado = True

    def volcar(self):
        if self.bien_salado and self.bien_mezclado:
            print('Un hermoso bollo de pan')
        if self.bien_salado and not self.bien_mezclado:
            print('Un rico pero tramboliko bollo de pan')
        if self.bien_mezclado and not self.bien_salado:
            print('Un firme y desabrido bollo de pan')
        if not self.bien_mezclado and not self.bien_salado:
            print('Un desastre')
        return Bollo(self)
            
class Bollo:
    # Amasar mínimo tres veces,
    # dejar levar mínimo 10 segundos y máximo 20
    
    def __init__(self, bowl):
        self.ingredientes = bowl
        self.amasado = 0
        
        self.levando = False
        self.comienzo_levado = 0

        self.honeando = False
        self.comienzo_horneado = 0

        self.bien_amasado = False
        self.bien_levado = False

    def amasar(self):
        self.amasado += 1
        if self.amasado > 3:
            self.bien_amasado = True

    def levar(self):
        self.levando = True
        self.comienzo_levado = time()

    def tiempo_levando(self):
        return time() - self.comienzo_levado

    def levantar(self):
        t = self.tiempo_levando()
        if t > 10 and t < 20:
            self.bien_levado = True

    def hornear(self):
        self.horneando = True
        self.comienzo_horneado = time()

    def tiempo_horneando(self):
        return time() - self.comienzo_horneado

    def sacar(self):
        t = self.tiempo_horneando()
        if t > 10 and t < 20:
            self.bien_horneado = True
            

def preparar_bowl():
    b = Bowl()
    b.agregar('harina', 1000)
    b.agregar('sal', 50)
    b.mezclar()
    b.agregar('agua', 680)
    b.agregar('aceite', 40)
    b.agregar('levadura', 20)
    b.mezclar()
    return b

