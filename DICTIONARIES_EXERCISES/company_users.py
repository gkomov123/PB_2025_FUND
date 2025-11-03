company_employees = {}

while True:
    command = input()

    if command == "End":
        break

    company_name, company_id = command.split(" -> ")

    if company_name not in company_employees.keys():
        company_employees[company_name] = []

    if company_id not in company_employees[company_name]:
        company_employees[company_name].append(company_id)

for company, id_list in company_employees.items():
    print(company)
    for id in id_list:
        print(f"-- {id}")
