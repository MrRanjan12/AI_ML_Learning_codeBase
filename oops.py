# class person:
#     def __init__(cast, castName):
#         cast.castName = castName

# person1 = person("Pandit")
# print(person1.castName)
        

# now in linkedlist code 
# node is a blueprint for creating nodes 
# linkedlist  is a blueprint for creating the list 

# now connecting to the code with linkedList

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
            print(temp.data, end = " -> ")
            temp = temp.next
        print("None")

#Creating and inserting 

my_list = LinkedList()  # empty list
my_list.insert_end("R") 
my_list.insert_end("A")
my_list.insert_end("N")
my_list.insert_begin("J")
my_list.delete("A")

# displaying the output 

my_list.display()
