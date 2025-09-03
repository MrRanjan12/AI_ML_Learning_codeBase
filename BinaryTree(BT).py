# A tree is a hierarchical data structure made of nodes
# Each node can have at most 2 children -> called left and right child.
# The topmost node is called the root.
# Node with no children are called leaves.

# why do we need Tree? 
# They provide hierarchial storage (file system, XML, JSON)
# Searching & sorting -> Binary Search Tree (BST).
# Used in AI/ML -> decision trees, parse trees.

# sample python implementation of a binary Tree Node

# class Node:
#     def __init__(self, data):
#         self.data  = data
#         self.left = None  #left child
#         self.right = None #right child

# # with this we can manually connect nodes to from a tree
# #Creating nodes 
# root = Node("A")
# root.left = Node("B")
# root.right = Node("C")
# root.left.left = Node("D")
# root.left.right = Node("E")
# #     # for printing data manually.
# # print(root.data)    
# # print(root.left.data)
# # print(root.left.right.data)

# # Tree Traversal
# # Traversal = visiting all nodes in same order 
# '''
# 1 Inorder (Left -> Root -> Right)
# 2 Preorder (Root -> Left -> Right)
# 3 Postorder (Left -> Right -> Root)

# '''
# def inorder(node):
#     if node:
#         inorder(node.left)
#         print(node.data, end=" ")
#         inorder(node.right)

# def preorder(node):
#     if node:
#         print(node.data, end=" ")
#         preorder(node.left)
#         preorder(node.right)

# def postorder(node):
#     if node:
#         postorder(node.left)
#         postorder(node.right)
#         print(node.data, end=" ")
# print("inorder:  " )
# inorder(root)

"""
we'll build a small tree, then use id() (which show the memory 
references of an object in  Python) to see hoe parents and children are connected.
"""
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# # Create nodes 
# A = Node("A")
# B = Node("B")
# C = Node("C")
# D = Node("D")
# E = Node("E")

# # Connect nodes (build tree)
# A.left = B
# A.right = C
# B.left = D
# B.right = E

# #Print memory address
# print("A:", id(A))
# print("B:", id(B))
# print("C:", id(C))
# print("D:", id(D))
# print("E:", id(E))

# print("\nConnections stored inside A:")
# print("A.left ->", id(A.left))  #should match B's id 
# print("A.right ->",id(A.right))  #should match C's id

# print("\nReferences stored inside B:")
# print("B.left ->", id(B.left)) # should match D's id
# print("B.right:", id(B.right)) # should match E's id

