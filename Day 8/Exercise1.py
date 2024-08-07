# Area Calculator:
"""
One can of paint can cover 5 square meter.
Given a random height and width of wall,
calculate how many cans of paint you'll need to buy.
Find area first.
"""
import math
def Calculate_Can(height, width, area_cover):
    can = (height * width) / area_cover
    can = math.ceil(can)
    print(f"Number of can are need is {can}")

h = int(input("Height of wall: "))
w = int(input("Weight of wall: "))
coverage = 5
Calculate_Can(height=h, width=w, area_cover=coverage)


