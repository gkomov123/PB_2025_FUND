def is_perfect_number(number):
    divisors = []
    for divisor in range(1, number):
        if number % divisor == 0:
            divisors.append(divisor)
    if sum(divisors) == number:
        return "We have a perfect number!"
    return "It's not so perfect."


number_input = int(input())
print(is_perfect_number(number_input))