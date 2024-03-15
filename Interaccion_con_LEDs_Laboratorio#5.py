import serial
from serial.tools.list_ports import comports
from time import sleep
from tkinter import *

estadoLed = 0

def setup():
    global puerto
    puerto = serial.Serial(comports()[0].device, 9600)
    sleep(2)  # Espera a que se establezca la conexión

def draw():
    global estadoLed
    if estadoLed == 0:
        canvas.delete("all")
        canvas.create_oval(width/2 - 50, height/2 - 50, width/2 + 50, height/2 + 50, fill="greenyellow")
    elif estadoLed == 1:
        canvas.delete("all")
        canvas.create_oval(width/2 - 50, height/2 - 50, width/2 + 50, height/2 + 50, fill="red")

def mousePressed(event):
    global estadoLed
    if estadoLed == 0:
        estadoLed = 1
        puerto.write(b'1')
    else:
        estadoLed = 0
        puerto.write(b'0')
    draw()  # Actualizar el color del botón después de cambiar el estado de la LED

# Configuración de la ventana
root = Tk()
width = 200
height = 200
root.geometry(f"{width}x{height}")
canvas = Canvas(root, width=width, height=height)
canvas.pack()

setup()

canvas.bind("<Button-1>", mousePressed)

draw()  # Dibujar el botón inicialmente

root.mainloop()  # Mantener la aplicación en funcionamiento
