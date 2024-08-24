"""
File Name: Cline_Jason_SolutionW1.py

Author: Jason Todd Cline

Institution: Colorado State University Global
Class: CSC500-1
Term: 24FB
Module: 1

Date Created: 08/18/2024
Last Modified: 08/18/2024

Description: 
    This program gets two floats from the user and then
    adds, subtracts, multiply, and divides the two numbers.
    The results are then printed for the user.

"""


class Calculator:
    def __init__(self):
        """
        Initializes the num1 and num2 variables to None.
        """
        self.num1 = None
        self.num2 = None

    def user_input(self):
        """
        Prompts the user to provide two numbers and returns them as a tuple.

        Returns:
            tuple[float, float]: A tuple containing the two numbers provided by the user.
        """
        self.num1 = float(input("Please provide a number: "))
        self.num2 = float(input("Please provide another number: "))
        return self.num1, self.num2

    def calculate_and_print_results(self):
        """
        Prints the results of addition, subtraction, multiplication, and division of two numbers.

        Args:
            num1 (float): The first number.
            num2 (float): The second number.
        """
        self.num1, self.num2 = self.user_input()
        print("Part 1: Addition and Subtraction\n")
        print(f"Addition: {self.add_numbers()}")
        print(f"Subtraction: {self.subtract_numbers()}")
        print("\nPart 2: Multiplication and Division\n")
        print(f"Multiplication: {self.multiply_numbers()}")
        print(f"Division: {self.divide_numbers()}")

    def add_numbers(self):
        """
        Adds two numbers.

        Args:
            num1 (float): The first number.
            num2 (float): The second number.

        Returns:
            float: The sum of the two numbers.
        """
        return self.num1 + self.num2

    def subtract_numbers(self):
        """
        Subtracts two numbers.

        Args:
            num1 (float): The first number.
            num2 (float): The second number.

        Returns:
            float: The difference between the two numbers.
        """
        return self.num1 - self.num2

    def multiply_numbers(self):
        """
        Multiplies two numbers.

        Args:
            num1 (float): The first number.
            num2 (float): The second number.

        Returns:
            float: The product of the two numbers.
        """
        return self.num1 * self.num2

    def divide_numbers(self):
        """
        Divides two numbers.

        Args:
            num1 (float): The first number.
            num2 (float): The second number.

        Returns:
            float: The quotient of the two numbers.

        Raises:
            ZeroDivisionError: If the second number is zero.

        """
        try:
            return self.num1 / self.num2
        except ZeroDivisionError as error:
            print(f"Error: {error}")


def main():
    """
    This function is the entry point of the program.
    It prompts the user for input, calls the user_input function to get two numbers,
    and then calls the calculate_and_print_results function to display the results.
    """
    # Calculator().user_input()
    Calculator().calculate_and_print_results()


if __name__ == "__main__":
    main()
