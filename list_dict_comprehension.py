'''List Comprehension'''
#
# nums = []
#
# for i in range(1, 21):
#     nums.append(i*2)
#
# print(nums)
#
# nums2 = [i for i in range(1, 21)]
#
# print(nums2)
#
# nums2 = [i*2 for i in range(1, 21)]
# print(nums2)
#
# '''Dict Comprehension'''
#
# names = ['sachin', 'sanju', 'lokesh', 'geetha', 'raaju', 'manoj']
#
# '''Enumerate'''
# dict_2 = {}
# for i, j in enumerate(names):
#     dict_2[i] = j
#
# print(dict_2)
#
# dict1 = {key: value for key, value in enumerate(names)}
#
# print(dict1)

'''Filter , Map, Reduce'''
# filter()
# map()

'''Map'''
# Python program to demonstrate working
# of map.

# Return double of n
# def addition(n):
#     return n + n

# We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))

'''Filter'''


# function that filters vowels
# def fun(variable):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if variable in letters:
#         return True
#     else:
#         return False
#
#
# sequence
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
#
# # using filter function
# filtered = filter(fun, sequence)
#
# print('The filtered letters are:')
# for s in filtered:
#     print(s)
# # Python code to demonstrate dictionary
# comprehension

# # Lists to represent keys and values
# keys = ['a', 'b', 'c', 'd', 'e']
# values = [1, 2, 3, 4, 5]
#
# # but this line shows dict comprehension here
# myDict = {k: v for (k, v) in zip(keys, values)}
#
# # We can use below too
# # myDict = dict(zip(keys, values))
#
# print(myDict)


def is_add(num):
    return num % 2 == 1


num = [1, 3, 4, 5, 6, 7, 7, 4, 3, 5, ]

odd_num = filter(is_add, num)
print(list(odd_num))


