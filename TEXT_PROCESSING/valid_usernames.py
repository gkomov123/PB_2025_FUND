def length_check(string: str) -> bool:
    if 3 <= len(string) <= 16:
        return True
    return False


def symbol_check(string: str) -> bool:
    valid_symbol = True
    for symbol in string:
        if not (symbol.isalnum() or symbol == "-" or symbol == "_"):
            valid_symbol = False
            break
    return valid_symbol


def redundant_check(string: str) -> bool:
    if " " not in string:
        return True
    return False


def username_validation(users: list) -> list:
    valid_users = []
    for user in users:
        if length_check(user) and symbol_check(user) and redundant_check(user):
            valid_users.append(user)
    return valid_users


usernames_input = input().split(", ")
valid_usernames = username_validation(usernames_input)

print("\n".join(valid_usernames))

# for username in valid_usernames:
#     print(username)
