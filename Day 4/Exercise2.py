row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map_map = [row1, row2, row3]
# Enter two digits number :
position = input("Where do you want to put the treasure? ")
row = int(position[1]) - 1
column = int(position[0]) - 1
map_map[row][column] = "X"
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
