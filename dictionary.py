"""1. Write a Python script to sort (ascending and descending) a dictionary by
value."""
# marks = {"tamil": 56, "english": 89, "maths": 63, "science": 78, "social science": 63}
# s_marks = sorted(marks)
# print(s_marks)
from turtle import update

""" 2. Write a Python script to add a key to a dictionary. 
Sample Dictionary : {0: 10, 1: 20} 
Expected Result : {0: 10, 1: 20, 2: 30} """

# marks = {"tamil": 56, "english": 89, "maths": 63, "science": 78}
#
# marks["social science"] = 78
# print(marks)
""" 3. Write a Python script to concatenate following dictionaries to create a new one. 
Sample Dictionary : 
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60} 
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# dic4 = {}
# for i in dic1, dic2, dic3:
#     dic4.update(i)
# print(dic4)
""" 4. Write a Python program to iterate over dictionaries using for loops."""
""" 6. Write a Python program to remove a key from a dictionary."""
marks = {"tamil": 56, "english": 89, "maths": 63, "science": 78, "social science": 63, "pt": 76}
if "pt" in marks:
    marks.pop("pt")
print(marks)



