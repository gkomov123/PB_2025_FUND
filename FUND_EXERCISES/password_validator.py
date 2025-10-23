def check_lenght(password:str):
    if 6 <= len(password) <= 10:
        return None
    return "Password must be between 6 and 10 characters"


def check_letters_and_digits(password:str):
    if password.isalnum():
        return None
    return "Password must consist only of letters and digits"


def check_two_digits(password:str):
    count = 0
    for char in password:
        if char.isdigit():
            count += 1
    if count >= 2:
        return None
    return "Password must have at least 2 digits"


def is_pass_valid(password:str) -> list:
    is_valid = []
    is_valid.append(check_lenght(password))
    is_valid.append(check_letters_and_digits(password))
    is_valid.append(check_two_digits(password))

    for string in range(len(is_valid) - 1, - 1, -1):
        if is_valid[string] == None:
            is_valid.pop(string)
    return is_valid
  
    
password_input = input()
password_is_not_valid = is_pass_valid(password_input)
if password_is_not_valid:
    print("\n".join(password_is_not_valid))
else:
    print("Password is valid")