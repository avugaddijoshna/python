menu = {
    "Idli": 30,
    "Dosa": 40,
    "Vada": 25,
    "Poori": 35,
    "Tea": 10
}

print("WELCOME TO PYTHON RESTAURANT")
print("----------------------------")
print("Menu Card")

for item, price in menu.items():
    print(f"{item:<10} - ₹{price}")

print("----------------------------")
print("Thank you! Visit again 😊")

