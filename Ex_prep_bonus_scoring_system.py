from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
student_number_of_lectures = 0

for student in range(number_of_students):
    current_student_attendances = int(input())
    current_student_bonus = ceil((current_student_attendances / number_of_lectures) * (5 + additional_bonus))
    if current_student_bonus > max_bonus:
        max_bonus = current_student_bonus
    if current_student_attendances > student_number_of_lectures:
        student_number_of_lectures = current_student_attendances

print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {student_number_of_lectures} lectures.")
