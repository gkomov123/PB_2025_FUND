year = int(input())

# While the condition is True run
while True:
    year += 1 # adds +1 to the year every iteration
    year_string = str(year) #converts year from int to str

    if len(set(year_string)) == len(year_string): # checks if the unique chars in year are the length of the year 
        break

print(year)