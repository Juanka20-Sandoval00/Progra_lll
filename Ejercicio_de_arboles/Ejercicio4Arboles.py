class TreeNode(object): # Definición de la clase TreeNode que representa un nodo en un árbol binario
    
    def __init__(self, x):  # Método constructor de la clase TreeNode que inicializa un nodo con un valor x
        self.val = x    # Asigna el valor x al atributo 'val' del nodo.
        self.left = None    # El valor izquierdo sera nulo 
        self.right = None   # El valor derecho sera nulo

def delete_Node(root, key): # Función para eliminar un nodo con el valor clave 'key' del árbol con raíz 'root'
    if not root:
        return root  # Si el árbol está vacío, no hay nada que eliminar
    if root.val > key:  # Si el valor en el nodo raíz es mayor que la clave, buscar en el subárbol izquierdo
        root.left = delete_Node(root.left, key)
    elif root.val < key: # Si el valor en el nodo raíz es menor que la clave, buscar en el subárbol derecho
        root.right = delete_Node(root.right, key)
    else:
        # Si el nodo raíz tiene el mismo valor que la clave
        if not root.right:
            return root.left  # Si no hay subárbol derecho, devolver el subárbol izquierdo
        if not root.left:
            return root.right  # Si no hay subárbol izquierdo, devolver el subárbol derecho
        
        # Si el nodo raíz tiene ambos subárboles
        temp_val = root.right  # Temporalmente almacenamos el subárbol derecho
        mini_val = temp_val.val  # Obtenemos el valor mínimo del subárbol derecho
        while temp_val.left:
            temp_val = temp_val.left
            mini_val = temp_val.val
        # Cambiamos el valor del nodo raíz al valor mínimo del subárbol derecho
        root.val = mini_val
        # Eliminamos el nodo con el valor mínimo del subárbol derecho
        root.right = delete_Node(root.right, root.val)
    return root

def preOrder(node):
    # Función para recorrer el árbol en preorden e imprimir los valores de los nodos
    if not node:
        return
    print(node.val)  # Imprimir el valor del nodo actual
    preOrder(node.left)  # Recorrer el subárbol izquierdo
    preOrder(node.right)  # Recorrer el subárbol derecho

# Creación del árbol con algunos nodos
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(7)

# Imprimir el árbol original en preorden
print(f"Nodo original: {preOrder(root)}")

# Eliminar un nodo específico del árbol
result = delete_Node(root, 4)

# Imprimir el árbol después de eliminar el nodo específico en preorden
print(f"Después de eliminar el nodo especifico: {preOrder(result)}")
