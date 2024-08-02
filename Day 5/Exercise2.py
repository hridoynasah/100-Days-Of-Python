student_scores = [78, 90, 65, 86, 91, 55, 64, 89]
max_score = student_scores[0]

for el in student_scores:
    if max_score < el:
        max_score = el

print(f"Max score is: {max_score}")

# Another way: Using function
max_mark = max(student_scores)
print(f"Max score is: {max_mark}")
