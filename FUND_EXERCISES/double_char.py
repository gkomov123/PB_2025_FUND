
result = ""

while True:

    command = input()

    if command == "End":
        break

    if command == "SoftUni":
        continue

    doubled = ""
    for char in command:
        doubled += char * 2

    result += doubled + "\n"

print(result.strip())