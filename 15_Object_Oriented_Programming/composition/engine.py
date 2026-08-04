class Engine:
    brand = "XYZ"

    def __init__(self, horsepower):
        self.name = "V8"
        self.horsepower = horsepower

    def show_engine(self):
        return (
            f"Brand: {self.brand}\n"
            f"Engine: {self.name}\n"
            f"Horsepower: {self.horsepower}"
        )