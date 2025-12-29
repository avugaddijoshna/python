menu = {
    "Idli": 30,
    "Dosa": 40,
    "Tea": 10
}

total = 0
while True:
    item = input("Enter item name (or 'done'): ").title()
    if item == "Done":
        break
    if item in menu:
        qty = int(input("Enter quantity: "))
        total += menu[item] * qty
    else:
        print("Item not available")

print("Total Bill: ₹", total)
