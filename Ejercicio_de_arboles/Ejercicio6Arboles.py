class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def kth_smallest(root, k):
    stack = []
    
    while True:
        while root:
            stack.append(root)
            root = root.left
        
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right

# Creamos un árbol de búsqueda binaria de ejemplo
root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(14)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.right.right = TreeNode(24)
root.right.right.left = TreeNode(22)

# Encontramos el k-ésimo elemento más pequeño
result = kth_smallest(root, 2)
resultado = kth_smallest(root, 3)
print(f"El k-ésimo elemento más pequeño es: {result}")
print(f"El k-ésimo elemento más pequeño es: {resultado}")
