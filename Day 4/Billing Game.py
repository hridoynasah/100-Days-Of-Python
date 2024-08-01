import random
names_string = "Sattik,Hridoy,Nasif,Toufiq,Rakib"
name = names_string.split(",")
length = len(name) - 1
random_idx = random.randint(0, length)
print(f"{name[random_idx]} is going to buy the meal today!")
