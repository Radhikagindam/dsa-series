class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createbst(root, val):
    if root is None:
        return TreeNode(val)
    else:
        if val < root.data:
            root.left = createbst(root.left, val)
        elif val > root.data:
            root.right = createbst(root.right, val)
    return root

def find_min(root):
    while root.left is not None:
        root = root.left
    return root

def delete_node(root, key):
    if root is None:
        return None
    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        # Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # Node with two children
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)
    return root


def update(root, old_val, new_val):
    root = delete_node(root, old_val)
    root = createbst(root, new_val)
    return root

def preorder(root):
    if root is None:
        return 
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def create_bst_from_array(arr):
    root = None
    for val in arr:
        root = createbst(root, val)
    return root


arr = [8, 3, 10, 1, 6, 14, 6, 4, 7]

root = create_bst_from_array(arr)


print("Preorder before deletion:")
preorder(root)
print()


root = delete_node(root, 6)


print("Inorder after deletion:")
inorder(root)
print()


root = update(root, 4, 9)


print("Inorder after update:")
inorder(root)
print()

print("Preorder after deletion and update:")
preorder(root)
print()
