words_input = input().split()
words_dict = {}

for word in words_input:
    word_lower = word.lower()
    if word_lower not in words_dict:
        words_dict[word_lower] = 0
    words_dict[word_lower] += 1

for word, word_amount in words_dict.items():
    if word_amount % 2 != 0:
        print(word, end=" ")
