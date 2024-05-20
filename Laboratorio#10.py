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

"""" Codigo de Arduino 
#include <Stepper.h>
#include <Servo.h>

// Definir el número de pasos para el motor paso a paso
const int STEPS_PER_REVOLUTION = 2048;

// Crear un objeto de la clase Stepper para el motor paso a paso
Stepper stepperMotor(STEPS_PER_REVOLUTION, 8, 10, 9, 11);

// Crear un objeto de la clase Servo para el servo motor
Servo servoMotor;

void setup() {
  // Conectar el servo motor al pin digital 2
  servoMotor.attach(2);

  // Establecer la velocidad del motor paso a paso en 10 RPM
  stepperMotor.setSpeed(10);

  // Iniciar la comunicación serial a 9600 baudios
  Serial.begin(9600);

  // Mensaje inicial en el monitor serial
  Serial.println("Sistema de control de motores iniciado.");
  Serial.println("Ingrese '1' para mover el motor paso a paso.");
  Serial.println("Ingrese '2' para mover el servo motor.");
}

void loop() {
  // Verificar si hay datos disponibles en el buffer serial
  if (Serial.available() > 0) {
    // Leer un carácter del buffer serial
    char command = Serial.read();

    // Ejecutar la función correspondiente según el comando recibido
    if (command == '1') {
      controlStepperMotor();
    } else if (command == '2') {
      controlServoMotor();
    }
  }
}

void controlStepperMotor() {
  Serial.println("Inicio del movimiento del motor paso a paso.");

  // Mover el motor paso a paso una vuelta completa en una dirección
  stepperMotor.step(STEPS_PER_REVOLUTION);
  delay(500); // Esperar medio segundo

  // Mover el motor paso a paso una vuelta completa en la dirección opuesta
  stepperMotor.step(-STEPS_PER_REVOLUTION);
  delay(500); // Esperar medio segundo

  Serial.println("Fin del movimiento del motor paso a paso.");
}

void controlServoMotor() {
  Serial.println("Inicio del movimiento del servo motor.");

  // Mover el servo motor a varias posiciones con pausas intermedias
  moveServoToPosition(0);   // Mover a 0 grados
  delay(500);

  moveServoToPosition(90);  // Mover a 90 grados
  delay(500);

  moveServoToPosition(180); // Mover a 180 grados
  delay(500);

  moveServoToPosition(90);  // Volver a 90 grados
  delay(500);

  moveServoToPosition(0);   // Volver a 0 grados
  delay(500);

  Serial.println("Fin del movimiento del servo motor.");
}

void moveServoToPosition(int position) {
  // Mover el servo motor a la posición especificada
  servoMotor.write(position);
  Serial.print("Servo movido a ");
  Serial.print(position);
  Serial.println(" grados.");
}
"""