class TreeNode: # Definimos la clase TreeNode
 
    def __init__(self, value):    # Inicializacion de la clase
        self.val = value  # Asignaremos un valor al nodo
        self.left = None  # El valor izquierdo sera nulo 
        self.right = None  # El valor derecho sera nulo

# Función para encontrar el valor más cercano al objetivo en el arbol
def closest_value(root, target):
    closest = root.val  # Asigna el valor de la raíz como el valor más cercano inicialmente
    
    #Ciclo while mientras los nodos tengan valores en el árbol
    while root:
        # Compara la diferencia absoluta entre el valor del nodo actual y el valor que estemos asignando
        if abs(root.val - target) < abs(closest - target):
            closest = root.val  # Actualiza el valor más cercano si se encuentra uno más cercano
        
        # Avanza hacia el hijo izquierdo si el objetivo es menor que el valor del nodo actual,
        # de lo contrario, avanza hacia el hijo derecho
        root = root.left if target < root.val else root.right
    
    return closest  # Devuelve el valor más cercano

# Creamos un arbol binario con valores aleatorios
root = TreeNode(9)  # Raiz
root.left = TreeNode(4)  
root.right = TreeNode(17) 
root.left.left = TreeNode(3)  
root.left.right = TreeNode(6)  
root.left.right.left = TreeNode(5)  
root.left.right.right = TreeNode(7)  
root.right.right = TreeNode(22)  
root.right.right.left = TreeNode(20)

# Encontramos el valor más cercano al objetivo en el árbol
result = closest_value(root, 16)  # Llamada a la función para encontrar el valor más cercano a 16
print(f"El valor más cercano en el árbol es: {result}")  # Imprime el valor más cercano encontrado

