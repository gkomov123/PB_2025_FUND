journal_of_items = input().split(", ")

inventory = [some_item for some_item in journal_of_items]

while True:
    command_input = input()
    if command_input == "Craft!":
        break
    else:
        command, item = command_input.split(" - ")

    if command == "Collect":
        if item not in inventory:
            inventory.append(item)

    if command == "Drop":
        if item in inventory:
            inventory.remove(item)

    if command == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in inventory:
            index = inventory.index(old_item)
            inventory.insert(index + 1, new_item)

    if command == "Renew":
        if item in inventory:
            index = inventory.index(item)
            removed = inventory.pop(index)
            inventory.append(removed)

print(*inventory, sep=", ")
