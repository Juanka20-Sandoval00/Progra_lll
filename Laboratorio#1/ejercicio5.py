variable_usuario = input("Ingrese una variable: ")

def obtener_tipo_dato(variable):
    return type(variable).__name__

try:
    variable_convertida = int(variable_usuario)
    tipo = "int"
except ValueError:
    try:
        variable_convertida = float(variable_usuario)
        tipo = "float"
    except ValueError:
        variable_convertida = variable_usuario
        tipo = "str"

print(f"La variable es de tipo {tipo}")
