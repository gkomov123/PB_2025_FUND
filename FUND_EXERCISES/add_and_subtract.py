def subtract(first_integer:int, second_integer:int) -> int:
    return first_integer - second_integer


def sum_numbers(number_first:int, number_second:int) -> int:
    return number_first + number_second


def add_and_subtract(num1:int, num2:int, num3:int) -> int:
    sum_result = sum_numbers(num1, num2)
    subtract_result = subtract(sum_result, num3)
    return subtract_result


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))
