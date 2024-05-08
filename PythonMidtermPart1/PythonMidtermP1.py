# Andrew Sy
# Midterm Part 1

def display_menu():
    """Display the food menu with options and prices."""
    menu = {
        1: ("De Anza Burger...", 5.25),
        2: ("Bacon Cheese...", 5.75),
        3: ("Mushroom Swiss...", 5.95),
        4: ("Western Burger...", 5.95),
        5: ("Don Cali Burger...", 5.95)
    }
    print("Menu:")
    for option, (item, price) in menu.items():
        print(f"{option}. {item}: ${price:.2f}")

def get_order():
    """Get user's order and quantity."""
    order = {}
    while True:
        choice = input("Enter the number of the item you want (or '6' to exit): ").strip()
        if choice == '6':
            return None
        elif not choice.isdigit() or int(choice) not in range(1, 6):
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        else:
            quantity = input(f"How many {menu[int(choice)][0]} do you want? ").strip()
            if not quantity.isdigit() or int(quantity) < 1:
                print("Invalid quantity. Please enter a positive integer.")
                continue
            order[int(choice)] = int(quantity)
            another = input("Do you want to order anything else? (yes/no): ").strip().lower()
            if another != "yes":
                return order

def calculate_price(order):
    """Calculate the total price of the order."""
    total_price = sum(menu[item][1] * quantity for item, quantity in order.items())
    return total_price

def apply_tax(total_price, user_type):
    """Apply tax based on user type."""
    if user_type == "student":
        return total_price
    elif user_type == "staff":
        tax = total_price * 0.09
        return total_price + tax
    else:
        return "Invalid user type."

def display_bill(order, total_price, user_type):
    """Display the bill including item details, total before tax, tax amount, and total price after tax."""
    print("Bill:")
    for item, quantity in order.items():
        item_name, price = menu[item]
        print(f"{item_name}: {quantity} x ${price:.2f} = ${price * quantity:.2f}")
    print(f"Total before tax: ${total_price:.2f}")
    if user_type == "staff":
        tax = total_price * 0.09
        print(f"Tax amount: ${tax:.2f}")
        total_price += tax
    print(f"Total price after tax: ${total_price:.2f}")

def main():
    """Main function to run the program."""
    display_menu()
    order = get_order()
    if order is None:
        print("Thank you, hope to see you again!")
        return
    user_type = input("Are you a student or a staff? ").strip().lower()
    total_price = calculate_price(order)
    total_price_with_tax = apply_tax(total_price, user_type)
    display_bill(order, total_price, user_type)

if __name__ == "__main__":
    menu = {
        1: ("De Anza Burger...", 5.25),
        2: ("Bacon Cheese...", 5.75),
        3: ("Mushroom Swiss...", 5.95),
        4: ("Western Burger...", 5.95),
        5: ("Don Cali Burger...", 5.95)
    }
    main()
