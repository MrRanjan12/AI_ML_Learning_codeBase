# why use linkedlist for Stack
# Dynamic size No fixed momory like arrays
# O(1) insertion & deletion at the top 
# perfect for function call backtracting in AI algorithms parsing expressions.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            print("Stack is empty:")
            return Node
        popped_value = self.top.data
        self.top = self.top.next 
        return popped_value
    
    def peek(self):
        if not self.top:
            return None
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end ="->")
            temp = temp.next
        print("None")
    

# example uses 
stack = Stack()
stack.push("R")
stack.push("A")
stack.push("N")
stack.push("J")
stack.push("A")
stack.push("N")

print("Top Element: ", stack.peek())
print("popped :", stack.pop())
stack.display()