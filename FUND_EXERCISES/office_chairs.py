rooms = int(input())


messages_to_output = []
total_free_chairs = 0

for room in range(rooms):
    chairs_and_visitors = input().split()
    free_chairs = chairs_and_visitors[0]
    visitiors = chairs_and_visitors[1]
    chair_difference = len(free_chairs) - int(visitiors)
    if chair_difference < 0:
        messages_to_output.append(f"{abs(chair_difference)} more chairs needed in room {room + 1}")
    else:
        total_free_chairs += chair_difference

if messages_to_output:
    for message in messages_to_output:
        print(message)
else:
    print(f"Game On, {total_free_chairs} free chairs left")

