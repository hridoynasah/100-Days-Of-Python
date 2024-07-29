# BMI Calculator 2.0:
print("---Welcome to BMI calculator---")
height = float(input("   Enter your height in m: "))
weight = float(input("   Enter your weight in kg: "))

BMI = weight / (height ** 2)
print("   Your BMI is:", round(BMI, 2))

if BMI <= 18.5:
    print("   You are underweight.")
elif BMI >  18.5 and BMI <= 25:
    print("   You have a normal weight.")
elif BMI > 25 and BMI <= 30:
    print("   You are overweight.")
elif BMI > 30 and BMI <= 35:
    print("   You are obese.")
else:
    print("   You are clinically obese.")

