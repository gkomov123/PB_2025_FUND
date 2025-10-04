def is_perfect_number(number):
    divisors_sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            divisors_sum += divisor
    if divisors_sum == number:
        return "We have a perfect number!"
    return "It's not so perfect."


number_input = int(input())
print(is_perfect_number(number_input))