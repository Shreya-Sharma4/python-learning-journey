class Student:
    college = "PRMCEAM"

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Shreya", 21)

print(Student.college)
print(student.name)
print(student.age)
