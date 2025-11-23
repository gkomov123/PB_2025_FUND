def rate(plant_dict: dict, some_command: list) -> dict:
    plant, rating = command[1], command[3]
    plant_dict[plant]['ratings'].append(int(rating))
    return plant_dict


def update(plant_dict: dict, some_command: list) -> dict:
    plant, some_rarity = command[1], command[3]
    plant_dict[plant]['rarity'] = int(some_rarity)
    return plant_dict


def reset(plant_dict: dict, some_command: list) -> dict:
    plant = command[1]
    plant_dict[plant]['ratings'].clear()
    return plant_dict


number_of_plants = int(input())
plants = {}

for _ in range(number_of_plants):
    current_plant, rarity = input().split('<->')
    plants[current_plant] = {'rarity': rarity, 'ratings': []}

command = input()
while command != 'Exhibition':
    command = command.split()

    action = command[0]
    plant_name = command[1]

    if plant_name not in plants.keys():
        print('error')
    elif action == 'Rate:':
        plants = rate(plants, command)
    elif action == 'Update:':
        plants = update(plants, command)
    elif action == 'Reset:':
        plants = reset(plants, command)

    command = input()

print('Plants for the exhibition:')
for plant_name in plants.keys():
    plant_rarity = plants[plant_name]['rarity']
    if sum(plants[plant_name]['ratings']) != 0:
        average_rating = sum(plants[plant_name]['ratings']) / len(plants[plant_name]['ratings'])
    else:
        average_rating = 0
    print(f'- {plant_name}; Rarity: {plant_rarity}; Rating: {average_rating:.2f}')
