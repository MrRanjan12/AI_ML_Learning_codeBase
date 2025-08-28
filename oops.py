# class person:
#     def __init__(cast, castName):
#         cast.castName = castName

# person1 = person("Pandit")
# print(person1.castName)
        

# now in linkedlist code 
# node is a blueprint for creating nodes 
# linkedlist  is a blueprint for creating the list 

# now connecting to the code with linkedList

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None       

#     def insert_end(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node

#     def insert_begin(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
    
#     def delete(self, key):
#         temp = self.head
#         if temp and temp.data == key:
#             self.head = temp.next
#             return
#         prev = None
#         while temp and temp.data != key:
#             prev = temp
#             temp = temp.next
#         if temp:
#             prev.next = temp.next

    
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end = " -> ")
#             temp = temp.next
#         print("None")

# #Creating and inserting 

# my_list = LinkedList()  # empty list
# my_list.insert_end("R") 
# my_list.insert_end("A")
# my_list.insert_end("N")
# my_list.insert_begin("J")
# my_list.delete("A")

# # displaying the output 

# my_list.display()

#<------------------>

# class Car:
#     # initilize attributes 
#     def __init__(self, brand, color):
#         # assign values to attributes
#         self.brand = brand
#         self.color = color
# # Create an object of the Car Class 
# my_car = Car("Audi", "yellow")
# print(my_car.color)
        
        #<---------->
# # Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def move(self):
#         print("Moving")
# #Inherits from Animal class 
# class Dog(Animal):
#     #Specific behaviour 
#     def bark(self):
#         print("woof!")
# #Creating and instance 
# my_dog = Dog("Bob")

# # inherited attribute and behavior 
# print(my_dog.name)
# my_dog.move()
# # Specific behavior
# my_dog.bark()

#<-------------------------->

#If a child class needs both inherited and new attributes,
#  define its own __init__ method, call super().__init__() to reuse the parent’s
#  attributes, and then add the extra ones normally.

# parent class 
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def move(self):
#         print("Moving")
# # child class 
# class Dog(Animal):
#     def __init__(self, name, breed, age):
#         # initialize attributes of the supperclass
#         super().__init__(name)
#         #Additional attributes specific to DOg
#         self.breed = breed
#         self.age = age
    
#     def bark(self):
#         print("Woof!")

# my_dog = Dog("Jax", "Bulldog", 5)
# #Inherited attribute
# print(my_dog.name)

# # Additional attributes
# print(my_dog.breed)
# print(my_dog.age)
  #<=====================>
# Class methods are called on the class itself, not on 
# indivisual instances. This allows their use without needing to create 
# a class as a whole, rather than actions limited to single object.
# Here's an example:

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
# regular method 
    def describe_book(self):
        print(self.title, "by", self.author)

# class method 
    @classmethod
    def books_in_series(cls, series_name, number_of_books):
        print("There are ", number_of_books, "books in the", series_name, "series")

#Creating and instance of book
my_book = Book("Harry Potter and the Sorcerer's", "J.K. Rowling")

#Using the instance method to describe the book
my_book.describe_book()
#Using the class method to display information about the series 
Book.books_in_series("Harry Potter", 7)