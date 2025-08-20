# prices = [250, 300, "240", 400]
# try:
#     # block that may cause and excepion
#     total = sum(prices)
#     print(total)

# except TypeError:
#     # To perform if there is an exception 
#     print("invalid data type")

# print("Happy s hopping")

      #  example of nameError
# color = "Green"
# try:
#   print(color)
# except NameError:
#   print("Check the variable name")

     #<<<----When you specify only one type of exception to be handled, other types of exceptions will not be covered. 
     # If these other exceptions occur, the program execution will fail.

# color = ["Red", "Yellow", "Green"]
# try:
#     # indexError
#     print(color[10])
#     # Wrong exception 
# except NameError:
#     print("Error")

# # will not be executed
# print("happy Shopping")

#----->>>>>

# We can have multiple except block to handle each possible exception
# color = ["Red", "Yellow", "Green"]
# try:
#     print(color[10])
# except IndexError:
#     print("Out of Range")
# except NameError:
#     print("Variable is not defiend")

# print("Happy shoping")

# handling exception at the time of user input
# print("Enter input")
# price = input() 
# try:
#     price_value = int(price)
# except ValueError:
#     print("Please enter a number")


# We can use the finally statement to perform and operation after the 
# try/ except block, no matter if an exception occured or not.
# prices = [559, 879, "N/A", 349]
# try:
#     print(sum(prices))
# except TypeError:
#     print('Check the price')
# finally:
#     print("Need help? Contact us")

   # <<<<.........
# The else statement can be used in conjunction with 
# the try / except block and will execute only when no erro in the try block

# books = ["harry Potter", "Dune", "Emma"]
# try:
#     choice = books[1]
# except IndexError:
#     print("Out of the range")
# else:
#     print(choice + " is a great choices!")

    #<<<<......^^^^^

#<<//////..........
# We can trigger our own exceptions based on specific condition 
# using the raise statement. This will immediately stop the program's execution 
# indicate an error has occured.

# print("Rate from 0 to 10")
# rate = 15
# if rate > 10 or rate < 0:
#     raise ValueError
# /////.......>>>

# To make exception more helpfull for the program users 
# we can add a message describing the error.
# rating  = 15
# if rating > 10 or rating < 0:
#     raise ValueError("Rate from 0 to 10")

try:
  print(3 + "3")
except ValueError:
  print("Cannot add different types")
except TypeError:
  print("Type mismatch error")