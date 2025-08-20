class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None   # first element 
        self.rear = None    # Last Element

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear: # Empty queue
            
