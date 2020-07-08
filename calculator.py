"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


"""Creating a function for a calculator"""

while True:
    input_string = input("Your equation?")
    tokens = input_string.split(' ')

    if "q" in tokens:
        print("Calculator exiting.")
        break

    symbol = tokens[0]
    num1 = tokens[1]

    if len(tokens) == 3:
        num2 = tokens[2]

    if len(tokens) > 3:
        num3 = tokens[3]

    answer = None

    if symbol == '+':
        answer = add(int(num1), int(num2))

    elif symbol == '-':
        answer = subtract(int(num1), int(num2))

    elif symbol == '*': 
        answer = multiply(int(num1), int(num2))

    elif symbol == '/': 
        answer = divide(int(num1), int(num2))

    elif symbol == 'square': 
        answer = square(int(num1))

    elif symbol == 'cube': 
        answer = cube(int(num1))

    elif symbol == 'pow': 
        answer = power(int(num1), int(num2))

    elif symbol == 'mod': 
        answer = mod(int(num1), int(num2))

    print(answer)
