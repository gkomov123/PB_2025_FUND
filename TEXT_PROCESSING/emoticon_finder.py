string = input()

emoticons = []

for char in range(len(string)):
    if string[char] == ":":
        emoticon = string[char] + string[char + 1]
        emoticons.append(emoticon)

print("\n".join(emoticons))
