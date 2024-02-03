# Ejercicio #5
""" Clases y Métodos:
Crea una clase llamada "Estudiante" con atributos como nombre, edad y calificación. 
Implementa un método en la clase para verificar si el estudiante ha aprobado o no
(calificación mayor o igual a 60)."""""
class Estudiante:

    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def ha_aprobado(self):
        return self.calificacion >= 60
nombre = input("Ingrese el nombre del estudiante. ")
edad = int(input("Ingrese la edad del estudiante. "))
calificacion = float(input("Ingrese la calificacion que ha obtenido el estudiante. "))

estudiante1 = Estudiante(nombre, edad, calificacion)

if estudiante1.ha_aprobado():
    print(f"{estudiante1.nombre} ha aprobado.")
else:
    print(f"{estudiante1.nombre} no ha aprobado.")

