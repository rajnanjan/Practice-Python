# file_obj = open('abc.txt', 'r')
#
# print(file_obj.readlines())
#
# file_obj.close()
#
# file_obj = open('abc.txt', 'a')
#
# file_obj.write('Hello World')
#
# file_obj.close()
#
# file_obj = open('abc.txt', 'r')
#
# print(file_obj.readlines())
#
# file_obj.close()
#

with open('abc.txt', 'r') as f:
    print(f.readlines())



