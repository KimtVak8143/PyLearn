# Concept of Try and Except

try:
    value = 10/0   # triggers ZeroDivision error
    number = int(input("Enter a number"))
    print(number)
except ZeroDivisionError as err:
    # print("Division by zero")
    print(err)
except ValueError as ve:
    # print("Invalid input")
    print(ve)

