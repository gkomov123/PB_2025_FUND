numbers = [int(num) for num in input().split(", ")]

indeces = map(
    lambda x: x if numbers[x] % 2 == 0 else "no",
    range(len(numbers))
)

even_indeces = [index for index in indeces if index != "no"]

print(even_indeces)