user_points_dict = {}
submissions_dict = {}

while True:
    current_result = input().split("-")

    if len(current_result) == 1:
        break  # exam finished command

    elif len(current_result) == 2:  # "user-banned" command
        user = current_result[0]
        del user_points_dict[user]

    else:
        name, course, points = current_result[0], current_result[1], int(current_result[2])
        if name not in user_points_dict.keys():
            user_points_dict[name] = 0
        if points > user_points_dict[name]:
            user_points_dict[name] = points
        if course not in submissions_dict.keys():
            submissions_dict[course] = 0
        submissions_dict[course] += 1

print("Results:")
for username, points in user_points_dict.items():
    print(f"{username} | {points}")
print("Submissions:")
for language, submissions_count in submissions_dict.items():
    print(f"{language} - {submissions_count}")
