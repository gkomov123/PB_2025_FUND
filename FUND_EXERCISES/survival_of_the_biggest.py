# map() and min() not used to practice basic loops and list looping

numbers_as_string = input().split()
numbers_to_remove = int(input())
numbers_as_integer = []

for number in numbers_as_string: #Iterate and convert from string to integer
    numbers_as_integer.append(int(number))

for _ in range(numbers_to_remove): # Removal interations
    #smallest = min(numbers_as_integer) can be used to simplify
    smallest = numbers_as_integer[0]
    for num in numbers_as_integer: # Iterate thru the numbers list
        if num < smallest:
            smallest = num # if smaller become the smallest number
    numbers_as_integer.remove(smallest) # remove the smallest number

survival_numbers = []
for number in numbers_as_integer: #convert back to string list to use .join
    survival_numbers.append(str(number))

print(", ".join(survival_numbers)) #print the survived numbers