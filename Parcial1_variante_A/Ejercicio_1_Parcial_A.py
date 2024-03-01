"""1. Escribe una función en Python que reciba una lista como parámetro y devuelva la suma de todos los 
elementos de la lista. """

def suma_lista(lista):
        suma = 0
        for elemento in lista:
            suma += elemento
        return suma

lista = [1,2,3,4,5,6,7,8,9,10]

print(suma_lista(lista))




