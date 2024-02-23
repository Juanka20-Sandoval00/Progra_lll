"""Implementación de una Pila (Stack):
Implementar una pila utilizando una lista en Python.
Crear funciones para realizar las operaciones básicas de una pila: push (añadir elemento), pop (eliminar 
elemento) y peek (ver el elemento superior sin eliminarlo).
Escribir un programa que utilice esta pila para invertir el orden de una lista dada.
Implementación de una Cola (Queue):"""

class Pila:
    def __init__(self):
        self.elementos = []  # Inicializa una lista vacía para almacenar los elementos de la pila
    
    def esta_vacia(self):
        return len(self.elementos) == 0  # Devuelve True si la pila está vacía, False en caso contrario
    
    def agregar(self, elemento):
        self.elementos.append(elemento)  # Agrega un elemento a la parte superior de la pila
    
    def sacar(self):
        if not self.esta_vacia():  # Verifica si la pila no está vacía
            return self.elementos.pop()  # Elimina y devuelve el elemento en la parte superior de la pila
        else:
            return "La pila está vacía"  # Devuelve un mensaje si la pila está vacía
    
    def ver_tope(self):
        if not self.esta_vacia():  # Verifica si la pila no está vacía
            return self.elementos[-1]  # Devuelve el elemento en la parte superior de la pila sin sacarlo
        else:
            return "La pila está vacía"  # Devuelve un mensaje si la pila está vacía
    
    def lista_invertida(self, lista):
        pila = Pila()  # Crea una nueva pila

        for elemento in lista:
            pila.agregar(elemento)  # Agrega cada elemento de la lista original a la pila

        lista_invertida = []
        while not pila.esta_vacia():
            lista_invertida.append(pila.sacar())  # Sacar los elementos de la pila y agregarlos a la lista invertida

        return lista_invertida  # Devuelve la lista invertida

pila = Pila()  # Crea una instancia de la clase Pila
lista_original = [1,2,3,4,5,6]  # Define una lista original
print("La lista original es:", lista_original)  # Imprime la lista original
print("La lista invertida es:", pila.lista_invertida(lista_original))  # Imprime la lista original e invertida

