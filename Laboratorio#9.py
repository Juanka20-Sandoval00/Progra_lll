import serial
import time

# Establece la comunicación con Arduino
arduino_port = 'COM4'  # Cambia esto al puerto COM correcto en Windows
arduino_baudrate = 9600
arduino = serial.Serial(arduino_port, arduino_baudrate, timeout=1)

def main():
    while True:
        # Espera a que Arduino envíe datos
        arduino_data = arduino.readline().decode().strip()
        if arduino_data:
            print("Arduino dice:", arduino_data)

if __name__ == "__main__":
    main()
