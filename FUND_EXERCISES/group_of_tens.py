numbers = [int(num) for num in input().split(", ")]

current_group = 10


while numbers:
    current_group_list = [num for num in numbers if num <= current_group]
    print(f"Group of {current_group}'s: {current_group_list}")
    numbers = [num for num in numbers if num not in current_group_list]
    current_group += 10


