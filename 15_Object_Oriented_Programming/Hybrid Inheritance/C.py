from P1 import P1
from P2 import P2


class C(P1, P2):
    def __init__(self, name, age, marks, city):
        super().__init__(name=name, age=age, marks=marks)
        self.city = city


obj = C("ram", 21, 99, "pune")

print(obj.name, obj.age, obj.marks, obj.city)