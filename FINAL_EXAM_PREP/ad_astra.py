import re

regex = r'(#|\|)([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'
food_string = input()

foods_info = re.findall(regex, food_string)

total_food_cals = 0
total_food_cals += sum([int(current_food[3]) for current_food in foods_info])
days_can_last = total_food_cals // 2000
print(f"You have food to last you for: {days_can_last} days!")
for current_food in foods_info:
    food_name = current_food[1]
    food_exp_date = current_food[2]
    food_cals = current_food[3]
    print(f"Item: {food_name}, Best before: {food_exp_date}, Nutrition: {food_cals}")
