students = {
    "101": {"name": "Shreya", "marks": 85},
    "102": {"name": "Rahul", "marks": 92},
    "103": {"name": "Anjali", "marks": 78}
}

highest_marks = 0
top_student = ""

for roll_number in students:
    if students[roll_number]["marks"] > highest_marks:
        highest_marks = students[roll_number]["marks"]
        top_student = students[roll_number]["name"]

print(f"Top Student: {top_student}")
print(f"Marks: {highest_marks}")