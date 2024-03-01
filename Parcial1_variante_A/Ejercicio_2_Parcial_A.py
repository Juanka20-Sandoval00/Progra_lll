""" 2. Define una función llamada inverso_palabra que reciba una cadena como
parámetro y devuelva la cadena invertida. Por ejemplo, si la entrada es python, la salida deberí
a ser nohtyp. """

def inverso_palabra(cadena):
    cadena_invertida = " "
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida

print(inverso_palabra("Guatemala"))
