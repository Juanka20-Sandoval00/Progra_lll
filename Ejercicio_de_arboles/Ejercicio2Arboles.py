class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def closest_value(root, target):
    closest = root.val
    
    while root:
        if abs(root.val - target) < abs(closest - target):
            closest = root.val
        
        root = root.left if target < root.val else root.right
    
    return closest

root = TreeNode(9)
root.left = TreeNode(4)
root.right = TreeNode(17)
root.left.left = TreeNode(3)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(5)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(22)
root.right.right.left = TreeNode(20)

# Encontramos el valor más cercano al objetivo en el árbol
result = closest_value(root, 16)
print(f"El valor más cercano en el árbol es: {result}")
