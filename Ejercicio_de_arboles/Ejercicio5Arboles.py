class TreeNode(object): # Definición de la clase TreeNode
   def __init__(self, x):     # Constructor de la clase TreeNode
        self.val = x    # Inicializa el valor del nodo con x
        self.left = None # Inicializa el nodo izquierdo como Nulo
        self.right = None   # Inicializa el nodo derecho como Nulo

def array_to_bst(array_nums): # Función para convertir un arreglo en un árbol de búsqueda binaria (BST)
    if not array_nums:  # Si el arreglo está vacío, retorna None
        return None
    mid_num = len(array_nums) // 2  # Calcula el índice medio del arreglo
    node = TreeNode(array_nums[mid_num])  # Crea un nodo con el valor en la posición media del arreglo
    # Asigna el nodo izquierdo llamando recursivamente a la función con la mitad izquierda del arreglo
    node.left = array_to_bst(array_nums[:mid_num])
    # Asigna el nodo derecho llamando recursivamente a la función con la mitad derecha del arreglo
    node.right = array_to_bst(array_nums[mid_num + 1:])
    # Retorna el nodo creado
    return node

def preOrder(node): # Función para recorrer el árbol en preorden e imprimir los valores de los nodos
    if not node:  # Si el nodo es nulo, retorna
        return
    print(node.val) # Imprime el valor del nodo
    preOrder(node.left)  # Llama recursivamente a la función para el nodo izquierdo
    preOrder(node.right)  # Llama recursivamente a la función para el nodo derecho

array_nums = [1,2,3,4,5,6,7]    # Arreglo de números
print(f"Array original: {array_nums}")  # Imprime el arreglo original
result = array_to_bst(array_nums) # Convierte el arreglo en un BST (árbol de búsqueda binaria)
print(f"Arreglo de tamaño balanceado BST: {preOrder(result)}")
