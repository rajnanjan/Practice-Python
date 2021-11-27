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
# marks = {"tamil": 56, "english": 89, "maths": 63, "science": 78, "social science": 63, "pt": 76}
# if "pt" in marks:
#     marks.pop("pt")
# print(marks)
""" 7. Write a Python program to print all unique values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}] 
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""
# scores = {"raj": 85, "mani": 98, "sachin": 90, "manoj": 85, "sid": 98}
# u_scores = set()
# for i in scores.values():
#     u_scores.add(i)
# print(u_scores)
""" 8. Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string. 
Sample string : 'w3resource' 
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1} """

name = input("enter the name :")
d_name = {}
for st in name:
    if st in d_name:
        d_name[st] += 1
    else:
        d_name[st] = 1
print(d_name)






