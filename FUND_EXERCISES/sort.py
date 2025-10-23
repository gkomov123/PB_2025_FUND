number_input = input().split()
integer_conversion = []

for number in number_input:
    integer_conversion.append(int(number))

print(sorted(integer_conversion))