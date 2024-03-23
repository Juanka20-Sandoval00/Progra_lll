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
#Codigo de ARDUINO
"""void setup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);

  pinMode(10, INPUT_PULLUP);
  pinMode(11, INPUT_PULLUP);
  pinMode(12, INPUT_PULLUP);
  pinMode(13, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char estadoMonitor = Serial.read();
    if (estadoMonitor == 'A') {
      digitalWrite(2, HIGH);
      digitalWrite(3, HIGH);
      Serial.println("Grupo Led A Encendidos");
    } else if (estadoMonitor == 'B') {
      digitalWrite(4, HIGH);
      digitalWrite(5, HIGH);
      Serial.println("Grupo Led B Encendidos");
    } else if (estadoMonitor == 'C') {
      digitalWrite(6, HIGH);
      digitalWrite(7, HIGH);
      Serial.println("Grupo Led C Encendidos");
    } else if (estadoMonitor == 'D') {
      digitalWrite(8, HIGH);
      digitalWrite(9, HIGH);
      Serial.println("Grupo Led D Encendidos");
    } else if (estadoMonitor == 'E') {
      digitalWrite(2, LOW);
      digitalWrite(3, LOW);
      Serial.println("Grupo Led A Apagados");
    } else if (estadoMonitor == 'F') {
      digitalWrite(4, LOW);
      digitalWrite(5, LOW);
      Serial.println("Grupo Led B Apagados");
    } else if (estadoMonitor == 'G') {
      digitalWrite(6, LOW);
      digitalWrite(7, LOW);
      Serial.println("Grupo Led C Apagados");
    } else if (estadoMonitor == 'H') {
      digitalWrite(8, LOW);
      digitalWrite(9, LOW);
      Serial.println("Grupo Led D Apagados");
    }
  } else if (digitalRead(10) == LOW) {
    Serial.write('A');
    delay(100);
  } else if (digitalRead(11) == LOW) {
    Serial.write('B');
    delay(100);
  } else if (digitalRead(12) == LOW) {
    Serial.write('C');
    delay(100);
  } else if (digitalRead(13) == LOW) {
    Serial.write('D');
    delay(100);
  } 
}"""


