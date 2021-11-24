"""1. Write a Python script to sort (ascending and descending) a dictionary by
value."""
# marks = {"tamil": 56, "english": 89, "maths": 63, "science": 78, "social science": 63}
# s_marks = sorted(marks)
# print(s_marks)
""" 2. Write a Python script to add a key to a dictionary. 
Sample Dictionary : {0: 10, 1: 20} 
Expected Result : {0: 10, 1: 20, 2: 30} """

marks = {"tamil": 56, "english": 89, "maths": 63, "science": 78}

marks["social science"] = 78
print(marks)
