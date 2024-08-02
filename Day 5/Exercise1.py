student_height = [180, 124, 165, 173, 189, 169, 146]
total = 0
for el in student_height:
    total += el

average = total / len(student_height)
print(round(average))

# Using function :
total_height = sum(student_height)
average_height = total_height / len(student_height)
print(f"Average height : {round(average_height)}")

