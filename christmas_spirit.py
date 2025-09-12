quantity_decorations = int(input())
remaining_days = int(input())

#Prices
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

total_price = 0
spirit = 0

for day in range(1, remaining_days + 1):

    if day % 11 == 0:
        quantity_decorations += 2

    if day % 2 == 0:
        total_price += ornament_set_price * quantity_decorations
        spirit += 5

    if day % 3 == 0:
            total_price += (tree_skirt_price + tree_garland_price) * quantity_decorations
            spirit += 3 + 10

    if day % 5 == 0:
        total_price += tree_lights_price * quantity_decorations
        spirit += 17
        if day % 3 == 0:
            spirit += 30

    if day % 10 == 0:
        spirit -= 20
        total_price += tree_garland_price + tree_lights_price + tree_skirt_price 

if remaining_days % 10 == 0:
     spirit -= 30


print(f"Total cost: {total_price}")

print(f"Total spirit: {spirit}")