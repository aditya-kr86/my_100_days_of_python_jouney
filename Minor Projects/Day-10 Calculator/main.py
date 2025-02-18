from calc_art import calculator_img
import os
# Add
def add(n1,n2):
    return n1 + n2

# Substract
def substract(n1,n2):
    return n1 - n2

# Multiply
def multiply(n1,n2):
    return n1 * n2

# Division
def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

repeatation = True

def calculator():
    print(calculator_img)
    num1 = float(input("What's the first number? : "))
    while(repeatation):
        for operator in operations:
            print(operator)
        operation_symbol = input("Pick an Operation from the line above: ")

        num2 = float(input("What's the second number? : "))
        function = operations[operation_symbol]
        answer = function(num1,num2)
        print(f'''
 _____________________
|  _________________  |
| |       {answer:10.2f}| |
| |_________________| |
|_____________________|
''')
        # print(f"{num1} {operation_symbol} {num2} = {answer}")
        again_chioce = input(f"Type 'y' to continue calculating with {answer},or type'n' to start a new Calculation: ")
        if again_chioce == 'y':
            num1 = answer
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            calculator()

calculator()

