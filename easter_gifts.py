gifts_list = input().split()

while True:
    command = input() #Command input
    if command == "No Money": #Listen for a specific command if said break while loop
        break

    command_parts = command.split() # Split the command 
    action = command_parts[0] # Set the action index required for if checks to a variable

    if action == "OutOfStock":
        gift_part = command_parts[1] # Set the gift part of the command to a variable for later use
        for i in range(len(gifts_list)): # Iterate thru the gifts in the list
            if gifts_list[i] == gift_part: # If gift name is the same as the gift we are looking for replace with NONE
                gifts_list[i] = "None"
            
    elif action == "Required":
        gift_part = command_parts[1] # Set the gift part of the command to a variable for later us
        index_part = int(command_parts[2]) # Set the index part of the command to a variable
        if 0 <= index_part < len(gifts_list): #Check if the index from the index part is valid
            gifts_list[index_part] = gift_part

    elif action == "JustInCase":
        gift_part = command_parts[1]
        if gifts_list: #Checks if list is not empty
            gifts_list[-1] = gift_part # If list not empty replace last gift in the list with the given one
    
result = []
for g in gifts_list: #Iterate thru the gift list
    if g != "None": #If gift is not None then append to result
        result.append(g)

print(" ".join(result)) #Print result