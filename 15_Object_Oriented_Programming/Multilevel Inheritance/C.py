from B import P


class C(P):
    pqr = "bye"

    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks


obj = C("ram", 21, 90)

print(obj.pqr, obj.xyz, obj.abc)
print(obj.marks, obj.age, obj.name)