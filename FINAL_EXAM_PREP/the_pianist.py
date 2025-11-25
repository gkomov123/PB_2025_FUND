def add_piece(pieces_dict: dict, some_command: list) -> dict:
    piece_to_add, composer_to_add, key_to_add = some_command[1], some_command[2], some_command[3]
    if piece_to_add in pieces_dict.keys():
        print(f'{piece_to_add} is already in the collection!')
        return pieces_dict
    pieces_dict[piece_to_add] = {'composer': composer_to_add, 'key': key_to_add}
    print(f'{piece_to_add} by {composer_to_add} in {key_to_add} added to the collection!')
    return pieces_dict


def remove_piece(pieces_dict: dict, some_command: list) -> dict:
    piece_to_remove = some_command[1]
    if piece_to_remove in pieces_dict.keys():
        del pieces_dict[piece_to_remove]
        print(f'Successfully removed {piece_to_remove}!')
        return pieces_dict
    print(f'Invalid operation! {piece_to_remove} does not exist in the collection.')
    return pieces_dict


def change_key(pieces_dict: dict, some_command: list) -> dict:
    piece_to_change, new_key = some_command[1], some_command[2]
    if piece_to_change in pieces_dict.keys():
        pieces_dict[piece_to_change]['key'] = new_key
        print(f'Changed the key of {piece_to_change} to {new_key}!')
        return pieces_dict
    print(f'Invalid operation! {piece_to_change} does not exist in the collection.')
    return pieces_dict


number_of_pieces = int(input())
pieces = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split('|')
    pieces[piece] = {'composer': composer, 'key': key}

command = input()
while command != 'Stop':
    command = command.split('|')
    action = command[0]

    if action == 'Add':
        pieces = add_piece(pieces, command)
    elif action == 'Remove':
        pieces = remove_piece(pieces, command)
    elif action == 'ChangeKey':
        pieces = change_key(pieces, command)

    command = input()

for piece, piece_details in pieces.items():
    print(f'{piece} -> Composer: {piece_details["composer"]}, Key: {piece_details["key"]}')
