dolares = float(input("Ingresa la cantidad de dólares a convertir: "))

tasa_cambio = float(input("Ingresa la tasa de cambio actual: "))

def convertir_dolares_a_quetzales(dolares, tasa_cambio):
    quetzales = dolares * tasa_cambio
    return quetzales

quetzales = convertir_dolares_a_quetzales(dolares, tasa_cambio)


print(f"{dolares} dólares equivalen a {quetzales} quetzales.")
