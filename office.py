employees = input().split()
improvement_factor = int(input())


employees_ = [int(x*improvement_factor) for x in employees]

#avarage_happines = [x for x in multiplied_employee if sum(multiplied_employee) / len(multiplied_employee)]
filtered = list(filter(lambda x: x >= (sum(employees_) / len(employees_)), employees_))

if len(filtered) >= len(employees_) / 2:
    print(f"Score: {len(filtered)}/{len(employees_)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees_)}. Employees are not happy!")