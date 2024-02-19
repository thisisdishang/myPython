# Python program to create computer accessory dictionary and replace dictionary value if price is less than 500

computer_accessories = {
    'mouse': 500,
    'keyboard': 200,
    'headphone': 300,
    'moniter': 100,
    'printer': 450}

print(computer_accessories)

for a, price in computer_accessories.items():
    if price < 500:
        computer_accessories[a] = "price lower than 500"  # type: ignore

print(computer_accessories)