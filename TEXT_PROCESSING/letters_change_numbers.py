strings_list = input().split()

total_sum = 0

for string in strings_list:
    first_letter = string[0]
    last_letter = string[-1]
    current_number = int(string[1:-1])
    # First letter is Uppercase
    if first_letter.isupper():
        current_number /= (ord(first_letter) - 64)
    # First letter is LowerCase
    elif first_letter.islower():
        current_number *= (ord(first_letter) - 96)

    # Last letter is Uppercase
    if last_letter.isupper():
        current_number -= (ord(last_letter) - 64)
    # Last letter is LowerCase
    elif last_letter.islower():
        current_number += (ord(last_letter) - 96)
    total_sum += current_number

print(f"{total_sum:.2f}")
