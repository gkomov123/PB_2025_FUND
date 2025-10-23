def find_greater_than_average(numbers):
    average = sum(numbers) // len(numbers)
    greater_numbers = []
    for number in numbers:
        if number > average:
            greater_numbers.append(number)
    while len(greater_numbers) > 5:
        lowest = min(greater_numbers)
        greater_numbers.remove(lowest)
    return sorted(greater_numbers, reverse=True)


def main():
    numbers_list = [int(n) for n in input().split()]
    result = find_greater_than_average(numbers_list)
    if not result:
        print("No")
    else:
        print(*result, sep=" ")


main()
