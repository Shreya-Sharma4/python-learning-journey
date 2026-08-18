from GP import GP


class P1(GP):
    def __init__(self, name, age, **kwargs):
        super().__init__(name, **kwargs)
        self.age = age