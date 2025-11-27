def plunder(cities_dict: dict, some_command: list) -> dict:
    town, people, gold = some_command[1], int(some_command[2]), int(some_command[3])
    cities_dict[town]['population'] -= people
    cities_dict[town]['gold'] -= gold
    print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
    if cities_dict[town]['population'] <= 0 or cities_dict[town]['gold'] <= 0:
        del cities_dict[town]
        print(f'{town} has been wiped off the map!')
        return cities_dict
    return cities_dict


def prosper(cities_dict: dict, some_command: list) -> dict:
    town, gold = some_command[1], int(some_command[2])

    if gold < 0:
        print('Gold added cannot be a negative number!')
        return cities_dict
    cities_dict[town]['gold'] += gold
    print(f'{gold} gold added to the city treasury. {town} now has {cities_dict[town]["gold"]} gold.')
    return cities_dict


cities = {}

command = input()
while command != 'Sail':
    command = command.split('||')
    city_name, population, gold_amount = command[0], int(command[1]), int(command[2])
    if city_name in cities.keys():
        cities[city_name]['population'] += population
        cities[city_name]['gold'] += gold_amount
    else:
        cities[city_name] = {'population': population, 'gold': gold_amount}

    command = input()

command = input()
while command != 'End':
    command = command.split('=>')
    action = command[0]

    if action == 'Plunder':
        cities = plunder(cities, command)
    elif action == 'Prosper':
        cities = prosper(cities, command)

    command = input()

if cities:
    count = len(cities)
    print(f'Ahoy, Captain! There are {count} wealthy settlements to go to:')
    for city, city_details in cities.items():
        print(f'{city} -> Population: {city_details["population"]} citizens, Gold: {city_details["gold"]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
