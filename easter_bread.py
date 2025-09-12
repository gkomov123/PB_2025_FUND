#Inputs
budget = float(input())
price_flour = float(input())

#Prices
eggs_price = price_flour * 0.75
milk_price_per_l = price_flour * 1.25
milk_price_per_loaf = milk_price_per_l * 0.25

#Cost per loaf
cost_per_loaf = eggs_price + price_flour + milk_price_per_loaf

#Counters
loafes = 0
colored_eggs = 0

#Loop for baking while having budget
while budget >= cost_per_loaf:
    budget -= cost_per_loaf
    loafes += 1

    colored_eggs += 3

     #Every third loaf subtract eggs
    if loafes % 3 == 0:
        colored_eggs -= (loafes - 2)

    
print(f"You made {loafes} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
