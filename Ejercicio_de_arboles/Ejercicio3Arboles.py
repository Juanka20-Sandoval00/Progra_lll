 # Se define la clase y esta va a representa un nodo en un árbol.
class TreeNode(object):
   
    def __init__(self, x):  # Inicializacion de la clase
        self.val = x    # Se asigna el valor 'x' al atributo 'val' del nodo.
        self.left = None    # El valor izquierdo sera nulo
        self.right = None   # El valor derecho sera nulo

def is_BST(root): # Se define la función is_BST que verifica el árbol binario
    stack = []  # Se inicializa una pila vacía para almacenar los nodos del árbol.
    prev = None #Se inicializa una variable prev para almacenar el nodo previo visitado en el recorrido del árbol.
    
    while root or stack:
        # Mientras todavía haya nodos en el árbol sin visitar o todavía haya nodos en la pila:
        while root:
            # Mientras haya nodos en el árbol que no se han visitado:
            stack.append(root)
            # Se agrega el nodo actual a la pila.
            root = root.left
            # Se avanza al hijo izquierdo del nodo actual.

        root = stack.pop()
        # Cuando no haya más nodos izquierdos que visitar, se extrae el nodo superior de la pila.
        if prev and root.val <= prev.val:
            # Si hay un nodo previo visitado y el valor del nodo actual es menor o igual al valor del nodo previo:
            return False
            # Se devuelve False, indicando que el árbol no es un árbol binario de búsqueda.
        prev = root
        # Se actualiza el nodo previo al nodo actual.
        root = root.right
        # Se avanza al hijo derecho del nodo actual.

    return True
    # Si se completa el bucle sin encontrar ninguna inconsistencia, se devuelve True, indicando que el árbol es un árbol binario de búsqueda.

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

result = is_BST(root)   # Se llama a la función is_BST con el árbol recién creado.

print(result) # Se imprime el resultado.

# Se crea otro árbol binario:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

result = is_BST(root)
print(result)# Se imprime el resultado.


