notes = [""] * 10 # Telling pylance its a list of strings beforehand to avoid a static analysis warning

while True:
    command = input()
    if command == "End":
        break
    current_note = command.split("-")
    importance = int(current_note[0]) - 1
    note = current_note[1]
    # notes[importance] = note Another way to do the insertion
    notes.pop(importance)
    notes.insert(importance, note)
    
result = [note for note in notes if note != ""]
print(result)