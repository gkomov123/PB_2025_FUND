courses = {}

while True:
    command = input()

    if command == "end":
        break

    course_name, student_name = command.split(" : ")
    if course_name not in courses.keys():
        courses[course_name] = []
    courses[course_name].append(student_name)

for course, student_list in courses.items():
    print(f"{course}: {len(student_list)}")
    for student in student_list:
        print(f"-- {student}")
