class Persona:

    # Inicializador (acá se crea el estado y corre al instanciarse la clase)
    def __init__(self, nombre):
        # Estado (conjunto de todas las variables internas a un objeto)
        self.nombre = nombre

    # Método
    def saludar(self):
        print(f'Hola me llamo {self.nombre}')

    # Método
    def renombrar(self, nombre_nuevo):
        self.nombre = nombre_nuevo


# Herencia
class Vladi(Persona):

    def saltar(self):
        print(f'{self.nombre} salta')


vladi = Vladi('Vladi')
aleja = Persona('Aleja')
