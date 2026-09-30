"""Order taking and calculation."""
from config import MENU, DISCOUNT_THRESHOLD, DISCOUNT_RATE, SENIOR_PWD_RATE
from validators import ask_yes_no, get_valid_item, get_valid_quantity


def take_order():
    order_list = []
    while True:
        item = get_valid_item()
        qty = get_valid_quantity()
        order_list.append({"item": item, "qty": qty, "price": MENU[item]})
        print(f"  >> Added: {qty} x {item}")
        if not ask_yes_no("Would you like to order another item?"):
            break
    return order_list


def calculate_order(order_list, senior_pwd=False):
    subtotal = 0.00
    for entry in order_list:
        subtotal += entry["price"] * entry["qty"]

    discount_rate = 0.00
    discount_label = "None"

    if senior_pwd:
        discount_rate = SENIOR_PWD_RATE
        discount_label = "Senior/PWD Discount (20%)"
    elif subtotal >= DISCOUNT_THRESHOLD:
        discount_rate = DISCOUNT_RATE
        discount_label = "Bulk Order Discount (10%)"

    discount_amount = subtotal * discount_rate
    total = subtotal - discount_amount

    return {
        "subtotal": subtotal,
        "discount_label": discount_label,
        "discount_amount": discount_amount,
        "total": total,
    }