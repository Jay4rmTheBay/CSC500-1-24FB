# File Name: Cline_Jason_Rainfall.py

# Author: Jason Todd Cline

# Institution: Colorado State University Global
# Class: CSC500-1
# Term: 24FB
# Module: 5

# Date Created: 09/16/2024
# Last Modified: 09/16/2024


def get_rainfall_data() -> list:
    """
    Prompts the user to enter the number of years and the inches of rainfall for each month of each year.

    Returns:
        list containing the inches of rainfall for each month.
    """
    rainfall = []
    num_years = int(input("Enter the number of years: "))
    months_per_year = 12
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    for year in range(1, num_years + 1):
        for month in range(1, months_per_year + 1):
            inches_rainfall = int(
                input(
                    f"Enter the inches of rainfall for {months[month]} of year {year}: "
                )
            )
            rainfall.append(inches_rainfall)
    return rainfall


def display_rainfall_results(rainfall: list[int]) -> None:
    """
    Display the rainfall results.

    Args:
        rainfall (list[int]): A list of rainfall measurements.

    Returns:
        None

    Prints the number of months, total inches of rainfall, and average rainfall per month for the entire period.
    """
    num_months = len(rainfall)
    total_inches = sum(rainfall)
    print(f"Number of months: {num_months}")
    print(f"Total inches of rainfall: {total_inches} inches")
    try:
        print(
            f"Average rainfall per month for the entire period: {total_inches / num_months:.2f} inches"
        )
    except ZeroDivisionError:
        print("You have entered zero. Skipping to part 2...")
        pass


def bookstore() -> None:
    """
    Calculates the number of points earned based on the number of books purchased.

    Returns:
        None
    """
    # Part 2: CSU Global Bookstore
    num_books = int(input("How many books have you purchased this month?: "))
    if num_books <= 1:
        print(f"You have earned 0 points for purchasing at least 0 books.")
    elif num_books > 1 and num_books <= 3:
        print(f"You have earned 5 points for purchasing at least 2 books.")
    elif num_books > 3 and num_books <= 5:
        print(f"You have earned 15 points for purchasing at least 4 books.")
    elif num_books > 5 and num_books <= 7:
        print(f"You have earned 30 points for purchasing at least 6 books.")
    else:
        print(f"You have earned 60 points for purchasing 8 or more books.")


def main() -> None:
    """
    Main function that calculates average rainfall and bookstore points.

    This function prompts the user to enter the number of years and the inches of rainfall for each month
    in those years. It then calculates the total number of months, total inches of rainfall, and the average
    rainfall per month for the entire period. If the user enters zero for the number of years, it skips to
    the second part of the function.

    In the second part, the function prompts the user to enter the number of books purchased in a month.
    Based on the number of books purchased, it determines the number of points earned by the user.

    Returns:
    None
    """
    # Part 1: Average Rainfall Over User Desired Years
    rainfall = get_rainfall_data()
    display_rainfall_results(rainfall)

    # Part 2: CSU Global Bookstore
    bookstore()


if __name__ == "__main__":
    main()
