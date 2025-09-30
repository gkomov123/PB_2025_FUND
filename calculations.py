operator_input = input()
first_num = int(input())
second_num = int(input())


def add(num1:int, num2:int):
    return num1 + num2

def subtract(num1:int, num2:int):
    return num1 - num2

def multiply(num1:int, num2:int):
    return num1 * num2

def divide(num1:int, num2:int):
    return int(num1 / num2)

def calculated(operator:str, num1:int, num2:int) -> int:
    if operator == "add":
       return add(num1, num2)
    elif operator == "subtract":
       return subtract(num1, num2)
    elif operator == "multiply":
        return multiply(num1, num2)
    elif operator == "divide":
       return divide(num1, num2)

print(calculated(operator_input, first_num, second_num))