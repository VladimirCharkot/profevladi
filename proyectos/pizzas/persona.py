
class Persona:
  def __init__(self, nombre, dinero):
    self.nombre = nombre
    self.dinero = dinero
    self.pizza = None
    self.hambriento = True
  
  def comer(self):
    if self.pizza:
      if not self.pizza.estado == 'cruda':
        self.hambriento = False
        print("Aaaahh... delicioso")
      else:
        print("Wákala pizza cruda puaj")
      self.pizza = None
    else:
      print("Si tan solo tuviera una pizza!!")

  def pagar(self, monto):
    self.dinero -= monto
    print(f'{self.nombre} pagó ${monto} y ahora tiene ${self.dinero}')

  def entrar(self, pizzeria):
    pizzeria.cola.append(self)