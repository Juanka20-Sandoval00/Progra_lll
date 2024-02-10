'''
Definir funciones para las operaciones básicas de una cola: enqueue (añadir elemento), dequeue (eliminar
elemento) y front (ver el primer elemento sin eliminarlo).
Escribir un programa que simule el proceso de atención en una fila, donde los elementos son atendidos en
el orden en que llegan.
'''
class Cola:
    def __init__(self):
        self.personas = []
    
    def agregar(self, persona):
        self.personas.append(persona)
    
    def sacar(self):
        if not self.cola_vacia():
            return self.personas.pop(0) 
        else:
            return None 
    
    def frente(self):
        if not self.cola_vacia():
            return self.personas[0]
        else:
            return None
    
    def cola_vacia(self):
        return len(self.personas) == 0

def atencion_fila(personas):
    fila = Cola()

    for persona in personas:
        fila.agregar(persona)

    print("Proceso de atención en la fila:")
    atendiendo_a = 1
    while not fila.cola_vacia():

        siguiente_persona = fila.sacar()
        print(f"Atendiendo: {siguiente_persona}")
        atendiendo_a += 1

    if fila.cola_vacia():
        print("¡Todas las personas han sido atendidas exitosamente!")

personas = ["Persona 1", "Persona 2", "Persona 3", "Persona 4", "Persona 5"]
atencion_fila(personas)
