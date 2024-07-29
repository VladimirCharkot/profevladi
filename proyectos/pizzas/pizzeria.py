from random import choice

class Pizzeria:
  def __init__(self, nombre_pizzeria, h, gente = []):
    self.cola = gente
    self.horno = h
    self.pizzeria_nombre = nombre_pizzeria

  def atender(self, menu):
    if len(self.cola) > 0:
      atendido = self.cola[0]
      self.cola.remove(atendido)
      p = choice(menu)
      atendido.pagar(3000)
      atendido.pizza = p
      print(f'{atendido.nombre} fue atendido')
    else:
       print('No hay clientes')