number_of_lines = int(input())
tank_capacity = 255

for lines in range(number_of_lines):
    liters_water = int(input())
    if tank_capacity < liters_water:
        print("Insufficient capacity!")
        continue
    tank_capacity -= liters_water
else:
    print(255 - tank_capacity)