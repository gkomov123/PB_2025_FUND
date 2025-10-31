phonebook = {}

while True:
    command = input()
    if "-" not in command:
        break

    name, number = command.split("-")
    phonebook[name] = number

searches = int(command)
for search in range(searches):
    searched_name = input()
    if searched_name in phonebook.keys():
        number = phonebook[searched_name]
        print(f"{searched_name} -> {number}")
    else:
        print(f"Contact {searched_name} does not exist.")
