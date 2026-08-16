from person import person


class tester(person):
    def __init__(self, name, id, skill, age):
        super().__init__(name, id, skill)
        self.age = age

    def calculate_bonus(self):
        salary = int(input("Enter your salary: "))
        bonus_amount = salary * 0.20
        super().bonus()
        print(bonus_amount)
        print(f"Your salary in this month will be {salary + bonus_amount}")

    def testing(self):
        print("I am a tester and I test software")