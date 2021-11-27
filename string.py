""" 1. Write a Python program to calculate the length of a string. """
#
# name = input("enter the name :")
# print("The length of Name :", len(name))

""" 2. Write a Python program to count the number of characters (character frequency) in a string. 
Sample String : google.com 
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1} """

sample_string = input("Enter the Name :")
dic = {}
for ch in sample_string:
    if ch in dic:
        dic[ch] += 1
    else:
        dic[ch] = 1
print(dic)




