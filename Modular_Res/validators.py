"""Input validation helpers."""
from config import MENU


def ask_yes_no(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        print("  >> Invalid input. Please type 'yes' or 'no'.")


def get_valid_item():
    while True:
        item_input = input("Enter menu item: ").strip()
        for menu_item in MENU:
            if menu_item.lower() == item_input.lower():
                return menu_item
        print("  >> Item not found on the menu. Please check spelling and try again.")


def get_valid_quantity():
    while True:
        qty_input = input("Enter quantity: ").strip()
        if qty_input.isdigit() and int(qty_input) > 0:
            return int(qty_input)
        print("  >> Invalid quantity. Please enter a positive whole number.")