# a linkedlist is a chain of nodes where 
# each node holds some data and a references or pointer t
# the next node

# node definition in python 
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# Building a linkedlist 
# class Node:
#     def __init__(self, data):
#         self.data =  data
#         self.next = None
# # Creating nodes
# n1 = Node("R")
# n2 = Node("A")
# n3 = Node("N")         

# # Linking nodes 
# n1.next = n2
# n2.next = n3

# #Traverse and print 
# current =  n1
# while current:
#     print(current.data)
#     current = current.next


# Task -5 Build Linked List 
# deffining mode 

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# # creating node
# n1 = Node("R")
# n2 = Node("A")
# n3 = Node("N")
# n4 = Node("J")
# n5 = Node("A")
# n6 = Node("N")

# # linking 
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6

# # traversing and printing value 
# current = n1
# while current:
#     print(current.data)
#     current = current.next

# full templates with insert and delete

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

