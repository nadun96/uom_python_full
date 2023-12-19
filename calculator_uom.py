# TODO: Write the functions for arithmatic operations here
# These functions should cover Task 2
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1 / num2
    except Exception as e:
        print(e)


def power(num1, num2):
    return num1**num2


def remainder(num1, num2):
    return num1 % num2


# -------------------------------------
# TODO: Write the select_op(choice) function here
# This function sould cover Task 1 (Section 2) and Task 3
def select_op(choice):

    if choice == '#':
        return -1

    elif choice == '$':
        return 0

    elif (choice in ('+', '-', '*', '/', '^', '%')):

        while True:
            num1 = str(input("Enter first number: "))
            print(num1)
            if num1.endswith('$'):
                return 0
            if num1.endswith('#'):
                return -1
            try:
                x = float(num1)
                break
            except Exception as e:
                print("Not A vlalid Number , Try Again")
                continue

        while True:
            num2 = str(input("Enter second number: "))
            print(num2)
            if num2.endswith('$'):
                return 0
            if num2.endswith('#'):
                return -1
            try:
                y = float(num2)
                break
            except Exception as e:
                print("Not A vlalid Number , Try Again")
                continue

    if choice == '+':
        print(x, "+", y, "=", add(x, y))

    if choice == '-':
        print(x, "-", y, "=", subtract(x, y))

    if choice == '*':
        print(x, "*", y, "=", multiply(x, y))

    if choice == '/':
        print(x, "/", y, "=", divide(x, y))

    if choice == '^':
        print(x, "^", y, "=", power(x, y))

    if choice == '%':
        print(x, "%", y, "=", remainder(x, y))


# End the select_op(choice) function here
# -------------------------------------
# This is the main loop. It covers Task 1 (Section 1)
# YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)

    if (select_op(choice) == -1):
        # program ends here
        print("Done. Terminating")
        exit()
