year = int(input("Enter a year to check : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is leap year.")
        else:
            print("It isn't leap year.")
    else:
        print("It is a leap year.")

else:
    print("It isn't leap year.")
