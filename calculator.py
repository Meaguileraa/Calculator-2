"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


def calculator():
"""Creating a function for a calculator"""

    while True:
        input_string = input("Your equation?")
        tokens = input_string.split(' ')
        symbol = tokens[0]

        if tokens[0] == "q":
            print("Calculator exiting.")
            break

        if symbol == '+':
            answer = add(num1, num2)

        elif symbol == '-':
            answer = subtract(num1, num2)

        elif symbol == '*': 
            answer = multiply(num1, num2)

        elif symbol == '/': 
            answer = divide(num1, num2)

        elif symbol == '**': 
            answer = square(num1, num2)

        elif symbol == '*3': 
            answer = cube(num1, num2)

        elif symbol == '**': 
            answer = power(num1, num2)

        elif symbol == '%': 
            answer = mod(num1, num2)

return answer


calculator()
