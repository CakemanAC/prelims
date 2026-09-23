def get_number(prompt_label):
    while True:
        raw_input_value = input(prompt_label)
        try:
            return float(raw_input_value)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def display_menu():
    print("ARITHMETIC CALCULATOR")
    print("1. Addition          2. Subtraction       3. Multiplication")
    print("4. Division          5. Modulus           6. Increment")
    print("7. Decrement")
    print()


def perform_operation(selected_option):
    if selected_option in ("1", "2", "3", "4", "5"):
        x_value = get_number("Enter the value of x: ")
        y_value = get_number("Enter the value of y: ")
        print()
        print(f"Variable Values: x = {x_value}, y = {y_value}")

        if selected_option == "1":
            result_value = x_value + y_value
            print(f"Addition: x + y = {result_value}")
        elif selected_option == "2":
            result_value = x_value - y_value
            print(f"Subtraction: x - y = {result_value}")
        elif selected_option == "3":
            result_value = x_value * y_value
            print(f"Multiplication: x * y = {result_value}")
        elif selected_option == "4":
            if y_value == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result_value = x_value / y_value
                print(f"Division: x / y = {result_value}")
        elif selected_option == "5":
            if y_value == 0:
                print("Error: Modulus by zero is not allowed.")
            else:
                result_value = x_value % y_value
                print(f"Modulus: x % y = {result_value}")

    elif selected_option in ("6", "7"):
        x_value = get_number("Enter the value of x: ")
        print()
        print(f"Variable Values: x = {x_value}")

        if selected_option == "6":
            result_value = x_value + 1
            print(f"Increment: x + 1 = {result_value}")
        elif selected_option == "7":
            result_value = x_value - 1
            print(f"Decrement: x - 1 = {result_value}")

    else:
        print("Invalid option. Please select a number from 1 to 7.")


def main():
    keep_running = True
    while keep_running:
        display_menu()
        selected_option = input("Select an arithmetic operation: ").strip()
        print()
        perform_operation(selected_option)
        print()

        while True:
            user_choice = input("Do you want to continue? (YES/NO): ").strip().upper()
            if user_choice == "YES":
                print()
                keep_running = True
                break
            elif user_choice == "NO":
                keep_running = False
                break
            else:
                print("Invalid input. Please enter YES or NO.")

    print("Program terminated. Thank you!")


if __name__ == "__main__":
    main()