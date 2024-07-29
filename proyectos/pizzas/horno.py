class Horno:
    def __init__(self, lugares):
        self.lugares = int(lugares)
        self.cant = 0
        contenido = [] 
        for n in range(lugares):
            contenido.append(None)
        self.contenido = contenido
            
    def meter(self, comida):
        if self.cant >= self.lugares:
            print('Horno lleno')
        else:
            self.contenido[self.cant] = comida
            self.cant += 1

    def cocinar(self):
        if self.cant:
            for i in range(self.cant):
                self.contenido[i].estado = 'cocida' 
        else:
            print('El horno no posee contenido !!')
            
    def sacar(self, lugar):
        r = self.contenido[lugar]
        self.contenido[lugar] = None 
        return r

    def sacar_todo(self):
        Todo = []
        for t in range(self.cant):
            r = self.contenido[t]
            self.contenido[t] = None 
            Todo.append(r)
        return Todo
