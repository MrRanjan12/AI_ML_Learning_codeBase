# comming up with level 3 listforce & StringSlice combat 
# Fast Note List & Strings

# fruits = ["apple", "banna", "cherry"]
# print(fruits[0]) 
# print(len(fruits))
# fruits.append("mango")
# print(fruits)

# text = "AI Master"
# print(text[0])
# print(text[-1])
# print(text[0:2])

# color = ["Red","pink","yellow","Gray","Green"]
# print(color[0])
# print(color[4])
# color.append("Orange")
# print(color)
# print(color[::-1])  reversing using slicing 

#🚀 Up Next: Level 4 – FunctionEdge + Array DSA

#defining funtions

# def greet(name):
#     return f"hello, {name}!"
# print(greet("Ranjan kuamr"))

# array list in python 
# arr = [1,2,3,4,5]
# print(sum(arr))
# print(max(arr))
# print(arr[::-1])

# def analyze_number(arr):
#     print(sum(arr))
#     print(sum(arr)/len(arr))
#     print(max(arr))
#     print(min(arr))

# analyze_number([3, 7, 1, 9, 5])
             # or 
# def analyze_number(arr):
#     totle = sum(arr)
#     avg = totle/len(arr)
#     return totle, avg, max(arr), min(arr)
# result = analyze_number([3, 7, 1, 9, 5])
# print("sum:", result[0])
# print("avg:", result[1])
# print("max:", result[2])
# print("min:", result[3])

#  🚀 Next: Level 5 – Search & Sort: DSA Begins!

# def find(x, arr):
#     for i in arr:
#         if i == x:
#             return True
#     return False

# result = find(5, [2,5,3,7,2])
# if result == -1:
#     print("Element not found")
# else:
#     print("Element found")
  
#   Binary search
# def binary_search(arr,  target):
#     left, right = 0, len(arr)-1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return False

# result = binary_search([2, 4, 7, 10, 13, 18, 20], 10)
# print(result)
   
# commig up with level 6 sorting +  Recursion Combat 
# sorting is using every where in ai 
# feature importance for search or models 

# Quick preview : Bubble Sort 

# def bubble_sort(arr):
#     size = len(arr)
#     for i in range(size):
#         for j in range(size - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr 
# print(bubble_sort([10, 2, 8, 5, 1]))      

# dict in pyton 
# person = {
#     "name":"Ranjan",
#     "age":25,
#     "city":"Delhi"
# }

# print(person["name"]) 
# print(person.get("city"))
# person["age"] = 26
# person["email"] = "a@x.com"
# print(person["age"])
# print(person.get("name"))

# Deep dive into hashmap 
# student = {
#     "name": "Ranjan",
#     "age" : 22,
#     "college" : "xyz institude"
# }

# print(student["name"])
# student["age"] = 23
# student["branch"] = "CS"
# del student["college"]
# print(student)

# mark = {
#     "Physics": 67,
#     "Math" : 88,
#     "chemistry" : 90
# }
# print(mark)
# print((sum(mark.values()))/len(mark))

# Lowest and Highest Subject by Marks
# lowest_subject = min(mark, key=mark.get)
# highest_subject = max(mark, key=mark.get)

# print("Lowest Scoring Subject:", lowest_subject, "→", mark[lowest_subject])
# print("Highest Scoring Subject:", highest_subject, "→", mark[highest_subject])

# print(mark.get("Biology", "Not Found"))
   # printing dict using loop
# for subject, score in mark.items():
#     print(subject, ":" ,score)

   #Reversing keys and value
# reversed_dict = {v: k for k, v in mark.items()}
# print(reversed_dict)

    # Looping through mark and Grade based on marks 
    # >90 = A, 70-90 = B, 50-70 = C, <50 = D
# grades = {}
# grade_counts = {"A" : 0, "B" : 0, "C" : 0, "D" : 0}
# for subject, score in mark.items():
#     if score > 90 :
#         grades[subject] = "A"
#         # grade_counts["A"]+=1
#     elif 70 <= score <= 90:
#          grades[subject] = "B"
#         #  grade_counts["B"]+=1
#     elif 50 <= score <= 70:
#          grades[subject] = "C"
#         #  grade_counts["C"]+=1
#     else:
#          grades[subject] = "D"
#         #  grade_counts["D"]+=1

    
# print(grades)
# print(grade_counts)
    #    or
# from collections import Counter 
# grade_list = list(grades.values())
# grade_counts = Counter(grade_list)
#      # this will print the result
# print(grade_counts)
#       #this gives all the grade valueS:
# print(grades.values())
#       # convert that to a list:
# print(list(grades.values()))
    
