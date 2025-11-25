def move(message: str, some_command: list) -> str:
    number_of_letters = int(some_command[1])
    message = message[number_of_letters:] + message[0:number_of_letters]
    return message


def insert(message: str, some_command: list) -> str:
    index, value = int(some_command[1]), some_command[2]
    message = message[0:index] + value + message[index:]
    return message


def change_all(message: str, some_command: list) -> str:
    substring, replacement = some_command[1], some_command[2]
    message = message.replace(substring, replacement)
    return message


encrypted_message = input()
command = input()
while command != 'Decode':
    command = command.split('|')
    action = command[0]
    if action == 'Move':
        encrypted_message = move(encrypted_message, command)
    elif action == 'Insert':
        encrypted_message = insert(encrypted_message, command)
    elif action == 'ChangeAll':
        encrypted_message = change_all(encrypted_message, command)

    command = input()

print(f'The decrypted message is: {encrypted_message}')
