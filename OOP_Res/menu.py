"""Menu display."""
from config import MENU, RESTAURANT_NAME


def display_menu():
    print("=" * 46)
    print(f"{RESTAURANT_NAME:^46}")
    print(f"{'MENU':^46}")
    print("=" * 46)
    print(f"{'ITEM':<25}{'PRICE (PHP)':>21}")
    print("-" * 46)
    for item, price in MENU.items():
        print(f"{item:<25}{price:>18.2f}")
    print("=" * 46)