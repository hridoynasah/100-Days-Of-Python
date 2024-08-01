import random
names_string = "Sattik,Hridoy,Nasif,Toufiq,Rakib"
nameList = names_string.split(",")
will_pay = random.choice(nameList)

print(f"{will_pay} is going to buy the meal today!")
