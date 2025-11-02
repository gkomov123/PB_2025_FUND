student_grades = {}
pair_of_rows = int(input())

for row in range(pair_of_rows):
    student_name = input()
    student_grade = float(input())

    if student_name not in student_grades.keys():
        student_grades[student_name] = []
    student_grades[student_name].append(student_grade)

for student, grade_list in student_grades.items():
    average_grade = sum(grade_list) / len(grade_list)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
