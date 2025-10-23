rooms = input().split("|")

MAX_HEALTH = 100

# Counters
bitcoins = 0
current_health = 100
dead = False
room_counter = 0

for room in rooms:
    split_command = room.split()  # command -> room[0], amount -> room[1]
    command = split_command[0]
    amount = int(split_command[1])
    room_counter += 1

    if command == "potion":
        before_hp = current_health
        current_health += amount
        if current_health > MAX_HEALTH:
            current_health = MAX_HEALTH
        healed_amount = current_health - before_hp
        print(f"You healed for {healed_amount} hp.")
        print(f"Current health: {current_health} hp.")
    elif command == "chest":
        bitcoins += amount
        print(f"You found {amount} bitcoins.")
    else:
        current_health -= amount
        if current_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_counter}")
            dead = True
            break

if not dead:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {current_health}")
