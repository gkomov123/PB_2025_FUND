number_of_electrons = int(input())

filled_shells = []
current_shell = 1

while number_of_electrons > 0:
    electrons_needed = 2 * current_shell ** 2
    if number_of_electrons > electrons_needed:
        number_of_electrons -= electrons_needed
        filled_shells.append(electrons_needed)
    else:
        filled_shells.append(number_of_electrons)
        break
    current_shell += 1


print(filled_shells)