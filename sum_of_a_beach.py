beach_word = input()

def count_beach_words(text):

    lower_text = beach_word.lower()

    target_words = ["sand", "water", "fish", "sun"]

    word_counts = {}

    for word in target_words:
        word_counts[word] = lower_text.count(word)

    return word_counts

counts = count_beach_words(beach_word)
print(sum(counts.values()))





#word_counter = 0


#if "sand" in beach_word:
#    word_counter += 1
#if "water" in beach_word:
#    word_counter += 1
#if "fish" in beach_word:
#    word_counter += 1
#if "sun" in beach_word:
#    word_counter += 1

#print(word_counter)