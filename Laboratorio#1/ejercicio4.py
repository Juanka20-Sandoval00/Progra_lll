import math

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

def calcular_raices(a, b, c):

    discriminante = b**2 - 4*a*c

    if discriminante > 0:
    
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2
    elif discriminante == 0:
    
        raiz = -b / (2*a)
        return raiz,
    else:
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(abs(discriminante)) / (2*a)
        raiz1 = complex(parte_real, parte_imaginaria)
        raiz2 = complex(parte_real, -parte_imaginaria)
        return raiz1, raiz2
    
raices = calcular_raices(a, b, c)

print("Las raíces son:", raices)
