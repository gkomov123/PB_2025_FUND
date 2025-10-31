string = input()
chars = {}

for char in string:
    if char != " ":
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1

for char, occurence in chars.items():
    print(f"{char} -> {occurence}")
