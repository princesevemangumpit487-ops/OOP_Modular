"""Restaurant Ordering System - Modular Version (run this file)."""
from config import RESTAURANT_NAME
from menu import display_menu
from validators import ask_yes_no
from order import take_order, calculate_order
from receipt import print_receipt


def main():
    print("Welcome to " + RESTAURANT_NAME + "!\n")
    display_menu()

    if not ask_yes_no("\nWould you like to place an order?"):
        print("\nThank you for visiting. Goodbye!")
        return

    order_list = take_order()
    senior_pwd = ask_yes_no("\nAre you a Senior Citizen or PWD?")
    summary = calculate_order(order_list, senior_pwd)
    print_receipt(order_list, summary)


if __name__ == "__main__":
    main()