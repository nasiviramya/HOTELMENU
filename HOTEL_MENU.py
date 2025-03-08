# RESTAURANT MENU
menu = {
    'Appetizers': {
        'Momos': 90,
        'Garlic Bread': 100,
        'French Fries': 110,
        'Spring Rolls': 120
    },
    'Main Course': {
        'Pizza': 180,
        'Pasta': 150,
        'Grilled Chicken': 200,
        'Paneer Tikka': 190,
        'Fried Rice': 140,
        'Noodles': 140
    },
    'Desserts': {
        'Cake': 160,
        'Ice Cream': 90,
        'Brownie': 130,
        'Hot Chocolate': 100
    },
    'Beverages': {
        'Coffee': 80,
        'Milkshake': 120,
        'Lemonade': 90,
        'Iced Tea': 100
    }
}

# GREET
print("Welcome to OUR Restaurant!\n")

# DISPLAY MENU....
print("----- Restaurant Menu -----\n")
for category, items in menu.items():
    print(f"{category}:\n")
    for item, price in items.items():
        print(f"{item} - Rs.{price}")
    print("\n")  # New line for spacing

# ORDER PLACEMENT
order_total = 0

# Convert all items to lowercase for case-insensitive matching
menu_items = {item.lower(): (category, item, price) for category, items in menu.items() for item, price in items.items()}

while True:
    item_input = input("Enter your order: ").strip().lower()  
    if item_input in menu_items:
        category, original_item, price = menu_items[item_input] 
        order_total += price
        print(f'Your item "{original_item}" from {category} has been added to your order.')
    else:
        print(f'Sorry, "{item_input}" is not available yet.')

    another_order = input('Do you want to add another item? (YES/NO): ').strip().lower()
    if another_order != 'yes':
        break

# PRINT TOTAL AMOUNT
print(f"\nTotal amount to pay: Rs.{order_total}")
