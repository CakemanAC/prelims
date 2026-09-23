def get_positive_amount(prompt_label):
    while True:
        raw_input_value = input(prompt_label)
        try:
            amount_value = float(raw_input_value)
        except ValueError:
            print("Invalid input. Please enter a numeric amount.")
            continue
        if amount_value < 0:
            print("Invalid input. Amount cannot be negative.")
            continue
        return amount_value


def main():
    print("PURCHASE PAYMENT CALCULATOR")
    print("=" * 35)

    first_item_cost = get_positive_amount("Enter the cost of the first item: $")
    second_item_cost = get_positive_amount("Enter the cost of the second item: $")
    total_cost = first_item_cost + second_item_cost

    payment_amount = get_positive_amount("Enter your payment amount: $")

    print()
    print(f"Total cost of items: ${total_cost:.2f}")

    if payment_amount < total_cost:
        amount_owed = total_cost - payment_amount
        print(f"Insufficient payment. You still owe ${amount_owed:.2f}.")
    else:
        change_amount = payment_amount - total_cost
        print(f"Thank you for your payment! Your change is ${change_amount:.2f}.")


if __name__ == "__main__":
    main()