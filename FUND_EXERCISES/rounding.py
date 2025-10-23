numbers_list = input().split()

rounded_nums = []

for num in numbers_list:
    rounded_nums.append(round(float(num)))

print(rounded_nums)