PEOPLE_PER_WAGON = 4


def lift_manager(people, lift_state):
    for index, wagon in enumerate(lift_state):
        if wagon < PEOPLE_PER_WAGON <= people:
            lift_state[index] += PEOPLE_PER_WAGON - wagon
            people -= PEOPLE_PER_WAGON - wagon
        elif wagon < PEOPLE_PER_WAGON and people < PEOPLE_PER_WAGON:
            lift_state[index] += people
            people = 0

    if people > 0:
        message = f"There isn't enough space! {people} people in a queue!"
    elif any(wagon < 4 for wagon in lift_state):
        message = f"The lift has empty spots!"
    else:
        message = ''

    return message, lift_state


def main():
    people_waiting = int(input())
    current_lift_state = [int(seat) for seat in input().split()]
    result_message, lift_state_list = lift_manager(people_waiting, current_lift_state)
    if result_message != "":
        print(result_message)
    print(*lift_state_list, sep=' ')


main()
