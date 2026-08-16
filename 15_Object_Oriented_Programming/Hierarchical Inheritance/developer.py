from person import person


class developer(person):
    def __init__(self, name, id, skill, age):
        super().__init__(name, id, skill)
        self.age = age

    def calculate_bonus(self):
        salary = int(input("Enter your salary: "))
        bonus_amount = salary * 0.15
        super().bonus()
        print(bonus_amount)
        print(f"Your salary in this month will be {salary + bonus_amount}")

    def development(self):
        print("I am a developer and I develop software")