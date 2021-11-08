# n1 = 10
# n2 = 5
#
#
# if n1 == n2:
#     print("n1 and n2 are equal")
# else:
#     print("n1 and n2 are not equal")
#
# print("Hello world")
#
# else:
#     print("n1 and n2 are not equal")
'''  practice problems '''
''' Q1 - Write a program to check whether a number entered by user is even or odd.
  ans '''
#
# num = int(input("enter the number : "))
#
# if num%2==0:
#     print("given number is even")
# else :
#     print("given number is Add")

'''Q2 - Write a program to check whether a number is divisible by 7 or not.'''

num = int(input("enter the value : "))

if num % 7 == 0:
    print("given number is divisible by 7")
else:
    print("given number is not divisible by 7")

'''Q3-Write a program to display "Hello" if a number entered by user is a multiple of five , 
otherwise print "Bye".'''

num = int(input("enter any number : "))

if num % 5 == 0:
    print("hello")
else:
    print("bye")

'''Q4. Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
             Unit                                                     Price  
First 100 units                                               no charge
Next 100 units                                              Rs 5 per unit
After 200 units                                             Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)'''

amount = 0
units = int(input("Enter the total number of units : "))

if units>200:
    amount = units * 10

elif units > 100:
    amount = units * 5
    print(amount)

else:
    print("no charge its free of cost ")
 # after seeing answer
amount = 0
units = int(input("enter the usages unit :"))
if units <=100:
    print("its a free of coast")
elif 100 < units <= 200:
    amount = (units - 100) * 5
    print("your bill amount is :", amount)
elif units > 200:
    amount = (units - 200) * 10 + 500
    print("your bill amount is:", amount)
'''5,Write a program to display the last digit of a number.'''

# num=int(input("enter the number : "))
# print("last digit number is :",num%10)

'''6 ,Write a program to check whether the last digit of a number( entered by user ) is 
divisible by 3 or not.'''

# num = int(input("enter the number : "))
# last_digit = num % 10

# if last_digit%3==0:
#     print("the last digit number is divisible by 3.")
# else:
#     print("the last digit number is not divisible by3.")
'''7,Write a program to accept percentage from the user and display the grade according to the following criteria:

         Marks                                    Grade
         > 90                                       A
         > 80 and <= 90                             B
         >= 60 and <= 80                            C
         below 60                                   D '''

# marks = int(input("enter yours marks : "))
# if marks < 60:
#     print("your grade was D")
# elif 60 <= marks <= 80:
#     print("your grade was C")
# elif 80 < marks <= 90:
#     print("your grade was B")
# elif marks>90:
#     print("your grade was A")
