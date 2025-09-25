coins_as_string = input().split(", ")
number_of_beggars = int(input())
coins_as_integer = []

for coin in coins_as_string:
    coins_as_integer.append(int(coin))

sum_of_coins = []
start_index = 0
for beggar in range(number_of_beggars):
    current_coins_sum = 0
    for index in range(start_index, len(coins_as_integer), number_of_beggars):
        current_coins_sum += coins_as_integer[index]
    sum_of_coins.append(current_coins_sum)
    start_index += 1
print(sum_of_coins)