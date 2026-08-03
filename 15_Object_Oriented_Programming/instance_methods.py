class Student:
    def __init__(self, name, roll_no, age):
        self.name = name
        self.roll_no = roll_no
        self.age = age

    def welcome(self):
        return "Welcome!"

    def update_name(self, new_name):
        old_name = self.name
        self.name = new_name
        print(f"{old_name} -> {self.name}")


student = Student("Ram", 101, 20)

print(student.name)
print(student.welcome())

student.update_name("Shyam")