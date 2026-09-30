# Coffee Management System

menu = {
    1: ("Espresso", 80),
    2: ("Cappuccino", 120),
    3: ("Latte", 100),
    4: ("Cold Coffee", 110),
    5: ("Mocha", 130),
}

cart = []


def show_menu():
    print("\n========== COFFEE MENU ==========")

    for number, item in menu.items():
        name, price = item
        print(f"{number}. {name} - Rs.{price}")

    print("6. Exit")


def add_coffee():
    show_menu()

    choice = int(input("\nEnter coffee number: "))

    if choice == 6:
        return False

    if choice not in menu:
        print("Invalid choice!")
        return True

    quantity = int(input("Enter quantity: "))

    name, price = menu[choice]
    total = price * quantity

    cart.append((name, price, quantity, total))

    print(f"{quantity} {name} added to cart.")
    print(f"Item total: Rs.{total}")

    return True


def generate_bill():
    if len(cart) == 0:
        print("\nYour cart is empty.")
        return

    print("\n====================================")
    print("          COFFEE BILL")
    print("====================================")

    grand_total = 0

    for item in cart:
        name, price, quantity, total = item

        print(f"{name}")
        print(f"Price: Rs.{price} x {quantity} = Rs.{total}")
        print("------------------------------------")

        grand_total += total

    print(f"Grand Total: Rs.{grand_total}")
    print("====================================")
    print("       Thank you for visiting!")
    print("====================================")


# Main Program

print("====================================")
print("       WELCOME TO COFFEE SHOP")
print("====================================")

while True:

    result = add_coffee()

    if result == False:
        break

    more = input("\nDo you want to order more? (yes/no): ")

    if more.lower() == "no":
        break


generate_bill()
