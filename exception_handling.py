try:
    age = int(input("enter your age :"))
    print("given age is :", age)
    if age <= 0:
        print("enter the valid age")
    elif age > 18:

        print("your eligible for voting:")

    elif age < 18:

        print("wait few more years")
except ValueError:
    print("oops", "ege must be in number")

finally:
    print("Thank you")
