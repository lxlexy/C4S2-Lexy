"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates.

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'.
2. scheduled_date (string): The scheduled date to compare, in the same format.

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today.
- Assume the dates are in the same year.
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""

from datetime import datetime

def remove_ordinal_suffix(date_str):
    return ''.join([char for char in date_str if not char.isdigit()]) + ''.join([char for char in date_str if char.isdigit()])

def date_passed(todays_date, scheduled_date):
    # Remove ordinal suffix and convert the dates to datetime objects
    todays_date = remove_ordinal_suffix(todays_date)
    scheduled_date = remove_ordinal_suffix(scheduled_date)
    format_str = "%d %B"
    todays_date_dt = datetime.strptime(todays_date, format_str)
    scheduled_date_dt = datetime.strptime(scheduled_date, format_str)

    # Compare the two dates
    if todays_date_dt > scheduled_date_dt:
        print("The scheduled date has passed.")
    elif todays_date_dt < scheduled_date_dt:
        print("The scheduled date is yet to pass.")
    else:
        print("The scheduled date is today.")

# Example usage
date_passed("26th March", "25th March")  # Scheduled date has passed
date_passed("24th March", "25th March")  # Scheduled date is yet to pass
date_passed("25th March", "25th March")  # Scheduled date is today
