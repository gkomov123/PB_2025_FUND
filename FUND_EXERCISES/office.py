employees_happines = input().split()
improvement_factor = int(input())


improved_happines = [int(x) * improvement_factor for x in employees_happines]

#avarage_happines = [x for x in multiplied_employee if sum(multiplied_employee) / len(multiplied_employee)]
# filtered = list(filter(lambda x: x >= (sum(employees_) / len(employees_)), employees_))

avarage = sum(improved_happines) / len(improved_happines)
filtered = [x for x in improved_happines if x >= avarage]

if len(filtered) >= len(improved_happines) / 2:
    print(f"Score: {len(filtered)}/{len(improved_happines)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(improved_happines)}. Employees are not happy!")