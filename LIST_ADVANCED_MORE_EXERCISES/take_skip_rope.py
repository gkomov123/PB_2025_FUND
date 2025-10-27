string_input = input()  # skipTest_String044160
numbers = [int(num) for num in string_input if num.isdigit()]
chars = [char for char in string_input if not char.isdigit()]

take_list = numbers[::2]
skip_list = numbers[1::2]

result_string = ''

index = 0
for take, skip in zip(take_list, skip_list):
    result_string += "".join(chars[index: index + take])
    index += take + skip

print(result_string)
# print(numbers)
# print(chars)
# print(take_list)
# print(skip_list)
