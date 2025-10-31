string = input()
chars = {}

for char in string:
    if char == " ":
        continue
    if char not in chars.keys():
        chars[char] = 0
    chars[char] += 1

for char, occurence in chars.items():
    print(f"{char} -> {occurence}")
