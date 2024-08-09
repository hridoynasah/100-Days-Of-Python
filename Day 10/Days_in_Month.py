def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    return False

def days_in_month(year, month):
    if month > 12 or month < 1:
        print("Invalid month.")
        return
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = isLeapYear(year)
    index = month - 1
    if leap_year and month == 2:
        return 29
    else:
        return days_in_month[index]

year = int(input("Enter year: "))
month = int(input("Enter month: "))

days = days_in_month(year, month)
print(days)
