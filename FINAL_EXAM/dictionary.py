words_dict = {}
words_and_def_input = input().split(' | ')

for current_word in words_and_def_input:
    if ':' in current_word:
        word, definition = current_word.split(': ')
        if word not in words_dict.keys():
            words_dict[word] = []
        words_dict[word].append(definition)

test_words = input().split(' | ')
command = input()

if command == 'Test':
    for word in test_words:
        if word in words_dict.keys():
            print(f'{word}:')
            for definition in words_dict[word]:
                print(f' -{definition}')
elif command == 'Hand Over':
    print(f'{" ".join(words_dict.keys())}')
