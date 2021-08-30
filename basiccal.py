# Basic Calculator
# Imports
from cmath import sqrt

# Choice list
choice_list = ["Addition", "Subtraction", "Divide", "Multiply", "Power/Exponent", "Square", "Cube", "Square Root"]


# Menu Card
def make_choice():
    print("Menu Card :\n")
    print(" 1. Add\n 2. Subtract\n 3. Divide\n 4. Multiply\n 5. Power/Exponent")
    print(" 6. Square\n 7. Cube\n 8. Square Root\n")

    choice = int(input("Enter your choice :\t"))
    while choice == 0 or choice > 7:
        print("Enter a Valid choice :\t")
        choice = int(input())

    return choice


# Input for 2 Operands
def take_input():
    x = int(input("Enter First Number :\t"))
    y = int(input("Enter Second Number :\t"))
    return x, y


# Input for Single Operand
def single_input():
    x = int(input("Enter the Number :\t"))
    return x


# Single Operand Operation
def single(c, p):
    if c == 6:
        result = p*p
    elif c == 7:
        result = p*p*p
    else:
        result = sqrt(p)
    return result


# Double Operand Operation
def select(c, p, q):
    if c == 1:
        result = p+q
    elif c == 2:
        result = abs(p-q)
    elif c == 3:
        result = p/q
    elif c == 4:
        result = p*q
    else:
        result = pow(p, q)
    return result


def main():
    c = make_choice()
    if 0 < c <= 5:
        p, q = take_input()
        print("The result for {} is : {}".format(choice_list[c-1], select(c, p, q)))
    else:
        p = single_input()
        print("The result for {} is : {}".format(choice_list[c-1], single(c, p)))


if __name__ == '__main__':
    main()
