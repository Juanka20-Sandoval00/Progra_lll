# Ejercicio #4
""" Funciones y Condicionales:
Define una función que tome dos parámetros y devuelva True si la suma de ambos es par y False si es impar."""""

def suma_de_parametros(num, num1):
    suma = num + num1
    return suma % 2 == 0

num = float(input("Ingrese el primer valor: "))
num1 = float(input("Ingrese el segundo valor: ")) 

resultado = suma_de_parametros (num, num1)

if resultado:
    print (f"La suma de {num} + {num1} es par. ")
else:
    print (f"La suma de {num} + {num1} es impar. ")
