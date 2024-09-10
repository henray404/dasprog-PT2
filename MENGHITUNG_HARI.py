

def leap_check(year):

    if (year % 400 == 0) and (year % 100 == 0):
        return True

    elif (year % 4 == 0) and (year % 100 != 0):
        return True

    else:
        return False


def calculate_date(day, month, year):

    month_number = {
        "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12
    }
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month_number_value = month_number.get(month, None)

    # Handle invalid month input
    if month_number_value is None:
        return "Invalid month entered."

    # Adjust February's days for leap years
    if leap_check(year):
        days_in_month[1] = 29

    # Calculate the day number by summing the days of previous months and adding the current day
    day_number = sum(days_in_month[:month_number_value - 1]) + day

    return day_number


day, month, year = input("input date: ").split(" ")
day = int(day)
month = month.lower()
year = int(year)

print(leap_check(year))
print(calculate_date(day, month, year))
