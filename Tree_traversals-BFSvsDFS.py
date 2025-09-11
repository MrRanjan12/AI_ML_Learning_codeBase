"""
DFS (Defth-First Search)
Go as deep as possible before backtracking.
Types (on trees):
Inorder(Left -> Root -> Right)
Preorder(Root -> Left -> Right)
Postorder(Left -> Right -> Root)

Already learned earlier

BFS (Breadth-First Search)
Visit level by level (root -> children -> grandChildren).
implemented using a Queue (FIFO).

"""
# pyhton implementation 
from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left  = None 
        self.right = None
# Dfs traversal 
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end = " ")
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data, end = " ")
        preorder(node.left)
        preorder(node.right)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end =" ")

# BFS traversal
def bfs(root):
    if not root:
        return 
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end = " ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Buid tree
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")

print("DFS - Inorder: ")
inorder(root)

print("\nDFS - Preorder: ")
preorder(root)

print("\nDFS - Postorder: ")
postorder(root)

print("\nBFS - Levelorder: ")
bfs(root)