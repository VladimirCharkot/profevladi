class Pizza:
    def __init__ (self, ingredientes, estado = 'cruda'):
       self.ingredientes = ingredientes
       self.estado = estado
    def status(self):
        listado = ', '.join(self.ingredientes)
        return f'Pizza de {listado} {self.estado}'
      
    def cocinar(self):
      self.estado = 'cocida'
      
    def desarmar(self):
      return self.ingredientes
      
    def __str__(self):
        return self.status()
    def __repr__(self):
        return self.status()