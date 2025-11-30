def make_lower(some_string: str, some_command: list) -> str:
    index = int(some_command[2])
    some_string_list = [letter for letter in some_string]
    letter = some_string_list.pop(index)
    some_string_list.insert(index, letter.lower())
    print(''.join(some_string_list))
    return ''.join(some_string_list)


def make_upper(some_string: str, some_command: list) -> str:
    index = int(some_command[2])
    some_string_list = [letter for letter in some_string]
    letter = some_string_list.pop(index)
    some_string_list.insert(index, letter.upper())
    print(''.join(some_string_list))
    return ''.join(some_string_list)


def insert(some_string: str, some_command: list) -> str:
    index, char = int(some_command[1]), some_command[2]
    some_string_list = [letter for letter in some_string]
    if index > len(some_string_list):
        return ''.join(some_string_list)
    some_string_list.insert(index, char)
    print(''.join(some_string_list))
    return ''.join(some_string_list)


def replace(some_string: str, some_command: list) -> str:
    char, value = some_command[1], int(some_command[2])
    if char not in some_string:
        return some_string
    replace_symbol = chr(ord(char) + value)
    some_string = some_string.replace(char, replace_symbol)
    print(some_string)
    return some_string


def validation(some_string: str) -> str:
    if len(some_string) < 8:
        print('Password must be at least 8 characters long!')
    if not all(letter.isalnum() or letter == '_' for letter in some_string):
        print('Password must consist only of letters, digits and _!')
    if not any(letter.isupper() for letter in some_string):
        print('Password must consist at least one uppercase letter!')
    if not any(letter.islower() for letter in some_string):
        print('Password must consist at least one lowercase letter!')
    if not any(letter.isdigit() for letter in some_string):
        print('Password must consist at least one digit!')
    return some_string


string_to_manipulate = input()

command = input()
while command != 'Complete':
    command = command.split()
    action = command[0]

    if action == 'Make':
        if command[1] == 'Lower':
            string_to_manipulate = make_lower(string_to_manipulate, command)
        elif command[1] == 'Upper':
            string_to_manipulate = make_upper(string_to_manipulate, command)
    elif action == 'Insert':
        string_to_manipulate = insert(string_to_manipulate, command)
    elif action == 'Replace':
        string_to_manipulate = replace(string_to_manipulate, command)
    elif action == 'Validation':
        string_to_manipulate = validation(string_to_manipulate)

    command = input()
