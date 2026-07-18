students = [
    ["Shreya", 85],
    ["Rahul", 92],
    ["Anjali", 78]
]

highest_marks = students[0]

for student in students:
    if student[1] > highest_marks[1]:
        highest_marks = student

print(f"Top Student: {highest_marks[0]}")
print(f"Marks: {highest_marks[1]}")