def add_numbers(first_number, second_number):
    return first_number + second_number


def subtract_numbers(first_number, second_number):
    return first_number - second_number


def multiply_numbers(first_number, second_number):
    return first_number * second_number


def divide_numbers(first_number, second_number):
    if second_number == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return first_number / second_number


def get_user_numbers():
    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
        return first_number, second_number
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return None, None


def choose_operation():
    print("\nChoose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    user_choice = input("Enter choice (1-4): ")
    return user_choice


def run_calculator():
    while True:
        user_choice = choose_operation()

        if user_choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Try again.")
            continue

        first_number, second_number = get_user_numbers()

        if first_number is None:
            continue

        try:
            if user_choice == "1":
                result = add_numbers(first_number, second_number)
            elif user_choice == "2":
                result = subtract_numbers(first_number, second_number)
            elif user_choice == "3":
                result = multiply_numbers(first_number, second_number)
            elif user_choice == "4":
                result = divide_numbers(first_number, second_number)

            print("Result:", result)

        except ZeroDivisionError as error_message:
            print("Error:", error_message)

        try_again = input("\nDo you want to try again? (yes/no): ").lower()

        if try_again != "yes":
            print("Thank you!")
            break


run_calculator()