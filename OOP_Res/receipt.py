"""Receipt printing."""
import datetime
from config import RESTAURANT_NAME, RESTAURANT_ADDRESS


def print_receipt(order_list, summary):
    now = datetime.datetime.now()

    print("\n")
    print("=" * 46)
    print(f"{RESTAURANT_NAME:^46}")
    print(f"{RESTAURANT_ADDRESS:^46}")
    print("=" * 46)
    print(f"Date: {now.strftime('%Y-%m-%d'):<20}Time: {now.strftime('%H:%M:%S')}")
    print("-" * 46)
    print(f"{'QTY':<5}{'ITEM':<23}{'PRICE':>8}{'TOTAL':>10}")
    print("-" * 46)

    for entry in order_list:
        line_total = entry["price"] * entry["qty"]
        print(f"{entry['qty']:<5}{entry['item']:<23}{entry['price']:>8.2f}{line_total:>10.2f}")

    print("-" * 46)
    print(f"{'Subtotal:':<34}{summary['subtotal']:>12.2f}")
    if summary["discount_amount"] > 0:
        print(f"{summary['discount_label']:<34}-{summary['discount_amount']:>11.2f}")
    print(f"{'TOTAL:':<34}{summary['total']:>12.2f}")
    print("=" * 46)
    print(f"{'Thank you for ordering with us!':^46}")
    print(f"{'Please come again!':^46}")
    print("=" * 46)