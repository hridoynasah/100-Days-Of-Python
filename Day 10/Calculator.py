import art
import os
import platform
def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
# Addition
def add(n1, n2):
    return n1 + n2

# Subtract
def sub(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Division
def division(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": division,
}

def Calculator():
    print(art.logo)
    num1 = float(input("What's the first number: "))
    is_Continue = True
    while is_Continue:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number: "))
        calculation_function1 = operations[operation_symbol]

        ans = calculation_function1(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {ans}")
        choice = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to exit.\nOr type 's' to start new calculation: ").lower()
        if choice == 'y':
            num1 = ans
            is_Continue = True
        elif choice == 's':
            clear_console()
            Calculator()
        elif choice == 'n':
            is_Continue = False

Calculator()