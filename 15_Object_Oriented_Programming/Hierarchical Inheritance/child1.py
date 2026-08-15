from parent import A


class B(A):
    def __init__(self):
        print("This is class B constructor")
        super().__init__()


c1 = B()