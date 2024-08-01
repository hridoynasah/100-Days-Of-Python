import random
names_string = input("Give everybody's names, separated by a comma: ")
name = names_string.split(",")
length = len(name) - 1
random_choice = random.randint(0, length)
print(f"{name[random_choice]} is going to buy the meal today!")




