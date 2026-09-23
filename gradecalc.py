def get_valid_score(subject_name):
    while True:
        raw_input_value = input(f"{subject_name} Score: ")
        try:
            score_value = float(raw_input_value)
        except ValueError:
            print("Invalid input. Please enter a numeric score.")
            continue
        if score_value < 0 or score_value > 100:
            print("Invalid input. Score must be between 0 and 100.")
            continue
        return score_value


def determine_letter_grade(average_score):
    if average_score >= 90:
        return "A"
    elif average_score >= 80:
        return "B"
    elif average_score >= 75:
        return "C"
    else:
        return "F"


def main():
    print("STUDENT GRADE CALCULATOR")
    print("=" * 40)

    keep_running = True
    while keep_running:
        java_score = get_valid_score("Java Programming")
        c_score = get_valid_score("C Programming")
        database_score = get_valid_score("Database Handling")

        average_score = (java_score + c_score + database_score) / 3
        letter_grade = determine_letter_grade(average_score)

        print()
        print(f"Average: {average_score:.2f}")
        print(f"Grade: {letter_grade}")
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