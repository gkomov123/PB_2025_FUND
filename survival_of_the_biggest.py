numbers_as_string = input().split()
numbers_to_remove = int(input())
numbers_as_integer = []

for number in numbers_as_string: #Iterate and convert from string to integer
    numbers_as_integer.append(int(number))

for _ in range(numbers_to_remove): # Removal interations
    #smallest = min(numbers_as_integer)
    smallest = numbers_as_integer[0]
    for num in numbers_as_integer: # Iterate thru the numbers list
        if num < smallest: # check if the current number  is smaller than variable smallest->0
            smallest = num # if smaller become the smallest number
    numbers_as_integer.remove(smallest) # remove the smallest number

survival_numbers = []
for number in numbers_as_integer:
    survival_numbers.append(str(number))

print(", ".join(survival_numbers))