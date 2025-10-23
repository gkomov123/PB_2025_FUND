def even_numbers(numbers:list) -> list:
    even = []
    for number in numbers:
        if int(number) % 2 == 0:
            even.append(int(number))
    return even


number_input = input().split()
print(even_numbers(number_input))