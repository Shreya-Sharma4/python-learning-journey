students = {
    "101": {
        "name": "Shreya",
        "marks": 85
    },
    "102": {
        "name": "Rahul",
        "marks": 92
    }
}

for roll_number in students:
    print(f"Roll No: {roll_number}")
    print(f"Name: {students[roll_number]['name']}")
    print(f"Marks: {students[roll_number]['marks']}")