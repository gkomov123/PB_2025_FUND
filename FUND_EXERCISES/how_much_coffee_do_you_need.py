
coffee_count = 0

while True:

    command = input()

    if command == "END":
        break

    if command == "coding":
        coffee_count += 1
    elif command == "CODING":
        coffee_count += 2
    elif command == "cat":
        coffee_count += 1
    elif command == "CAT":
        coffee_count += 2
    elif command == "dog":
        coffee_count += 1
    elif command == "DOG":
        coffee_count += 2
    elif command == "movie":
        coffee_count += 1
    elif command == "MOVIE":
        coffee_count += 2

if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)
    
    
    

        



