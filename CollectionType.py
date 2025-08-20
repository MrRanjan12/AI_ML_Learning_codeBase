# Pyhton Intermediet learning from sololearn 
#  this is the exanple of list that is mutable 
# colors =["Yellow","Red","Blue"]
# print("Original List:")
# print(colors)

# # making changes 
# colors[1] = "Orange"
# colors.append("Black")
# print("Changed list")
# print(colors)

# this is example of tuple that is immuatable
    # this is throught error because i try to make changes in tuple 
# eiffel_tower = (48.8584, 2.2945)
# eiffel_tower[0] = 56.7581

# Tuples like list can contain duplicate elements
# You can use the count() function to calculate the number of occurance of an item in a tuple.
# score = (7,9,9,8,9)
# print("# of 7 :", score.count(7))
# print("# of 9 :", score.count(9))
# print("# of 2 :", score.count(2))


# << we can use tuple and list in any controle flow structure >>
# points = (12, 14, 9, 10, 9)
# for point in points:
#     if point > 10:
#         print(point, ": passed")


# Tuple unpacking allows for assiging tuple items to variables. The values 
# will be assigned in the order they appear in the tupple

# birthday_date = (12, "August", 1993)
# day, month, year = birthday_date

# print(day)
# print(month)
# print(year)

# The * operator in tuple unpacking is used to gather multiple elements from 
# the tuple into a list. This is usefull when dealing with tuples of unknown length.

# scores =  (98, 69,255 ,21, 41)
# winner, *rest = scores\

# print(winner)
# print(rest)

# Sets unlike list and tuples are unordered collections. They are created 
# with curly brackets{}.

# #syntax
# guests = {"Mery", "Anna", "Jonathan"}

# Sets are unordered and don't support indexing or slicing.

# guestes = {"Mery", "Anna", "Jonathan"}
# print(guestes)
# print(guestes[0]) #error


   # sets can't have duplicates value
   # In this duplicate value will be ignored instead of error 
# friends = {"Anna", "Mery","Mery", "Jonathan"}
# print(friends)

# Sets are mutable meaning you can add or remove items from them.
# guests = {"Anilkumar", "Mery", "Jonathan"}
# # adding princekumar
# guests.add("Princekumar")
# # removing Jonathan
# guests.remove("Jonathan")
# # guests.clear()   for clear set or remove all element form the set
# print(guests)

# calling the union() funtion return a new set with all elements from both 
# sets, omitting duplicates 

# set1 = {"apple", "banana"}
# set2 = {"banana", "Cherry"}

# combined_set = set1.union(set2)
# print(combined_set)

# The difference() function return a set containing elements that are only 
# in th first set and not in the second.

# set1 = {"Apple", "Banana","Cherry"}
# set2 = {"Banana", "Oranage"}

# unique = set1.difference(set2)
# print(unique)


# nums = []
# for x in range(1,51):
#     nums.append(x)
# print(nums)
  #or  List Comprehension  making shorthand 
# nums = [x for x in range(1,51)]
# print(nums)

# .... << printing hashtag using comprehension >>...
# tags = ["travel", "vacation", "journey"]

# hashtags = ["#" + x for x in tags]
# print(hashtags)
     #<<<...................
# We can incorporate a condition into list comprehension,
# placed after the iterable.
# for example, the following code filter out names that start with B
   
# users = ["Brandan","Emma","Brian",
#          "Sophia","Bella", "Ethan", 
#          "AVa","Benjamin","Mia","Chloe"]

# group = [x for x in users if x[0] == "B"]
# print(group)

 # ^^^^^^^^^^..............
     # problem for practice

# words = ["tree", "button", "cat", "window", "defenestrate"]

# # Use a list comprehension to filter out words longer than four letters
# long_word = [x for x in words if len(x) > 4]
# # Display the filtered list
# print(long_word)

