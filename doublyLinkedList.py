class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head

        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end = " <-> ")
            temp = temp.next
        print("None")

    def display_backward(self):
        temp = self.head
        if not temp:
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end = " <->")
            temp = temp.prev
        print("None")

d11 = DoublyLinkedList()
d11.insert_end(10)
d11.insert_end(20)
d11.insert_end(30)

print("printing traversal forward:")
d11.display_forward()

print("Printing backward traversal")
d11.display_backward()