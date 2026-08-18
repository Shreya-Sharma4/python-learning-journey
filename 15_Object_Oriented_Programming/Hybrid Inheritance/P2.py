from GP import GP


class P2(GP):
    def __init__(self, name, marks, **kwargs):
        super().__init__(name, **kwargs)
        self.marks = marks