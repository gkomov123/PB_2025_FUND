products = {}
command = input()

while command != 'buy':
    name, price, quantity = command.split()
    if name not in products.keys():
        products[name] = []
        products[name].append(float(price))
        products[name].append(int(quantity))
    else:
        products[name][1] += int(quantity)
        products[name][0] = float(price)
    command = input()

for product_name, price_list in products.items():
    total_price = price_list[0] * price_list[1]
    print(f"{product_name} -> {total_price:.2f}")
