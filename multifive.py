def get_integer_input(prompt_label):
    while True:
        raw_input_value = input(prompt_label)
        try:
            return int(raw_input_value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
 
 
def main():
    print("MULTIPLE OF 5 CHECKER")
    print("=" * 30)
 
    user_number = get_integer_input("Enter a multiple of 5 between 1 and 100: ")
 
    if 1 <= user_number <= 100 and user_number % 5 == 0:
        print(f"{user_number} is a valid multiple of 5 between 1 and 100.")
    else:
        print(f"{user_number} is not a valid multiple of 5 between 1 and 100.")
 
 
if __name__ == "__main__":
    main()