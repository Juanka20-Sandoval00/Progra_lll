import serial
import tkinter as tk
import threading

# Configuración del puerto serial, cambia el puerto y la velocidad según tu configuración de Arduino
ser = serial.Serial('COM4', 9600)

# Función para leer datos del puerto serie en un hilo separado
def serial_reader():
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            if data:
                handle_code(data)

# Función para encender un círculo
def turn_on_circle(circle, color):
    canvas.itemconfig(circle, fill=color)

# Función para apagar un círculo
def turn_off_circle(circle):
    canvas.itemconfig(circle, fill="white")

# Función para manejar los datos recibidos del puerto serie
def handle_code(code):
    try:
        digit = int(code)
        print("Código recibido:", digit)
        # Apagar todos los círculos primero
        for circle in circles:
            turn_off_circle(circle)

        # Encender el círculo correspondiente al código recibido
        if digit == 1:
            turn_on_circle(circles[0], "green")
        elif digit == 2:
            turn_on_circle(circles[1], "blue")
        elif digit == 3:
            turn_on_circle(circles[2], "yellow")
        # Actualizar el valor de la barra de potenciómetro
        update_bar_graph(digit)
    except ValueError:
        print("Mensaje desde Arduino:", code)

# Función para actualizar la barra de potenciómetro
def update_bar_graph(value):
    # Normalizar el valor para que esté en el rango de 0 a 1 (Tkinter no acepta valores fuera de este rango)
    normalized_value = value / 1023
    # Calcular las coordenadas de la barra
    x0 = 50
    y0 = 400
    x1 = 50 + normalized_value * 500  # El valor máximo es 1023, por lo que 500 corresponde a aproximadamente la mitad del rango horizontal
    y1 = 450
    # Calcular el color en función del valor del potenciómetro
    color = '#%02x%02x%02x' % (int(255 - (normalized_value * 255)), int(normalized_value * 255), 0)

    # Actualizar las coordenadas y el color de la barra
    canvas.coords(bar, x0, y0, x1, y1)
    canvas.itemconfig(bar, fill=color)


# Configuración de la ventana de Tkinter
root = tk.Tk()
root.title("Botón Controlador")
root.geometry("800x600")

# Configuración de la gráfica de barras
canvas = tk.Canvas(root, width=600, height=500, bg='white')
canvas.pack()
bar = canvas.create_rectangle(50, 400, 50, 450, fill='green')  # Rectángulo que representa la barra de potenciómetro

circles = []
for i in range(3):
    circle = canvas.create_oval(50 + i * 70, 150, 100 + i * 70, 200, outline="black", width=2)
    canvas.create_text(75 + i * 70, 175, text=str(i+1), font=("Arial", 12))
    circles.append(circle)

title_text = tk.Label(root, text="Laboratorio #3")
title_text.place(x=350, y=25)

# Texto "Botones" encima del botón
button_text = tk.Label(root, text="Botones")
button_text.place(x=375, y=100)

# Texto "Potenciómetro" encima de la barra
pot_text = tk.Label(root, text="Potenciómetro")
pot_text.place(x=350, y=370)

# Crear y ejecutar el hilo para leer datos del puerto serie
serial_thread = threading.Thread(target=serial_reader)
serial_thread.daemon = True
serial_thread.start()

# Ejecutar la aplicación Tkinter
root.mainloop()