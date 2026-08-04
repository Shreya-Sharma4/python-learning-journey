from engine import Engine


class Car:
    def __init__(self, horsepower):
        self.age = 90
        self.engine = Engine(horsepower)

    def car_details(self):
        print(self.engine.show_engine())
        return f"Car Age: {self.age}"


car = Car(200)

print(car.age)
print(car.engine.name)
print(car.engine.horsepower)
print(car.engine.brand)
print(car.car_details())