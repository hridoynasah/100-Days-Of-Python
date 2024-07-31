import random
import My_Module
random_integer = random.randint(1, 5)
print(random_integer)
print(My_Module.module)
random_float = random.random()
print(random_float)
# How to get decimal number between 0 and 5?
new_random_float = random_float * random_integer
print(round(new_random_float, 2))
