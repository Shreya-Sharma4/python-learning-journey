from parent import p


class c(p):
    def abc(self):
        print("child abc")

    def sound(self):
        print("child sound")

    def add(self, a, b, c):
        return a + b + c

    def add_parent(self, a, b):
        return super().add(a, b)