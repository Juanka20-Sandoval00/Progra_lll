horas = float(input("Ingrese la hora "))
minutos = float(input("Ingrese los minutos "))
segundos = float(input("Ingrese los segundos "))

def segundos_del_dia(horas, minutos, segundos):
    segundos_totales = (horas * 3600) + (minutos * 60) + segundos
    return segundos_totales

segundos_totales = segundos_del_dia(horas, minutos, segundos)
    
print(f"{horas} Horas, {minutos} Minutos, {segundos} Segundos, equivalen a {segundos_totales} segundos transcurridos ")