# ''' for loop '''
print(233 % 7.9)
for i in range(21):

    if i % 2 != 0:
        print(i)

""" 1- Write a program to print the following using for loop
     a. First 10 Even numbers
     b. First 10 Odd numbers
     c. First 10 Natural numbers
     d. First 10 Whole numbers """
# for num in range(0, 20, 2):
#     print(num)

# for num in range(1, 20,2):
#     print(num)

# for num in range(1, 11):
#     print(num)
#
# for num in range(0, 10):
#     print(num)
""" 2-Write a program to print first 10 integers and their squares like
1 1
2 4
3 9 and so on"""

# print("numbers\t\t\squares")
# for num in range(1, 11):
#     print(num, "\t\t\t", num ** 2)

""" 3-Write for loop statement to print the following series:
10, 20, 30 … … 300"""

# for num in range(10, 301, 10):
#     print(num, end=",")

""" 4-Write a for loop statement to print the following series
105, 98, 91 ………7 """

# for num in range(105,6,-7):
#     print(num, end=",")

""" 5- Write a program to print first 10 natural number in reverse order."""

# for num in range(10,0,-1):
#     print(num,end=",")

""" 6- Write a program to print table of a number entered from the user."""

# num = int(input("enter the number :"))
#
# for i in range(1,11):
#     print(i, "*", num*i)

"""7-Write a program to display all even numbers that falls between two numbers
 (exclusive both numbers) entered from the user."""
#
# start_num = int(input("enter the first number :"))
# end_num = int(input("enter the second number :"))
# if start_num > end_num:
#     for num in range(end_num+1,start_num):
#         if num % 2 ==0:
#             print(num)
# else:
#     for num in range(start_num+1,end_num):
#         if num % 2 == 0:
#             print(num)

n = int(input("enter the number of row"))
for i in range(0, n):
    for j in range(0, i+1):
        print("*", end=" ")
    print()