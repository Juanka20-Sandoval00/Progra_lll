import tkinter as tk
import serial
import threading

# Inicializar la comunicación serial con Arduino
arduino = serial.Serial('COM4', 9600)  # Reemplaza 'puerto_serial_de_arduino' con el puerto correcto

# Función para procesar los datos recibidos de Arduino
def procesar_datos(datos):
    print("Datos recibidos desde Arduino:", datos.decode().strip())

# Función para enviar comandos a Arduino
def enviar_comando(comando):
    arduino.write(comando.encode())

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Dashboard")

# Estilo para los botones
estilo_boton = {
    'font': ('Arial', 14),
    'width': 10,
    'height': 2,
    'bg': 'skyblue',  # Color de fondo
    'fg': 'black',  # Color del texto
    'activebackground': 'greenyellow',  # Color de fondo cuando se presiona
    'activeforeground': 'black',  # Color del texto cuando se presiona
    'bd': 0,  # Grosor del borde
    'highlightthickness': 0,  # Grosor del resaltado
}

# Ejemplo de creación de botones con el estilo aplicado
boton_A = tk.Button(ventana, text="Botón A", command=lambda: enviar_comando('A'), **estilo_boton)
boton_A.pack(pady=5)

boton_B = tk.Button(ventana, text="Botón B", command=lambda: enviar_comando('B'), **estilo_boton)
boton_B.pack(pady=5)

boton_C = tk.Button(ventana, text="Botón C", command=lambda: enviar_comando('C'), **estilo_boton)
boton_C.pack(pady=5)

boton_D = tk.Button(ventana, text="Botón D", command=lambda: enviar_comando('D'), **estilo_boton)
boton_D.pack(pady=5)

boton_E = tk.Button(ventana, text="Botón E", command=lambda: enviar_comando('E'), **estilo_boton)
boton_E.pack(pady=5)

boton_F = tk.Button(ventana, text="Botón F", command=lambda: enviar_comando('F'), **estilo_boton)
boton_F.pack(pady=5)

boton_G = tk.Button(ventana, text="Botón G", command=lambda: enviar_comando('G'), **estilo_boton)
boton_G.pack(pady=5)

boton_H = tk.Button(ventana, text="Botón H", command=lambda: enviar_comando('H'), **estilo_boton)
boton_H.pack(pady=5)

# Bucle principal para recibir y procesar datos de Arduino
def leer_datos_desde_arduino():
    while True:
        datos = arduino.readline()
        if datos:
            procesar_datos(datos)

# Crear un hilo para leer datos de Arduino en segundo plano
thread_arduino = threading.Thread(target=leer_datos_desde_arduino)
thread_arduino.start()

# Iniciar el bucle de la interfaz de usuario
ventana.mainloop()



