lost_fight_count = int(input())
helmet_price = float(input()) 
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_price = 0
shield_broken_count = 0

for loss in range(1, lost_fight_count + 1):
    if loss % 2 == 0:
        total_price += helmet_price
    if loss % 3 == 0:
        total_price += sword_price
        if loss % 2 == 0:
            total_price += shield_price
            shield_broken_count += 1
    if shield_broken_count == 2:
        total_price += armor_price
        shield_broken_count = 0
print(f"Gladiator expenses: {total_price:.2f} aureus" )
    

