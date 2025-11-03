force_users_dict = {}

while True:
    command = input()

    if command == "Lumpawaroo":
        break

    if "|" in command:
        force_side, force_user = command.split(" | ")
        force_user_part_of_the_force = False

        for force_user_list in force_users_dict.values():
            if force_user in force_user_list:
                force_user_part_of_the_force = True
                break

        if not force_user_part_of_the_force:
            if force_side not in force_users_dict.keys():
                force_users_dict[force_side] = []
            force_users_dict[force_side].append(force_user)

    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        for list_with_force_users in force_users_dict.values():
            if force_user in list_with_force_users:
                list_with_force_users.remove(force_user)
                break

        if force_side not in force_users_dict.keys():
            force_users_dict[force_side] = []
        force_users_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for force_side, list_with_force_users in force_users_dict.items():
    if list_with_force_users:
        print(f"Side: {force_side}, Members: {len(list_with_force_users)}")
        for force_user in list_with_force_users:
            print(f"! {force_user}")
