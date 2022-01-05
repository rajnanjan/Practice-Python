'''List Comprehension'''
#
# nums = []
#
# for i in range(1, 21):
#     nums.append(i * 2)
#
# print(nums)


# filter
# def is_add(num):
#     return num % 2 == 1
# def is_even(num):
#     return num % 2 == 0
#
#
# num = [1, 3, 4, 5, 6, 7, 7, 4, 3, 5, ]
#
# odd_num = filter(is_add, num)
# for i in odd_num:
#     print(i, end=", ")

# def square_num(num):
#     return num * num
#
#
# square = map(square_num, num)
# print(num)
# print(list(square))
#
"1 Find all of the numbers from 1–1000 that are divisible by 8"
#
# list1 = [i for i in range(1, 1000) if i % 8 == 0]
# print(list1)
" Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension."

list1 = [i for i in range(1, 100, 13)]

print(list1)

"Use list comprehension to construct a new list but add 6 to each item."

list2 = [i + 6 for i in list1]
print(list2)


"Using list comprehension, construct a list from the squares of each element in the list."

list3 = [i*i for i in list2]
print(list3)

"Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50."

list4 = [i ** 2 for i in list3 if i ** 2 > 50]
print(list4)

""" Given dictionary is consisted of vehicles and their weights in kilograms. 
Contruct a list of the names of vehicles with weight below 150 kilograms. 
In the same list comprehension make the key names all upper case."""

dic1 = {"Pulsar": 150, "Ktm": 130, "R15": 160, "FZ": 175}

list2 = [i.upper() for i in dic1 if dic1[i] < 150]

print(list2)

# dictionary comprehension

"""Create a dictionary from the list with same key:value pairs, such as: {"key": "key"}."""
list1 = ["raj", "siddu", "mani", "sachin", "manoj"]
list2 = [1, 2, 3, 4, 5]

dic2 = {k: v for (k, v) in zip(list1, list2)}
print(dic2)

""" First, create a range from 100 to 160 with steps of 10.


Second, using dict comprehension, create a dictionary where each number in the range is the key
 and each item divided by 100 is the value."""

dic1 = {i: i / 100 for i in range(100, 160, 10)}

print(dic1)

""" Using dict comprehension and a conditional argument 
create a dictionary from the current dictionary where only the key:value pairs
 with value above 2000 are taken to the new dictionary."""

dic1 = {"tcs": 3884.75, "reliance": 2458, "hdfc": 1528, "hindusthan}": 2401}
dic2 = {i: dic1[i] for i in dic1 if dic1[i] > 2000}
print(dic2)

dic3 = {i: dic1[i] for i in dic1 if dic1[i] < 2000}
print(dic3)
