class TreeNode: # Definición de la clase TreeNode
    def __init__(self, value): # Método para inicializar un nodo con un valor específico
        self.val = value  # Valor almacenado en el nodo
        self.left = None  # Inicializa el nodo izquierdo como Nulo
        self.right = None # Inicializa el nodo derecho como Nulo

def kth_smallest(root, k): # Función para encontrar el k-ésimo elemento más pequeño en un árbol binario de búsqueda
    stack = []  # Creamos una pila para seguir los nodos que visitamos
    
    while True:  # Entramos en un bucle infinito
        while root:  # Mientras haya nodos a la izquierda
            stack.append(root)  # Añadimos el nodo actual a la pila
            root = root.left  # Avanzamos al siguiente nodo a la izquierda
        
        root = stack.pop()  # Sacamos el último nodo visitado de la pila
        k -= 1  # Decrementamos el valor de k
        if k == 0:  # Si k alcanza cero, hemos encontrado el k-ésimo elemento más pequeño
            return root.val  # Devolvemos el valor del nodo actual
        root = root.right  # Avanzamos al nodo a la derecha

root = TreeNode(8) 
root.left = TreeNode(5)  
root.right = TreeNode(14) 
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)  
root.right.right = TreeNode(24)  
root.right.right.left = TreeNode(22)  

# Encontramos el k-ésimo elemento más pequeño
result = kth_smallest(root, 7)  # Encontramos el segundo elemento más pequeño
resultado = kth_smallest(root, 3)  # Encontramos el tercer elemento más pequeño
print(f"El k-ésimo elemento más pequeño es: {result}")
print(f"El k-ésimo elemento más pequeño es: {resultado}")
