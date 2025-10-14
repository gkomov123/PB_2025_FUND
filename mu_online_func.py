MAX_HEALTH = 100


def fight_monster(monster, hp, attack_amount, room_number):
    hp -= attack_amount
    if hp <= 0:
        dead = True
        output = f"You died! Killed by {monster}."f"\nBest room: {room_number}"
    else:
        dead = False
        output = f"You slayed {monster}."
    return dead, hp, output


def chest(number_of_currency, amount_of_taken_currency):
    number_of_currency += amount_of_taken_currency
    return number_of_currency, f"You found {amount_of_taken_currency} bitcoins."


def heal(current_hp, potion_amount, max_hp):
    before_hp = current_hp
    current_hp += potion_amount
    if current_hp > max_hp:
        current_hp = max_hp
    healed_amount = current_hp - before_hp
    message = f"You healed for {healed_amount} hp."f"\nCurrent health: {current_hp} hp."
    return current_hp, healed_amount, message


def main():
    dead_status = False
    rooms = input().split("|")
    room_counter = 0
    current_health = MAX_HEALTH
    bitcoins = 0
    for room in rooms:
        split_command = room.split()  # command -> room[0], amount -> room[1]
        command = split_command[0]
        amount = int(split_command[1])
        room_counter += 1

        if command == "potion":
            current_health, healed_hp, heal_message = heal(current_health, amount, MAX_HEALTH)
            print(heal_message)
        elif command == "chest":
            bitcoins, loot_message = chest(bitcoins, amount)
            print(loot_message)
        else:
            dead_status, current_health, fight_message = fight_monster(command, current_health, amount, room_counter)
            print(fight_message)
            if dead_status:
                break

    if not dead_status:
        print("You've made it!")
        print(f"Bitcoins: {bitcoins}")
        print(f"Health: {current_health}")


main()
