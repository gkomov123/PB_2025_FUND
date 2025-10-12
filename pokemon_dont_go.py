distance_to_pokemon = [int(num) for num in input().split()]
captured_pokemons = []

while distance_to_pokemon:
    pokemon_index = int(input())  # input for the pokemon index

    element_to_remove = 0

    if pokemon_index < 0:
        element_to_remove = distance_to_pokemon[0]
        replacement_value = distance_to_pokemon[-1]
        distance_to_pokemon[0] = replacement_value
        distance_to_pokemon.pop(0)
    elif pokemon_index >= len(distance_to_pokemon):
        element_to_remove = distance_to_pokemon[-1]
        replacement_value = distance_to_pokemon[0]
        distance_to_pokemon[-1] = replacement_value
        distance_to_pokemon.pop()
    else:
        element_to_remove = distance_to_pokemon.pop(pokemon_index)

    captured_pokemons.append(element_to_remove)

    for i in range(len(distance_to_pokemon)):
        if distance_to_pokemon[i] <= element_to_remove:
            distance_to_pokemon[i] += element_to_remove
        if distance_to_pokemon[i] > element_to_remove:
            distance_to_pokemon[i] -= element_to_remove

print(sum(captured_pokemons))
