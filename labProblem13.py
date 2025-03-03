class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)

def preOrder(root):
    if root:
        print(root.data, end=" ")
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=" ")

from collections import deque

def buildTree(values):
    if not values:
        return None

    root = Node(values[0])
    queue = deque([root])
    i = 1

    while i < len(values):
        current = queue.popleft()

        if values[i] != -1:  # Assuming -1 represents a null node
            current.left = Node(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] != -1:
            current.right = Node(values[i])
            queue.append(current.right)
        i += 1

    return root

# Taking user input (space-separated values)
values = list(map(int, input("Enter space-separated values (use -1 for NULL nodes): ").split()))
root = buildTree(values)

# Printing traversals
print("In Order Traversal: ")
inOrder(root)
print("\nPre Order Traversal: ")
preOrder(root)
print("\nPost Order Traversal: ")
postOrder(root)
