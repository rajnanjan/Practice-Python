""" lambda
syntax  lambda<arguments OR sequence >: expression"""

num = lambda x: x * 25

print(num)
print("sum", num(20))

# using lambda with map
nums = [1, 3, 4, 5, 6, 7, 8]

multi_num = map(lambda x: x * 2, nums)
print(multi_num)
for i in multi_num:
    print(i, end=" ")




