"""
Binary Search Tree (BST)
A Special binary tree where:
Left child < Parent
Right child > Parent
No duplicates (in standard BST)
This ordering makes search, insertion, and 
deletion efficient (O(log n) average).
"""
# python implementation 
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class BST:
#     def __init__(self):
#         self.root = None
   
#    #insert node
#     def insert(self, root, data):
#         if root is None:
#             return Node(data)
#         if data < root.data:
#             root.left = self.insert(root.left, data)
#         elif data > root.data:
#             root.right = self.insert(root.right, data)
#         return root
#     # search node 
#     def search(self, root, key):
#         if root is None or root.data == key:
#             return root
#         if key < root.data:
#             return self.search(root.left, key)
#         return self.search(root.right, key)
    
#     # inorder travaersal (gives sorted output)
#     def inorder(self, root):
#         if root:
#             self.inorder(root.left)
#             print(root.data, end=" ")
#             self.inorder(root.right)   

# tree = BST()
# root = None
# root = tree.insert(root, 50)
# root = tree.insert(root, 30)
# root = tree.insert(root, 70)
# root = tree.insert(root, 20)
# root = tree.insert(root, 40)
# root = tree.insert(root, 60)
# root = tree.insert(root, 80)

# print("Inorder Traversal (sorted):")
# tree.inorder(root)
# print("\nSearching 40:", "Found" if tree.search(root, 40) else "Not Found")
# print("\nSearching 90:", "Found" if tree.search(root, 00) else "Not Found")

#### <----------->

"""  Deletion  """
# Let's a delete method to your BST class 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self, data = None):
        if data is not None:
            self.root = Node(data)
        else:
            self.root = None
    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end = " ")
            self.inorder(root.right)
    
    def minValueNode(self, node):
        """Helper to find the smallest value in a subtree"""
        current = node
        while current.left:
            current = current.left
        return current
    
    def delete(self, root, key):
        if root is None:
            return root
        
        # case 1: go left 
        if key < root.data:
            root.left = self.delete(root.left, key)
        
        # case 2: go right
        elif key > root.data:
            root.right = self.delete(root.right, key)

        # case 3: key == root.data(delete this node)
        else:
            # Node with one or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # Node with two children 
            successor = self.minValueNode(root.right)
            root.data = successor.data
            root.right = self.delete(root.right, successor.data)
        return root

tree = BST()
root = None
root = tree.insert(root, 30)
root = tree.insert(root, 70)
root = tree.insert(root, 20)
root = tree.insert(root, 40)
root = tree.insert(root, 60)
root = tree.insert(root, 80)

# printing value in inorder before deletion 
print("Inorder before deletion: ")
tree.inorder(root)

# delete a node
print("\nDeleting 20 (leaf)...")
root =  tree.delete(root, 20)
tree.inorder(root)

print("\nDeleting 30 (one child)...")
root = tree.delete(root, 30)
tree.inorder(root)

print("\nDeleting 50 (two children)...")
root =  tree.delete(root, 50)
tree.inorder(root)