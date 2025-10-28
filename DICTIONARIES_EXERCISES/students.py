student_data = {}
command = input()

while ":" in command:
    data = command.split(":")
    name, id, course = data[0], data[1], data[2]
    if course not in student_data:
        student_data[course] = {}
    student_data[course][id] = name
    command = input()

course = " ".join(command.split("_"))
for key, value in student_data.items():
    if key == course:
        for id, name in value.items():
            print(f"{name} - {id}")
