class Car:
    brand = "BMW"

    def __init__(self, name, model, price, quantity):
        self.name = name
        self.model = model
        self.price = price
        self.quantity = quantity


cars = [
    Car("A", "M2", 100, 8),
    Car("B", "M3", 200, 3),
    Car("C", "M4", 300, 6),
]

total = 0

for car in cars:
    print(Car.brand, car.name, car.model, car.price, car.quantity)
    total += car.price * car.quantity

print("Total Value:", total)