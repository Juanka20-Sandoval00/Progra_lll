"""Implementación de una Pila (Stack):
Implementar una pila utilizando una lista en Python.
Crear funciones para realizar las operaciones básicas de una pila: push (añadir elemento), pop (eliminar 
elemento) y peek (ver el elemento superior sin eliminarlo).
Escribir un programa que utilice esta pila para invertir el orden de una lista dada.
Implementación de una Cola (Queue):"""

class Pila:
    def __init__(self):
        self.elementos = [] 
    
    def esta_vacia(self):
        return len(self.elementos) == 0  
    
    def agregar(self, elemento):
        self.elementos.append(elemento) 
    
    def sacar(self):
        if not self.esta_vacia():
            return self.elementos.pop() 
        else:
            return "La pila está vacía" 
    
    def ver_tope(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        else:
            return "La pila está vacía"
    
    def lista_invertida(self, lista):
        pila = Pila()

        for elemento in lista:
            pila.agregar(elemento)

        lista_invertida = []
        while not pila.esta_vacia():
            lista_invertida.append(pila.sacar())

        return lista_invertida

pila = Pila()
lista_original = [1,2,3,4,5,6]
print("La lista original es:", lista_original)
print("La lista invertida es:", pila.lista_invertida(lista_original))
