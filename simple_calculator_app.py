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
