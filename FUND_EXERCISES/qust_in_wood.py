def adventure_calculation(days, people, energy, water_per_day_person, food_per_day_person):
    total_food = days * people * food_per_day_person
    total_water = days * people * water_per_day_person
    for day in range(1, days + 1):
        energy_loss_daily = float(input())
        energy -= energy_loss_daily
        if energy <= 0:
            break
        if day % 2 == 0:
            energy += energy * 0.05
            total_water -= total_water * 0.30
        if day % 3 == 0:
            energy += energy * 0.10
            total_food -= total_food / people
    if energy <= 0:
        message = f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water."
    else:
        message = f"You are ready for the quest. You will be left with {energy:.2f} energy!"

    return message


def main():
    days_of_adventure = int(input())
    number_of_adventurers = int(input())
    energy_amount = float(input())
    water_per_person_per_day = float(input())
    food_per_person_per_day = float(input())
    result = adventure_calculation(days_of_adventure, number_of_adventurers, energy_amount, water_per_person_per_day,
                                   food_per_person_per_day)

    print(result)


main()
