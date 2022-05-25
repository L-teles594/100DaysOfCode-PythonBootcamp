from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return 'There is no division for 0'
    return n1 / n2


def calculator():
    operation = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    num1 = float(input("What's the first number?: "))
    while True:
        for ops in operation:
            print(ops)

        calc = input('Pick an operation: ')
        num2 = float(input("What's the next number?: "))
        result = operation[calc](num1, num2)
        print(f'{num1} {calc} {num2} = {result}')

        if result == 'There is no division for 0':
            break
        if input(f'Type "y" to continue calculating with {result} or type "n" to exit.: ').lower()[0] == 'y':
            num1 = result
        else:
            if input('Do you want to use the calculator again?: "y" or "n" \n').lower()[0] == 'n':
                break
            calculator()


print(logo)
calculator()

