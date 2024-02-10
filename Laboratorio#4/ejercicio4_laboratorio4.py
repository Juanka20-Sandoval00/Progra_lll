""" Implementación de una Cola con Dos Pilas:
Desarrollar una clase ColaConPilas que utilice dos pilas para simular el comportamiento de una cola.
Implementar las operaciones enqueue y dequeue utilizando las operaciones de pilas."""
class ColaConPilas:
    
    def __init__(self):
        self.pilaEntrada = [] 
        self.pilaSalida = []  

    def encolar(self, elemento):
        self.pilaEntrada.append(elemento) 
    
    def desencolar(self):
        if not self.pilaSalida:  
            while self.pilaEntrada:  
                self.pilaSalida.append(self.pilaEntrada.pop())
        if self.pilaSalida: 
            return self.pilaSalida.pop()
        else:  
            return None

cola = ColaConPilas() 

cola.encolar(10)
cola.encolar(20)
cola.encolar(90)
cola.encolar(50)
cola.encolar(70)
cola.encolar(5)
cola.encolar(80)

print(cola.desencolar())  
print(cola.desencolar())  
print(cola.desencolar())  
print(cola.desencolar()) 
print(cola.desencolar()) 
print(cola.desencolar()) 
print(cola.desencolar()) 
print(cola.desencolar()) 

