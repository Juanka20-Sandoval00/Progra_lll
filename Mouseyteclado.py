import tkinter as tk

def mouse_move(event):
    x = event.x
    y = event.y
    label.config(text=f'Posición del ratón: x={x}, y={y}')

def key_press(event):
    key = event.keysym
    label.config(text=f'Tecla presionada: {key}')

def key_release(event):
    label.config(text='')

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Captura de Eventos de Ratón y Teclado")

# Crear una etiqueta para mostrar la posición del ratón y la tecla presionada
label = tk.Label(root, text="")
label.pack()

# Asociar el evento de movimiento del ratón con la función mouse_move
root.bind('<Motion>', mouse_move)

# Asociar el evento de presionar una tecla con la función key_press
root.bind('<KeyPress>', key_press)

# Asociar el evento de soltar una tecla con la función key_release
root.bind('<KeyRelease>', key_release)

# Ejecutar el bucle principal
root.mainloop()