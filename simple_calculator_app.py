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

