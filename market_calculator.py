def print_receipt(cart, total):
    print("\n--- RECEIPT ---")
    for item, (qty, price) in cart.items():
        print(f"{item.title():10} x {qty:<3} @ ${price:.2f} = ${qty*price:.2f}")
    print("-" * 24)
    print(f"{'TOTAL':15} = ${total:.2f}")
    print("-" * 24)

def main():
    prices = {
        'milk': 4.00,
        'meat': 10.00,
        'redbull': 3.99,
        'bread': 2.00
    }
    other_price = 7.99
    cart = {}
    total = 0.0

    print("Welcome to the Market! (type 'done' when finished)\n")
    while True:
        item = input("Enter item name (or 'done'): ").strip().lower()
        if item == "done":
            break
        try:
            qty = float(input(f"How many {'(or kg for meat)'} of {item}? "))
        except ValueError:
            print("Invalid quantity. Try again.")
            continue
        price = prices.get(item, other_price)
        cart[item] = (qty, price)
        total += qty * price

    print_receipt(cart, total)

    # Payment
    while True:
        try:
            paid = float(input("\nEnter amount paid ($): "))
            if paid < total:
                print("Not enough, please enter a higher amount.")
                continue
            break
        except ValueError:
            print("Invalid amount. Try again.")
    change = paid - total
    print(f"Change: ${change:.2f}")

if __name__ == "__main__":
    main()