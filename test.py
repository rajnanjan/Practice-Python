# # 1."program to find the sum of all the numbers in the list "
# num = [3, 5, 7, 13, 15]
# sum = 0
# for i in num:
#     sum += i
# print("sum of the given number is :",sum)
#
# # 2." find the all the prime number in list "
# num = [2, 3, 5, 7, 11, 13, 15]
# prime_num = []
# print("prime number is :", prime_num)
#
# # 3." find all the squares of number in the list "
# num = [2, 3, 5, 7, 11, 13, 15]
# for i in num:
#     print(i, "squares", i ** 2)
#
# # 4."reverse the array"
# num = [2, 3, 5, 7, 11, 13, 15]
# num.reverse()
# print(num)
#
# # 5." find the max and min element of an array"
# num = [2, 3, 5, 7, 11, 13, 15]
# max_num = 0
# for i in num:
#     if i > max_num:
#         max_num = i
# print("maxmium number is :", max_num)
#
#
# # 6." check  whether a string in palindrome or not"
# names = ["malayalam", "english","tenet"]
# palindrome_names = []
# for i in names:
#     j = i[::-1]
#     if i == j:
#         palindrome_names.append(i)
#
# print("palindrome names is:", palindrome_names)
#
#
# # 7." find the duplicate characters in a string"
# name = "raj nanjan"
# from collections import Counter
#
# x = Counter(name)
# y = [m for m in x.keys() if x[m] > 1]
# print(y)
#
# """ 1. Write a Python program which accepts the user's first
# and last name and print them in reverse order with a space between them."""
#
# first_name = input("Enter the First Name :")
# last_name = input("Enter the Last name :")
# print(last_name, "", first_name)
#
# """2. Write a Python program which accepts a sequence of comma-separated numbers from user
# and generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23') """
#
# number = input("Enter the numbers ")
# list_num = number.split(" ")
# num_in_tuple = tuple(list_num)
# print(list_num, type(list_num))
# print(num_in_tuple, type(num_in_tuple))
#
# """ 3. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"] """
# color_list = ["Red", "Green", "White", "Black"]
# print("first color is :", color_list[0])
# print("last color is :", color_list[-1])
#
# """ 4. Write a Python program to print the calendar of a given month and year. Note : Use 'calendar' module. """
#
# import calendar
#
# month = int(input("enter the month :"))
# year = int(input("enter year :"))
# print(month, year)
#
# print(calendar.month(month,year))
#
# S = "geeksforgeeks"
# y = S[::-1]
# print(y)
# from datetime import date
#
#
# def dates_calculate():
#     f_date = date(2014, 7, 2)
#     last_date = date(2022, 3, 22)
#     days_between = last_date - f_date
#     return days_between.days
#
#
# print(dates_calculate())
#
#
# def is_group_member(group_data, n):
#     for values in group_data:
#         if n == values:
#             return True
#     else:
#         return False
#
#
# print(is_group_member([1, 3, 4, 5, 6, 7], 8))
#
#
# def con_list_into_str(list):
#     con_str = ''
#     for i in list:
#         con_str += str(i)
#     return con_str
#
#
# print(con_list_into_str([5, 1, 1998]))
#
# Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday", "Sunday"}
# # Days2 = {"Friday", "Saturday", "Sunday"}
# # print(Days1 | Days2)
# # print(Days1.union(Days2))
# # print(Days1 & Days2)
# # print(Days1.intersection(Days2))
#
# def upper_d(func):
#     def inner():
#         str1 = func()
#         return str1.upper()
#
#     return inner
#
#
# @upper_d
# def display():
#     return "Welcome all"
#
#
# print(display())
#
#
# def check_vowels(char):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     if char in vowels:
#         return "given char is vowels "
#     else:
#         return "given char is not vowels"
#
#
# def convert_int_to_str():
#     list_of_numbers = [1, 3, 5, 7, 8, 9, 50]
#     num_in_str = ''
#     for i in list_of_numbers:
#         num_in_str += str(i)
#
#     print(num_in_str)
#     print(type(num_in_str))
#
#
# print(convert_int_to_str())
#
#
# def checking_colors():
#     list_of_colors = ["red", "black", "white", "blue"]
#     list_of_colors1 = ["red", "blue", "orange"]
#     results = []
#     for color in list_of_colors:
#         if color not in list_of_colors1:
#             results.append(color)
#     return results
#
#
# print(checking_colors())


# lst = [1,2,3,4,5,6,7,8,9,10]
# for i in range(len(lst)-1, -1, -1):
#     print( lst[i] , end = ' ')

# num = 4
#
# def foo(num):
#   return num**3
#
#
# # print(foo(3)**2
# # print([if i%2==0: i; else: i+1; for i in range(4)])
# print(0.7+0.2==0.9)

# txt = "              Hello World            "
# x = txt.strip()
# print(x)
#


print(bool("abc"))