stock = {}

while True:
    command = input()

    if command == "statistics":
        break

    product, quantity = command.split(": ")
    quantity = int(quantity)

    if product in stock.keys():
        stock[product] += quantity
    else:
        stock[product] = quantity

count_all_products = len(stock.keys())
sum_all_quantities = sum(stock.values())

print("Products in stock:")
for product, quantity in stock.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {count_all_products}")
print(f"Total Quantity: {sum_all_quantities}")
