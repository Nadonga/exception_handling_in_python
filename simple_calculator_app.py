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
