routes = input().split("||")
fuel_amount = int(input())
ammunition_amount = int(input())

for route in routes:
    command_split = route.split()
    command = command_split[0]

    if command == "Travel":
        light_years = int(command_split[1])
        if fuel_amount >= light_years:
            fuel_amount -= light_years
            print(f"The spaceship travelled {light_years} light-years.")
        else:
            print("Mission failed.")
            break

    elif command == "Enemy":
        enemy_armour = int(command_split[1])
        if ammunition_amount >= enemy_armour:
            ammunition_amount -= enemy_armour
            print(f"An enemy with {enemy_armour} armour is defeated.")
        elif fuel_amount >= (enemy_armour * 2):
            fuel_amount -= enemy_armour * 2
            print(f"An enemy with {enemy_armour} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break

    elif command == "Repair":
        fuel_and_ammo_added = int(command_split[1])
        fuel_amount += fuel_and_ammo_added
        ammunition_amount += fuel_and_ammo_added * 2
        print(f"Ammunitions added: {fuel_and_ammo_added * 2}.")
        print(f"Fuel added: {fuel_and_ammo_added}.")

    elif command == "Titan":
        print(f"You have reached Titan, all passengers are safe.")
        break
