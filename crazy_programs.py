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

data = input("Enter the Numbers:")
num = data.split(",")
num_tuple = tuple(num)
print(num)
print(num_tuple)
print(type(num))
print(type(num_tuple))
