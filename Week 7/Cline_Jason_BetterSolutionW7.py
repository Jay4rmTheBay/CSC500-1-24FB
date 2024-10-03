# File Name: Cline_Jason_PortfolioMilestoneW6.py

# Author: Jason Todd Cline

# Institution: Colorado State University Global
# Class: CSC500-1
# Term: 24FB
# Module: 7


# Date Created: 10/03/2024
# Last Modified: 10/03/2024


def initialize_variables():
    room_nums: dict = {
        "CSC101": 3004,
        "CSC102": 4501,
        "CSC103": 6755,
        "NET110": 1244,
        "COM241": 1411,
    }
    instructors: dict = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee",
    }
    meeting_times: dict = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m.",
    }
    default_message = "Course number not found."
    return room_nums, instructors, meeting_times, default_message


def fetch_input():
    user_input = input("Enter a course number:").upper()
    return user_input


def main():
    room_nums, instructors, meeting_times, default_message = (
        initialize_variables()
    )
    user_input = fetch_input()
    print("Room number:", room_nums.get(user_input, default_message))
    print("Instructor:", instructors.get(user_input, default_message))
    print("Meeting time:", meeting_times.get(user_input, default_message))


if __name__ == "__main__":
    main()
