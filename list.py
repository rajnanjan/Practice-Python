""" 1. Write a Python program to sum all the items in a list. """
# num = [1, 3, 5, 6, 7, 13, 56]
# sum_of_num = 0
# for i in num:
#     sum_of_num = sum_of_num + i
# print("Sum of all items :", sum_of_num)
""" 2. Write a Python program to multiplies all the items in a list."""
# num = [1, 3, 5, 6, 7, 13, 56]
# sum_of_num = 1
# for i in num:
#     sum_of_num *= i
# print(sum_of_num)
""" 3. Write a Python program to get the smallest number from a list."""
# num = [3, 5, 6, 7, 13, 56, 2]
# print("The smallest number in list :", min(num))
# print("The highest number in list :", max(num))
""" 4. Write a Python program to remove duplicates from a list."""
num = [3, 5, 6, 7, 2, 3, 13, 56, 2, 5, 7]
print("The original list :",num)
un_num = []
for i in num:
    if i not in un_num:
        un_num.append(i)
un_num.sort()
print("After removing duplicates from list:",un_num)



