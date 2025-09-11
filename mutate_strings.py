first_string = input()
second_string = input()

for char_index in range(len(first_string)):
    left_part = second_string[: char_index + 1]
    right_part = first_string[char_index + 1:]
    new_string = left_part + right_part
    if first_string[char_index] != second_string[char_index]:
        print(new_string)
