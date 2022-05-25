"""
Instructions
In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap()
so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return
False if it is not a leap year.

You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

days_in_month(year=2022, month=2)
And it will use this information to work out the number of days in the month, then return that as the output, e.g.:

28
The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year
has 29 days in February.
"""


def is_leap(year_check):
    if (year_check % 4 == 0 and year_check % 100 != 0) or (year_check % 100 == 0 and year_check % 400 == 0):
        return True
    else:
        return False


def days_in_month(year_check, month_check):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    checked_year = is_leap(year_check)
    if checked_year and month_check == 2:
        return 29
    return month_days[month_check - 1]



# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
