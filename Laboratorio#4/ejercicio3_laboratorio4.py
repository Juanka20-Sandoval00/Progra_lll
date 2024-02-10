""" Verificación de Paréntesis Balanceados:
Escribir una función en Python que tome una cadena de paréntesis y determine si están balanceados.
Utilizar una pila para rastrear la apertura y cierre de paréntesis."""

def parentesis_balanceados(cadena):
    pila = []

    for caracter in cadena:
        if caracter == '(' or caracter == '[' or caracter == '{':
            pila.append(caracter)
        elif caracter == ')' or caracter == ']' or caracter == '}':
            if not pila or (caracter == ')' and pila.pop() != '(') or (caracter == ']' and pila.pop() != '[') or (caracter == '}' and pila.pop() != '{'):
                return False
    return not pila 

# Ejemplo para False.      
cadena1 = "())"             
cadena2 = "[(])"            
cadena3 = "{[()]})"            
print(parentesis_balanceados(cadena1))
print(parentesis_balanceados(cadena2))
print(parentesis_balanceados(cadena3))