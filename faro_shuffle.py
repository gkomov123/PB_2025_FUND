deck_of_cards = input().split()
shuffle_count = int(input())

for current_shuffle in range(shuffle_count):
    middle = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle]
    right_part = deck_of_cards[middle:]
    shuffled_deck = []
    for card_index in range(len(left_part)):
        shuffled_deck.append(left_part[card_index])
        shuffled_deck.append(right_part[card_index])
    deck_of_cards = shuffled_deck.copy()
print(deck_of_cards)
