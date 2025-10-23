animal = input().split(", ")

wolf_index = animal.index("wolf")

if wolf_index == len(animal) - 1:
    print("Please go away and stop eating my sheep")
else:
    sheep_number = len(animal) - wolf_index -1
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")