# syntax
# def <function_name>():
#     < code block>

# for i in range(11):
#     print(i)
# for i in range(11):
#     print(i)

# def loop_func(n, w):
#     results = []
#     for i in range(n):
#         if i % 2 == 0:
#             results.append(i)
#     return results, w, n
#
#
# # calling of a function
# def sample():
#     even_numbers1 = loop_func(88, 98)
#     return even_numbers1
#
#
# a = sample()
# print(a)
# def sum(a, b):
#     c = a + b
#     return c
#
#
# add = sum(23, 56)
# print(add)
#
#
# def fun1(*data):
#     for i in data:
#         print(i)
#     print("done!")
#
#
# fun1(25, 75, 55)
# fun1(10, 20)
#
#
# def even_num(n):
#     if n % 2 == 0:
#         print("given number is even:", n)
#     else:
#         print("given number is odd:", n)
#
#
# n = int(input("enter the number :"))
#
# even_num(n)

#
# def is_even(list1):
#     global x
#     x = even_num = []
#     odd_num = []
#     for i in list1:
#         if i % 2 == 0:
#             even_num.append(i)
#         else:
#             odd_num.append(i)
#     return even_num, odd_num, x
#
# num = is_even([2, 3, 4, 4, 5,67, 34, 23])
# print(num)

# def addition(*nums):
#     total = 0
#     for i in nums:
#         total += i
#     return total
# total = addition(4, 5, 8, 9, 7, 67, 89)
# print(total)

def factorial(no):
    if no == 0:
        return 1
    else:
        return no * factorial(no - 1)
num = int(input("enter the number "))
print("factorial of a number is:", factorial(num))
