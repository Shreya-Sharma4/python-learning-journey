from parent import Person


class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def study(self):
        print("Studying Python")


student = Student("Shreya", 101)

print(student.name)
print(student.roll_no)
student.greet()
student.study()

print(Student.mro())