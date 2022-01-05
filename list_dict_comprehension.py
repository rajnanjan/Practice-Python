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

list1 = [i for i in range(1200, 2000, 130)]

print(list1)

"Use list comprehension to construct a new list but add 6 to each item."

list2 = [i + 6 for i in list1]
print(list2)


"Using list comprehension, construct a list from the squares of each element in the list."

list3 = [i*i for i in list2]
print(list3)
