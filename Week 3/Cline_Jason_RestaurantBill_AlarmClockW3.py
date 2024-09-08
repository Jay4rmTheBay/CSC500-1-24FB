# File Name: Cline_Jason_RestaurantBill_AlarmClockW3.py

# Author: Jason Todd Cline

# Institution: Colorado State University Global
# Class: CSC500-1
# Term: 24FB
# Module: 3

# Date Created: 09/08/2024
# Last Modified: 09/08/2024


def get_user_input_meal() -> float:
    """
    Get user input for the charge of the food.

    Returns:
        float: The charge for the food.
    """
    try:
        meal_charge = float(input("Enter the charge for the food: "))
        return meal_charge
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_input_meal()


def calculate_meal(meal_charge: float) -> None:
    """
    Calculate the tax, tip, and total amount for the meal.

    Args:
        meal_charge (float): The charge for the food.
    """
    tax = meal_charge * 0.07
    tip = meal_charge * 0.18
    total = meal_charge + tax + tip
    print(f"7% sales tax: ${tax:.2f}")
    print(f"18% tip: ${tip:.2f}")
    print(f"Total amount: ${total:.2f}\n")


def get_user_input_clock() -> tuple[int, int]:
    """
    Get user input for the current time and wait time for the alarm.

    Returns:
        tuple[int, int]: The current time and wait time for the alarm.
    """
    try:
        user_input_time = int(
            input(
                "Enter the time now in hours (11 is 11am and 23 is 11pm, 0 is midnight): "
            )
        )
        user_input_wait_time = int(
            input("Enter the amount of hours to wait for the alarm: ")
        )
        return user_input_time, user_input_wait_time
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_user_input_clock()


def clock(user_input_time: int, user_input_wait_time: int) -> None:
    """
    Calculate the new time after waiting for the specified hours.

    Args:
        user_input_time (int): The current time.
        user_input_wait_time (int): The amount of hours to wait for the alarm.
    """
    new_time = ((user_input_wait_time % 24) + user_input_time) % 24
    print(f"In {user_input_wait_time} hours it will be {new_time:02d}:00")


def main() -> None:
    """
    Main function to run the program.
    """
    user_input_charge = get_user_input_meal()
    calculate_meal(user_input_charge)
    user_input_time, user_input_wait_time = get_user_input_clock()
    clock(user_input_time, user_input_wait_time)


if __name__ == "__main__":
    main()
