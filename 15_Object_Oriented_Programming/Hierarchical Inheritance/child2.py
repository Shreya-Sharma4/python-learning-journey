from parent import A


class C(A):
    def __init__(self):
        print("This is class C constructor")
        super().__init__()


c1 = C()