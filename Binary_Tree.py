# Travseral algo in treess preorder(root-left-right),Inorder(left-root-right),postorder(left-right-root),level order

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def create_bt(arr, i, n):
    if i > n:
        return None
    root = TreeNode(arr[i - 1])
    root.left = create_bt(arr, 2 * i, n)
    root.right = create_bt(arr, 2 * i + 1, n)
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


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


def levelorder(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.data)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


def search_levelorder(root, ele):
    if root is None:
        return False
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.data == ele:
            return True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False


def search_preorder(root, ele):
    if root is None:
        return False
    if root.data == ele:
        return True
    return search_preorder(root.left, ele) or search_preorder(root.right, ele)

def search_inorder(root, ele):
    if root is None:
        return False
    if search_inorder(root.left, ele):
        return True
    if root.data == ele:
        return True
    return search_inorder(root.right, ele)

# Search element in postorder
def search_postorder(root, ele):
    if root is None:
        return False
    if search_postorder(root.left, ele):
        return True
    if search_postorder(root.right, ele):
        return True
    if root.data == ele:
        return True
    return False

# Example to test the functions
arr = [1, 2, 3, 4, 5, 6, 7, 8]
root = create_bt(arr, 1, len(arr))

# Printing traversals
print("Preorder Traversal:")
preorder(root)
print("\n")

print("Inorder Traversal:")
inorder(root)
print("\n")

print("Postorder Traversal:")
postorder(root)
print("\n")

print("Levelorder Traversal:")
print(levelorder(root))
print("\n")


print("Search in Levelorder (7):", search_levelorder(root, 7))
print("Search in Preorder (7):", search_preorder(root, 7))
print("Search in Inorder (7):", search_inorder(root, 7))
print("Search in Postorder (7):", search_postorder(root, 7))
