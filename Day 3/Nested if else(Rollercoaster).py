
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What's your age ? "))

if height > 120:
    print("You can ride.")
    if age < 12:
        bill = 5
        print(f"Child tickets are ${bill}.")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are ${bill}.")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}.")
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == 'Y' or wants_photo == 'y':
        bill += 3
        print(f"Your total bill is: ${bill}")
    else:
        print(f"Your total bill is: ${bill}")
else:
    print("Sorry, you can't ride.")
