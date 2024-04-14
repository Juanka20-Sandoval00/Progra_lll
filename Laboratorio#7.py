import serial
import tkinter as tk
import threading

# Configuración del puerto serial, cambia el puerto y la velocidad según tu configuración de Arduino
puerto_serial = serial.Serial('COM4', 9600)

# Función para leer datos del puerto serie en un hilo separado
def leer_puerto_serial():
    while True:
        if puerto_serial.in_waiting > 0:
            data = puerto_serial.readline().decode().strip()
            if data:
                manejar_codigo(data)

# Función para encender un círculo
def encender_circulo(circulo, color):
    canvas.itemconfig(circulo, fill=color, width=4)  # Aumentamos el grosor del borde del círculo

# Función para apagar un círculo
def apagar_circulo(circulo):
    canvas.itemconfig(circulo, fill="white", width=2)  # Restauramos el grosor del borde del círculo a su valor original

# Función para manejar los datos recibidos del puerto serie
def manejar_codigo(codigo):
    try:
        digito = int(codigo)
        print("Código recibido:", digito)
        # Apagar todos los círculos primero
        for circulo in circulos:
            apagar_circulo(circulo)

        # Encender el círculo correspondiente al código recibido
        if digito == 1:
            encender_circulo(circulos[0], "#00FF00")  # Verde
        elif digito == 2:
            encender_circulo(circulos[1], "#FFFF00")  # Amarillo
        elif digito == 3:
            encender_circulo(circulos[2], "#FF0000")  # Rojo
        # Actualizar el valor de la barra de potenciómetro
        actualizar_grafico_barra(digito)
    except ValueError:
        print("Mensaje desde Arduino:", codigo)

# Función para actualizar la barra de potenciómetro
def actualizar_grafico_barra(valor):
    # Normalizar el valor para que esté en el rango de 0 a 1 (Tkinter no acepta valores fuera de este rango)
    valor_normalizado = valor / 1023
    # Calcular las coordenadas de la barra
    x0 = 675
    y0 = 450 - valor_normalizado * 300  # Disminuimos la altura de la barra
    x1 = 725
    y1 = 450
    # Establecer el color de la barra
    color = "#00FF00"  # Verde

    # Actualizar las coordenadas y el color de la barra
    canvas.coords(barra, x0, y0, x1, y1)
    canvas.itemconfig(barra, fill=color)

# Función para enviar comando al Arduino
def enviar_comando(orden):
    puerto_serial.write(orden.encode())

# Configuración de la ventana de Tkinter
raiz = tk.Tk()
raiz.title("Botón Controlador")
raiz.geometry("900x700")

# Configuración de la gráfica de barras
canvas = tk.Canvas(raiz, width=800, height=600, bg='white')
canvas.pack()
barra = canvas.create_rectangle(675, 50, 725, 350, fill='#00FF00')  # Rectángulo que representa la barra de potenciómetro, verde

circulos = []
for i in range(3):
    circulo = canvas.create_oval(50 + i * 70, 150, 100 + i * 70, 200, outline="black", width=2, fill="white")  # Círculos blancos con borde negro
    canvas.create_text(75 + i * 70, 175, text=str(i+1), font=("Arial", 12))
    circulos.append(circulo)

# Función para InOrden
def in_orden():
    enviar_comando("1")

# Función para PostOrden
def post_orden():
    enviar_comando("2")

# Función para PreOrden
def pre_orden():
    enviar_comando("3")

# Texto "Potenciómetro" encima de la barra
texto_pot = tk.Label(raiz, text="Potenciómetro", font=("Arial", 14, "bold"))  # Fuente más grande y en negrita
texto_pot.place(x=680, y=470)

# Crear y ejecutar el hilo para leer datos del puerto serie
hilo_serial = threading.Thread(target=leer_puerto_serial)
hilo_serial.daemon = True
hilo_serial.start()

# Ejecutar la aplicación Tkinter
raiz.mainloop()
