""" 1. Write a Python program to calculate the length of a string. """
#
# name = input("enter the name :")
# print("The length of Name :", len(name))

""" 2. Write a Python program to count the number of characters (character frequency) in a string. 
Sample String : google.com 
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1} """

# sample_string = input("Enter the Name :")
# dic = {}
# for ch in sample_string:
#     if ch in dic:
#         dic[ch] += 1
#     else:
#         dic[ch] = 1
# print(dic)

# """ 3. Write a Python program to get a string from a given string where all occurrences of
# its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'"""
#
# name = input("Enter the name :")
# dic = list(name)
# for ch in name:
#     if ch in dic:
#         dic.replace(ch, "$")
# print(dic)
""" 4. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
given string is less than 3, leave it unchanged. 
Sample String : 'abc' 
Expected Result : 'abcing' 
Sample String : 'string' 
Expected Result : 'stringly'"""

# name = input("Enter the word :")
# if len(name) > 2:
#     if name[-3:] == "ing":
#         name += "ly"
#     else:
#         name += "ing"

""" 5. Write a Python function that takes a list of words and returns the length of the longest one."""
# names = ["raj", "siddaraj", "manoj", "mani", "sachinlokesh", "ramkrishnabalasubramanyan"]
# len_names = []
# for name in names:
#     len_names.append(len(name))
# len_names.sort()
# print(len_names)
# print("the longest one:", len_names[-1])

""" 6. Write a Python script that takes input from the user and displays 
that input back in upper and lower cases."""

name = input("Enter the name :")
print("Given name is upper case :", name.upper())
print("given name is lower case :", name.lower())







