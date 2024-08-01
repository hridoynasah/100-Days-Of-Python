# BMI - Body Mass Index
# BMI calculator :
# BMI = weight(kg)/(height)^2 (m^2)
height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))
BMI = weight // (height**2)
print("Your BMI is:", int(BMI))

