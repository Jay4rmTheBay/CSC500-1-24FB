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


def user_input() -> tuple[float, float]:
    """
    Prompts the user to provide two numbers and returns them as a tuple.

    Returns:
        tuple[float, float]: A tuple containing the two numbers provided by the user.
    """
    num1 = float(input("Please provide a number: "))
    num2 = float(input("Please provide another number: "))
    print()
    return num1, num2


def calculate_and_print_results(num1: float, num2: float) -> None:
    """
    Prints the results of addition, subtraction, multiplication, and division of two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
    """
    print("Part 1: Addition and Subtraction\n")
    print(f"Addition: {add_numbers(num1, num2)}")
    print(f"Subtraction: {subtract_numbers(num1, num2)}")
    print("\nPart 2: Multiplication and Division\n")
    print(f"Multiplication: {multiply_numbers(num1, num2)}")
    print(f"Division: {divide_numbers(num1, num2)}")


def add_numbers(num1: float, num2: float) -> float:
    """
    Adds two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return num1 + num2


def subtract_numbers(num1: float, num2: float) -> float:
    """
    Subtracts two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The difference between the two numbers.
    """
    return num1 - num2


def multiply_numbers(num1: float, num2: float) -> float:
    """
    Multiplies two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The product of the two numbers.
    """
    return num1 * num2


def divide_numbers(num1: float, num2: float) -> float | None:
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
        return num1 / num2
    except ZeroDivisionError as error:
        print(f"Error: {error}")
        # return None


def main() -> None:
    """
    This function is the entry point of the program.
    It prompts the user for input, calls the user_input function to get two numbers,
    and then calls the calculate_and_print_results function to display the results.
    """
    num1, num2 = user_input()
    calculate_and_print_results(num1, num2)


if __name__ == "__main__":
    main()
