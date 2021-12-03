"""1. Write a Python program which accepts the user's
first and last name and print them in reverse order with a space between them."""

# first_name = input("Enter your first name :")
# last_name = input("Enter the last name :")
#
# print(last_name + " " + first_name)
""" 2. Write a Python program which accepts a sequence of comma-separated numbers from user 
and generate a list and a tuple with those numbers. 
Sample data : 3, 5, 7, 23 
Output : 
List : ['3', ' 5', ' 7', ' 23'] 
Tuple : ('3', ' 5', ' 7', ' 23') """

# data = input("Enter the Numbers:")
# num = data.split(",")
# num_tuple = tuple(num)
# print(num)
# print(num_tuple)
# print(type(num))
# print(type(num_tuple))
""" 3. Write a Python program to display the first and last colors 
from the following list. color_list = ["Red","Green","White" ,"Black"]"""
#
# colors = input("enter the colors name with comma :")
#
# print("given colors:      ", colors)
# given_colors = colors.split(",")
# print("The first color is :   ", given_colors[0])
# print("The last color is :    ", given_colors[-1])


a = [1, 8, 4, 6, 9, 0, 3, 5]


def find_the_index(li):
    length = len(li)
    for i in range(length):
        if li[i] == 9:
            return i

    print("Hello world")


result = find_the_index(a)
print(result)
