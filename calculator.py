"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


def calculator():

    while True:
        input_string = input("Your equation?")
        tokens = input_string.split(' ')
        symbol = tokens[0]

        if tokens[0] == "q":
            print("Calculator exiting.")
            break

        if symbol == '+':
            answer = add(num1, num2)

return answer


calculator()
