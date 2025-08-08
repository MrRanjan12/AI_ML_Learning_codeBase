# Stack + Queue (Level 7:Linear Ds)
# used in :
# undo/Redo system 
#Browser navigation 
#Bfs/Dfs traversal
#AI: TOcken history, recursion call tracing 

# deep Explanation : Stack 
# LIFO (Last In, Fist Out)
# Think: A stack of plates
 # python stack using List

# stack = []
# stack.append("A")
# stack.append("B")
# print(stack.pop())

# Task
# Stack = []
# Stack.append("R")
# Stack.append("A")
# Stack.append("N")
# Stack.append("J")
# Stack.append("A")
# Stack.append("N")
 
# while Stack:
#  item = Stack.pop() 
#  print(item)

# Task 2
# reversing string using stack 
# name = "Ranjan"
# stack = list(name)

# while stack:
#     print(stack.pop(),end= "")

# if stack:
#     print("Top of the Stack:", stack[-3])
#getting size of the stack 
# print("Stack size :",len(stack))

#   now moving to : Queue - FIFO
#   deep understanding : Queue
  #Fifo  first in first out 
# Think :People standing in line for tea 

# Queue in python using with  collection.deque

# from collections import deque
# queue = deque() 
# queue.append("R")
# queue.append("A")
# queue.append("N")
  
# print(queue.pop())

#Task 4

# from collections import deque
# queue = deque()
# queue.append("R")
# queue.append("A")
# queue.append("N")
# queue.append("J")
# queue.append("A")
# queue.append("N")

# while queue:
#  print(queue.popleft())

