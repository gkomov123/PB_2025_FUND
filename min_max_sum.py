numbers_as_string = input().split()
numbers_as_integer = []
for number in numbers_as_string:
    numbers_as_integer.append(int(number))

print(f"The minimum number is {min(numbers_as_integer)}"
      f"\nThe maximum number is {max(numbers_as_integer)}"
      f"\nThe sum number is: {sum(numbers_as_integer)}")