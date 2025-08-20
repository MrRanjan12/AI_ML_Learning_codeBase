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
names = ["alice", "bob", "CHARLIE", "dEborah"]
# Function to capitalize each name 
def capitalize(name):
    return name.capitalize()
#using map() to apply the capitalizaton to each name 
capitalize = map(capitalize, names)
# converting map object to a list
capitalize = list (capitalize)
print(capitalize) 
#<------------------------------------->

