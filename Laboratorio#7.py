import serial  # Importa el módulo para la comunicación serial
import tkinter as tk  # Importa el módulo para la creación de interfaces gráficas
import threading  # Importa el módulo para la gestión de hilos

# Configuración del puerto serial para la comunicación con Arduino
puerto_serial = serial.Serial('COM4', 9600)

# Función para leer datos del puerto serie en un hilo separado
def leer_puerto_serial():
    while True:  # Bucle infinito para mantener la lectura constante
        if puerto_serial.in_waiting > 0:  # Verifica si hay datos disponibles en el puerto
            data = puerto_serial.readline().decode().strip()  # Lee los datos y los decodifica
            if data:  # Verifica si hay datos válidos
                manejar_codigo(data)  # Llama a la función para manejar los datos recibidos

# Función para encender un círculo en la interfaz gráfica
def encender_circulo(circulo, color):
    canvas.itemconfig(circulo, fill=color, width=4)  # Modifica el color y grosor del borde del círculo

# Función para apagar un círculo en la interfaz gráfica
def apagar_circulo(circulo):
    canvas.itemconfig(circulo, fill="white", width=2)  # Restaura el color y grosor original del borde del círculo

# Función para manejar los datos recibidos del puerto serie
def manejar_codigo(codigo):
    try:
        digito = int(codigo)  # Convierte los datos a un número entero
        print("Código recibido:", digito)  # Imprime el código recibido desde Arduino

        # Apaga todos los círculos antes de encender uno nuevo
        for circulo in circulos:
            apagar_circulo(circulo)

        # Enciende el círculo correspondiente al código recibido
        if digito == 1:
            encender_circulo(circulos[0], "green") 
        elif digito == 2:
            encender_circulo(circulos[1], "yellow")  
        elif digito == 3:
            encender_circulo(circulos[2], "red")  

        # Actualiza el valor de la barra de potenciómetro
        actualizar_grafico_barra(digito)
    except ValueError:
        print("Mensaje desde Arduino:", codigo)  # Imprime un mensaje si los datos no son un número

# Función para actualizar la barra de potenciómetro en la interfaz gráfica
def actualizar_grafico_barra(valor):
    valor_normalizado = valor / 1023  # Normaliza el valor del potenciómetro
    x0 = 675
    y0 = 450 - valor_normalizado * 300  # Calcula la posición del rectángulo de la barra
    x1 = 725
    y1 = 450
    color = "green"

    # Actualiza las coordenadas y color de la barra
    canvas.coords(barra, x0, y0, x1, y1)
    canvas.itemconfig(barra, fill=color)

# Función para enviar un comando al Arduino a través del puerto serial
def enviar_comando(orden):
    puerto_serial.write(orden.encode())

# Configuración de la ventana principal de Tkinter
raiz = tk.Tk()
raiz.title("Botón Controlador")
raiz.geometry("900x700")

# Configuración del lienzo para la interfaz gráfica
canvas = tk.Canvas(raiz, width=800, height=600, bg='white')
canvas.pack()
barra = canvas.create_rectangle(675, 50, 725, 350, fill='#00FF00')  # Barra de potenciómetro inicialmente en verde

circulos = []
for i in range(3):  # Crea tres círculos en la interfaz gráfica
    circulo = canvas.create_oval(50 + i * 70, 150, 100 + i * 70, 200, outline="black", width=2, fill="white")
    canvas.create_text(75 + i * 70, 175, text=str(i+1), font=("Arial", 12))  # Muestra el número en cada círculo
    circulos.append(circulo)  # Agrega el identificador del círculo a la lista

# Funciones para enviar comandos al Arduino según el orden de recorrido del árbol binario
def in_orden():
    enviar_comando("1")

def post_orden():
    enviar_comando("2")

def pre_orden():
    enviar_comando("3")

# Texto "Potenciómetro" encima de la barra
texto_pot = tk.Label(raiz, text="Potenciómetro", font=("Arial", 14, "bold"))
texto_pot.place(x=680, y=470)

# Crea y ejecuta un hilo para leer datos del puerto serie en segundo plano
hilo_serial = threading.Thread(target=leer_puerto_serial)
hilo_serial.daemon = True
hilo_serial.start()

# Ejecuta la aplicación Tkinter
raiz.mainloop()
