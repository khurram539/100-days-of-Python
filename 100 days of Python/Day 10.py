# Day 10 - Python Functions with Outputs

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
format_name("Mikey", "Mouse")

# leap year calculator

def is_leap(year):
    """Return True if year is a leap year, False if not."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    """Return number of days in that month in that year."""
    if month > 12 or month < 1:
        return "Invalid Month"
    if is_leap(year) and month == 2:
        return 29
    if not is_leap(year) and month == 2:
        return 28
    if month in [4, 6, 9, 11]:
        return 30
    return 31
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)