numbers = input().split()
opposite_numbers = []

for number in numbers:
    opposite = -int(number)
    opposite_numbers.append(opposite)

print(opposite_numbers)