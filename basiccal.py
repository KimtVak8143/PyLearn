# Basic Calculator

def addition(a, b):
    return a + b


def subtraction(a, b):
    return abs(a-b)


def multiply(a, b):
    return a*b


def power(a, b):
    return pow(a, b)


def divide(a, b):
    return "{:2d}".format(a/b)


def make_choice():
    print("Menu Card :\n")
    print(" 1. Add\n 2. Subtract\n 3. Divide\n 4. Multiply\n 5. Power/Exponent")

    choice = int(input("Enter your choice :"))
    while choice == 0 or choice > 5:
        print("Enter a Valid choice")
        choice = int(input())

    return choice


def take_input():
    x = int(input("Enter First Number"))
    y = int(input("Enter Second Number"))
    return x, y


def select(c, p, q):
    if c == 1:
        result = addition(p, q)
    elif c == 2:
        result = subtraction(p, q)
    elif c == 3:
        result = divide(p, q)
    elif c == 4:
        result = multiply(p, q)
    else:
        result = power(p, q)
    return result


def main():
    c = make_choice()
    p, q = take_input()
    print("The result is : {}".format(select(c, p, q)))


if __name__ == '__main__':
    main()
