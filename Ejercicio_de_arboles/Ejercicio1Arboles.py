# Definimos la clase TreeNode
class TreeNode(object):
    def __init__(self, x): # Inicializacion de la clase
        self.val = x  # Asigna el valor x al atributo 'val' del nodo.
        self.left = None  # El valor izquierdo sera nulo
        self.right = None  # El valor derecho sera nulo

# Función para convertir un arreglo ordenado en un árbol binario.
def sorted_array_to_bst(nums):   
    if not nums: # Verifica si el arreglo 'nums' está vacío.
        return None  # Retorna Nulo si el arreglo está vacío esto quiere decir que no hay nodos.
    mid_val = len(nums) // 2  # Calcula el índice medio del arreglo.
    node = TreeNode(nums[mid_val])# Crea un nuevo nodo con el valor en el índice medio.
    
    # Llama recursivamente a la función para los elementos de la izquierda y los asigna como nodos hijos izquierdos.
    node.left = sorted_array_to_bst(nums[:mid_val])
    
    # Llama recursivamente a la función para los elementos de la derecha y los asigna como nodos hijos derechos.
    node.right = sorted_array_to_bst(nums[mid_val + 1:])
    return node # Retorna el nodo raíz del árbol binario creado.

# Función que recorrera el árbol en preorden e imprimir los valores de los nodos.
def preOrder(node):
    if not node:  # Verifica si el nodo actual es nulo.
        return  # Si es nulo, no hace nada y retorna.
    print(node.val) # Imprime el valor del nodo actual.
    
    # Llama recursivamente a la función para el hijo izquierdo.
    preOrder(node.left)
    
    # Llama recursivamente a la función para el hijo derecho.
    preOrder(node.right)

# Crea un árbol binario de búsqueda a partir de un arreglo ordenado.
result = sorted_array_to_bst([1,2,3,4,5,6,7])

# Realiza un recorrido en preorden del árbol creado e imprime los valores de los nodos.
preOrder(result)

