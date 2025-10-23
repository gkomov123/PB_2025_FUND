product_input = input()
quantity_input = int(input())

def price_calculator(product:str, quantity:int):
    if product == "coffee":
        return quantity * 1.50
    elif product == "water":
        return quantity * 1.00
    elif product == "coke":
        return quantity * 1.40
    elif product == "snacks":
        return quantity * 2.00
    
result = price_calculator(product_input, quantity_input)
print(f"{result:.2f}")