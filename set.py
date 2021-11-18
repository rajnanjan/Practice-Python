""" 1. Write a Python program to create a set."""
# values = {"apple","orange","mango"}
# print(values)
# print(type(values))
""" 2. Write a Python program to iteration over sets."""
# values = {"apple","orange","mango"}
# fruits = set(values)
# print(fruits)
# print(type(fruits))
"""3. Write a Python program to add member(s) in a set."""
# values = {"apple", "orange", "mango"}
# values.add("banana")
# print(values)
""" 4. Write a Python program to remove item(s) from set """
# values = {"apple", "orange", "mango"}
# values.remove("mango")
# print(values)
# """ 5. Write a Python program to remove an item from a set if it is present in the set. """
# num = {1, 4, 5, 8, 6, 56, 78}
# num.discard(56)
# print(num)
""" 6. Write a Python program to create an intersection of sets."""
# roll_no = {1, 2, 3, 4, 5, 6, 7, 8}
# rank_no ={12, 4, 6, 7, 3, 4}
# common_no = roll_no.intersection(rank_no)
# print(common_no)
# print(common_no)
""" 7. Write a Python program to create a union of set"""
# roll_no = {1, 2, 3, 4, 5, 6, 7, 8}
# rank_no ={12, 4, 6, 7, 3, 4}
# common_no = roll_no.union(rank_no)
# print(common_no)
""" 8. Write a Python program to create set difference."""
# roll_no = {1, 2, 3, 4, 5, 6, 7, 8}
# rank_no = {1, 2, 4, 6, 7, 3}
# num = roll_no.difference(rank_no)
# print(num)
""" 9. Write a Python program to create a symmetric difference."""
roll_no = {1, 2, 3, 4, 5, 6}
rank_no = {3, 5, 7, 6, 8, 9, 13}
num = roll_no.symmetric_difference(rank_no)
print(num)
print(type(num))


