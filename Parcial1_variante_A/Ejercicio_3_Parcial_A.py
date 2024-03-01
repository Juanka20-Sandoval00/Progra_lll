"""3. Escribe un programa que pida al usuario una lista de números y luego imprima la suma de 
los números pares en la lista. """

lista = []
suma = 0

print("Ingrese una lista de números separados por comas")
lista = input().split(",")

for i in lista:
    if int(i) % 2 == 0:
        suma += int(i)
print (suma)

