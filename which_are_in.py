first_strings = input().split(", ")
second_strings = input().split(", ")

filtered = [word for word in first_strings if any(word in word2 for word2 in second_strings)]

print(filtered)