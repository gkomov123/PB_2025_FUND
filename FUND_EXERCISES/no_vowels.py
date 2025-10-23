word_input = input()
vowels = ["a", "o", "u", "e", "i"]

filtered = [letter for letter in word_input if letter.lower() not in vowels]

print("".join(filtered))