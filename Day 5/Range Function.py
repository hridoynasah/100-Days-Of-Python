# Range function:
# range(start, end, steps)
# It start form starting point and finishes in less than ending point.
# Type 1: by default start from zero and increases by 1
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()

# Type 2:
for i in range(0, 5):
    print(i, end=" ")   # 0 1 2 3 4
print()

# Type 2:
for i in range(3, 5):
    print(i, end=" ")   # 3 4
print()

# Type 3:
for i in range(1, 11, 3):
    print(i, end=" ")
