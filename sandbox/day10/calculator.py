import art

import calculator_functions

print(art.logo)

num1 = float(input("What's the first number? "))

operations = calculator_functions.operations

for symbol in operations:
    print(symbol)

should_continue = True

while should_continue:

    operation_symbol = input("Pick an operation: ")

    while operation_symbol not in operations:
        operation_symbol = input("Pick a valid operation from the list: ")

    num2 = float(input("What's the next number? "))

    operation = operations[operation_symbol]

    result = operation(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {result}")

    next_step = input(
        f"Type 'y' to continue to calculating with {result}, type 'n' to input a new number, or type 'exit' to "
        f"exit: ")

    if next_step == 'y':
        num1 = result
    elif next_step == 'n':
        num1 = int(input("What's the first number? "))
    else:
        should_continue = False
