word_input = input().split()

words = [word for word in word_input if len(word) % 2 == 0]

for i in words:
    print(i)
