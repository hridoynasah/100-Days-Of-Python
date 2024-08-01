# If the bill was $X.Y, split between 5 people,
# with 10%, 12% or 15% tip.
# How much each person should pay ?
print("---Welcome to tip calculator---")
bill = float(input("   What was the total bill? $"))
tip = int(input("   What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("   How many people to split the bill? "))
tip_percentage = bill * (tip / 100)
total_bill = bill + tip_percentage
each_pay = total_bill / split
each_pay = round(each_pay, 2)
bill = input(f"   Each person have to pay: ${each_pay}")
