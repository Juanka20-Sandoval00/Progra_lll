import serial
import tkinter as tk
from tkinter import messagebox

# Configuración de la conexión serial
ser = serial.Serial('COM4', 9600)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Control de Motores")
root.configure(bg='#1f1f2e')

# Dimensiones de la ventana
ancho_ventana = 400
alto_ventana = 300
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()
x_pos = (ancho_pantalla - ancho_ventana) // 2
y_pos = (alto_pantalla - alto_ventana) // 2
root.geometry(f'{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}')

# Estilo de fuente
font_title = ("Helvetica", 18, "bold")
font_text = ("Helvetica", 12)
font_button = ("Helvetica", 12, "bold")

# Colores
bg_color = '#1f1f2e'
fg_color = '#ffffff'
button_bg = '#4CAF50'
button_fg = '#ffffff'
button_hover_bg = '#45a049'

# Función para enviar comandos al puerto serial
def enviar_comando(comando):
    ser.write(comando.encode())

def boton_presionado(comando):
    enviar_comando(comando)
    if comando == '1':
        print("El motor Stepper está funcionando.")
        messagebox.showinfo("Stepper", "El motor Stepper ha sido iniciado.")
    elif comando == '2':
        print("El motor Servo está funcionando.")
        messagebox.showinfo("Servo", "El motor Servo ha sido iniciado.")

# Estilo del botón al pasar el ratón
def on_enter(e, button):
    button['background'] = button_hover_bg

def on_leave(e, button):
    button['background'] = button_bg

# Etiqueta de título
titulo_label = tk.Label(root, text="Control de Motores", bg=bg_color, fg=fg_color, font=font_title)
titulo_label.pack(pady=20)

# Mensaje de bienvenida
mensaje_label = tk.Label(root, text="Selecciona una opción:", bg=bg_color, fg=fg_color, font=font_text)
mensaje_label.pack(pady=10)

# Frame para los botones
frame_botones = tk.Frame(root, bg=bg_color)
frame_botones.pack(pady=20)

# Botón para iniciar el Stepper
botonStepper = tk.Button(frame_botones, text="Iniciar Stepper", command=lambda: boton_presionado('1'), bg=button_bg, fg=button_fg, font=font_button, width=15)
botonStepper.pack(side=tk.LEFT, padx=20)
botonStepper.bind("<Enter>", lambda e: on_enter(e, botonStepper))
botonStepper.bind("<Leave>", lambda e: on_leave(e, botonStepper))

# Botón para iniciar el Servo
botonServo = tk.Button(frame_botones, text="Iniciar Servo", command=lambda: boton_presionado('2'), bg=button_bg, fg=button_fg, font=font_button, width=15)
botonServo.pack(side=tk.LEFT, padx=20)
botonServo.bind("<Enter>", lambda e: on_enter(e, botonServo))
botonServo.bind("<Leave>", lambda e: on_leave(e, botonServo))

# Ejecución del bucle principal de la ventana
root.mainloop()
