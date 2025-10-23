def sum_of_even_and_odd(number:str) -> str:
    odd_sum = 0
    even_sum = 0
    for n in number:
        if int(n) % 2 == 0:
            even_sum += int(n)
        else:
            odd_sum += int(n)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"
        


number_input = input()
print(sum_of_even_and_odd(number_input))