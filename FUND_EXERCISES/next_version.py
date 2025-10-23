version_number_input = input().split(".")
new_number = []

nums = list(map(int, version_number_input))

for i in range(len(nums) - 1, -1, -1):
    nums[i] += 1
    if nums[i] == 10:
        nums[i] = 0
    else:
        break
print(".".join(map(str, nums)))
