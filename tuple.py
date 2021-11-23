""" 1. Write a Python program to create a tuple."""
# num = (2, 5, 6, 7, 8)
# print(num)
# print(type(num))
""" 2. Write a Python program to create a tuple with different data types"""
# values = (1, 45.8, "raj", True)
# print(values)
""" 3. Write a Python program to unpack a tuple in several variables."""
# num = [1, 2, 5, 58]
# (n1, n2, n3, n4) = num
# print(n1, n2, n3, n4)
""" 4. Write a Python program to find the repeated items of a tuple."""
# num = [3, 5, 6, 7, 2, 3, 13, 56, 2, 5, 7]
# repeated_value = []
# for i in num:
#     if num.count(i) > 1:
#         if i not in repeated_value:
#             repeated_value.append(i)
# print(repeated_value)
""" 6. Write a Python program to check whether an element exists within a tuple."""
num = [3, 5, 6, 7, 2, 3, 13, 56, 2, 5, 7]
user_num = int(input("enter the num :"))
for i in num:
    if user_num == i:
        print(" given number already exists ")
        break
    else:
        print("given number is not in the tuple ")
        break






