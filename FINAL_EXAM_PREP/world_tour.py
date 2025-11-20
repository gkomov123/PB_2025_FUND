def add_stop(some_string: str, some_command: list) -> str:
    insert_index = int(some_command[1])
    insert_string = some_command[2]
    before_string = some_string[:insert_index]
    after_string = some_string[insert_index:]
    if 0 <= insert_index <= len(some_string):
        some_string = before_string + insert_string + after_string

    return some_string


def remove_stop(some_string: str, some_command: list) -> str:
    start_index = int(some_command[1])
    end_index = int(some_command[2])
    if start_index <= len(some_string) and end_index <= len(some_string) - 1:
        some_string = some_string[:start_index] + some_string[end_index + 1:]

    return some_string


def switch(some_string: str, some_command: list) -> str:
    old_string = some_command[1]
    new_string = some_command[2]

    if old_string in some_string:
        some_string = some_string.replace(old_string, new_string)

    return some_string


string_to_manipulate = input()
command = input()
while command != 'Travel':
    command = command.split(':')
    action = command[0]

    if action == 'Add Stop':
        string_to_manipulate = add_stop(string_to_manipulate, command)
        print(string_to_manipulate)

    elif action == 'Remove Stop':
        string_to_manipulate = remove_stop(string_to_manipulate, command)
        print(string_to_manipulate)

    elif action == 'Switch':
        string_to_manipulate = switch(string_to_manipulate, command)
        print(string_to_manipulate)

    command = input()

print(f"Ready for world tour! Planned stops: {string_to_manipulate}")
