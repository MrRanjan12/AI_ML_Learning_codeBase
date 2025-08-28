# Funtions in python play a crucial role in enhancing the efficiency, 
# reuseability, and organization of code 
   

#  After assigning a function to a variable, you can use the variable to call the function.
# def welcome(name):
#     return "Welcome, " + name
# greet = welcome
# greet("bob")

# Functions can take other funtions as arguments.
# def welcome(name):
#     return "Welcome " + name

# def process_user(name, func):
#     return func(name)

# print(process_user("Alice", welcome))
           # <--------------------->
#In Python, functions that operate with other
#  functions — that is, take another function as an argument or return a 
# function -  are called Higher-Order Functions. 
# They are particularly useful for processing various 
# functions and returning specific results.
# def welcome(name):
#     return "welcome " + name
# def bye(name):
#     return "Goodbye " + name

# def process_user(name, func):
#     return func(name)

# result1 = process_user("Ranjan", welcome)
# result2 = process_user("Ranjan", bye)
# print(result1)
# print(result2)
        #<--------------------->

#An important concept in Functional Programming is Pure Functions.
# A function is called pure if it gives the same result every
# time you give it the same inputs, and it doesn't affect anything
#  outside of the function. This makes them trustworthy and simpler
#  to understand.
# def total(price, count):
#    return price * count

#<<-------------------------->
 # Lambda expressions are funtions without a name that are quickly to create and use.
# They are written in just one line using the lambda keyword and are often 
# used for small, simple tasks.

# greet  = lambda name: "Welcome, " + name
# print(greet("Scientist Ranjan"))
# <<--------------------------->

   # syntax ->   
#<<<<--   lambda <argument> : <expression>  -->>>>
  # Lanbda expressions perform a single operation and return a result.
# They are defiend using the lambda keyword, followed by its arguments,
# a colon, and the expression to perform.

#<<<---------------------------->
# the power of lambda is better shown when you use them as an anonymous 
# function inside another function. Say you have a function definition that 
# takes one argument, and that argument will be multiplied with an unknown 
# number

# def mult(n):
#     return lambda a : a * n
# doubler = mult(2)
# tripler = mult(3)

# print(doubler(5))
# print(tripler(5))

# <--------------------------------->
# The Map() function applies a specific function to every element in 
# an iterable, like list or tuples. It produce a result that can be 
# transformed into list using the list() funtion for easy viewing or further use.
# 
# # lsit of the name in variable 
# names = ["alice", "bob", "CHARLIE", "dEborah"]
# # Function to capitalize each name 
# def capitalize(name):
#     return name.capitalize()
# #using map() to apply the capitalizaton to each name 
# capitalize = map(capitalize, names)
# # converting map object to a list
# capitalize = list (capitalize)
# print(capitalize) 
#<------------------------------------->
    # map funtion required  --->   map(<function>,<iterable)
# exam_scores = [85, 62, 95, 40, 78]
# def is_passing(score):
#     return "Pass" if score >= 70 else "Fail"
# status = list(map(is_passing,exam_scores))
# print(status)

#<----------------------------------------->
# using lanmbda expression inside the map function
# numbers = [1,2,3]
# doubled = list(map(lambda x:x*2, numbers))
# print(doubled)

#<------------------------------------------->

# The filter() function, just like the map() funtion, takes in a funtion 
# and an iterable as arguments. The key purpose of filter() is to apply a 
# condition specified in the provided funtion to each item in iterable and return 
# and return only those for which the function evaluates to True

# this code filters and returns product with names 4 characters long.

# products = [" Table", "Sofa","Cushion","Bookshelf","vase"]
# # filter products with name length equal to 4
# filtered_prod = list(filter(lambda name: len(name) == 4, products))
# print(filtered_prod)   

#<--------------------------------------------->

# The map() and filter() funtions can work with any iterable. 
# In the example below, filter() is used to extract items from 
# the products dictionary, where prices are under 90.

# products = {"Table": 110, "Sofa": 120, "Chair": 45, "Lamp": 70}
# # filtering products with prices less than 90 
# filtered_products = dict(filter(lambda item: item[1] < 90, products.items()))
# print(filtered_products)

#<----------------------------------------------->

# If the number of argument of our function is unknown and unpredictable,
# you can always use an iterable as an argument.

# def total(numbers):
#     result = 0
#     # iterating over the list 
#     for i in numbers:
#         result += i
#     return result
# nums = [1,2,3,4,5]
# print(total(nums))

#<--------------------------------------------------->

# def display(*words):
#     for item in words:
#         print(item)

# display("Paper", "Pen","pencil")

#<----------------------------->
# When defining a function with both regular arguments and *args, the 
# regular arguments must come before *args in the function definiton.

# for example
# def show_items(category, *items):
#     print("Categories: ", category)
#     for item in items:
#         print(item)
# show_items("Electronics","laptop","Smartphone","tablets")    

#<------------------------------->
# Python also you to pass keyword argument using **Kwargs. In this 
# case, **kwargs recieves arguments in the form of a dictionary, consisting of key:value pairs.

#** kwargs is a dictionary 
# def display_info(**kwargs):
#     #kwargs.item() return the key:value pairs
#     for key, value in kwargs.items():
#         print(key, ":", value)
# display_info(name = "Alice", age = 30, city = "New York")

#<------------------------------->

# Imagine you have a function that generates a message. your goal is to 
# create another function that takes this original function as an
# argument and converts the original message into uppercase, without altering 
# the original function's code.
# These functions are known as decorators. In the code below, the uppercase() function
# acts as decorator, and the wrapper() funtion represents the modified (or decorated) 
# version of the greet() function.

# def greet():
#     return "welcome!"
# # takes a funtion as an argument 
# def uppercase(func):
#     #Wrapper function to keep the 
#     #original function code unchanged 
#     def wrapper():
#         orig_message = func()
#         modified_message = orig_message.upper()
#         return modified_message
#     return wrapper
# gree_upper = uppercase(greet)
# print(gree_upper())

#<---------------------------->
'''
We can apply a decorator to a function using the @ sign. It 
improves the code readability and provides a clean separation 
between the function and its decoration.
When a function with a decorator is called, it automatically include the 
behaviour defiend in the decorator.
'''
# def uppercase(func):
#     def wrapper():
#         orig_message = func()
#         modified_message = orig_message.upper()
#         return modified_message
#     return wrapper

# @uppercase
# def greet():
#     return "Welcome!"

# # using the decorated function 
# print(greet())

#<----------------------------------->

"""
Decorators are a powerful feature, offering a concise, readable,
and efficient way to enhance the functionality of existing funtions.
We can apply the same decorators to several different functions:
"""

# def stock_status_decorators(func):
#     def wrapper(item):
#         result = func(item)
#         print(result, ": stock status for", item )
#         return result
#     return wrapper
# @stock_status_decorators
# def restock_item(item):
#     return "Restocked"

# @stock_status_decorators
# def sell_item(item):
#     return "Sold"

# print(restock_item("Laptop"))
# print(sell_item("Smartphone"))

