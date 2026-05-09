#Simple Calculator by Yael Nadonga

import random


class BasicCalculator:

    def add_numbers(self, first_number, second_number):
        return first_number + second_number

    def subtract_numbers(self, first_number, second_number):
        return first_number - second_number

    def multiply_numbers(self, first_number, second_number):
        return first_number * second_number

    def divide_numbers(self, first_number, second_number):

        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return first_number / second_number


class AdvancedCalculator(BasicCalculator):

    def power_numbers(self, first_number, second_number):
        return first_number ** second_number

    def modulo_numbers(self, first_number, second_number):
        return first_number % second_number


class FunCalculator(AdvancedCalculator):

    def math_quiz(self):

        print("\n=== MATH QUIZ ===")

        number1 = random.randint(1, 10)
        number2 = random.randint(1, 10)

        user_answer = int(input(f"What is {number1} + {number2}? "))

        if user_answer == number1 + number2:
            print("Correct!")
        else:
            print("Wrong!")
            print("Correct answer is:", number1 + number2)


def display_banner():

    print("===================================")
    print("   Simple Calculator by Yael Nadonga")
    print("===================================")
    print("CALC-X v1.0")
    print("Developed by Yael Nadonga")
    print("===================================")


def display_menu():

    print("\n====== CALCULATOR MENU ======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulo")
    print("7. Math Quiz")
    print("8. Exit")


def get_two_numbers():

    try:

        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        return first_number, second_number

    except ValueError:

        print("Invalid input.")
        return None, None


def run_calculator():

    calculator = FunCalculator()
    history = []

    display_banner()

    while True:

        display_menu()

        user_choice = input("Enter choice: ")

        try:

            if user_choice == "1":

                first_number, second_number = get_two_numbers()
                if first_number is None:
                    continue

                result = calculator.add_numbers(first_number, second_number)
                print("Result:", result)

                history.append(f"{first_number} + {second_number} = {result}")

            elif user_choice == "2":

                first_number, second_number = get_two_numbers()
                if first_number is None:
                    continue

                result = calculator.subtract_numbers(first_number, second_number)
                print("Result:", result)

                history.append(f"{first_number} - {second_number} = {result}")

            elif user_choice == "3":

                first_number, second_number = get_two_numbers()
                if first_number is None:
                    continue

                result = calculator.multiply_numbers(first_number, second_number)
                print("Result:", result)

                history.append(f"{first_number} * {second_number} = {result}")

            elif user_choice == "4":

                first_number, second_number = get_two_numbers()
                if first_number is None:
                    continue

                result = calculator.divide_numbers(first_number, second_number)
                print("Result:", result)

                history.append(f"{first_number} / {second_number} = {result}")

            elif user_choice == "5":

                first_number, second_number = get_two_numbers()
                if first_number is None:
                    continue

                result = calculator.power_numbers(first_number, second_number)
                print("Result:", result)

                history.append(f"{first_number} ^ {second_number} = {result}")

            elif user_choice == "6":

                first_number, second_number = get_two_numbers()
                if first_number is None:
                    continue

                result = calculator.modulo_numbers(first_number, second_number)
                print("Result:", result)

                history.append(f"{first_number} % {second_number} = {result}")

            elif user_choice == "7":

                calculator.math_quiz()

            elif user_choice == "8":

                print("\n===== HISTORY =====")

                for item in history:
                    print(item)

                print("\nGoodbye!")
                break

            else:

                print("Invalid choice.")

        except ZeroDivisionError as error:
            print("Error:", error)


run_calculator()