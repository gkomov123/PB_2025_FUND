number_of_commands = int(input())
parking_dict = {}

for _ in range(number_of_commands):
    current_command = input().split()
    command, username = current_command[0], current_command[1]

    if command == "register":
        license_plate_number = current_command[2]
        if username in parking_dict.keys():
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking_dict[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

    elif command == "unregister":
        if username not in parking_dict.keys():
            print(f"ERROR: user {username} not found")
        else:
            parking_dict.pop(username)
            print(f"{username} unregistered successfully")

for user, plate_number in parking_dict.items():
    print(f"{user} => {plate_number}")
