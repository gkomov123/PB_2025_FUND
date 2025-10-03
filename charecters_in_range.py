def characters_in_between(first_symbol:str, second_symbol:str) -> list:
    symbols = []
    for symbol in range(ord(first_symbol) + 1, ord(second_symbol)):
        symbols.append(chr(symbol))
    return symbols

first_char = input()
second_char = input()
print(" ".join(characters_in_between(first_char, second_char)))