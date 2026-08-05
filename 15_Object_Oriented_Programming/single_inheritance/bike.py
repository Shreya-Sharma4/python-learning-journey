from vehicle import Vehicle


class Bike(Vehicle):
    def __init__(self, color, price, fuel_type, brand):
        self.color = color
        self.price = price
        super().__init__(fuel_type, brand)

    def ride(self):
        return "Bike rides fast"

    def custom_start(self):
        print(super().start())
        return "BHRRRR..."


bike = Bike("Black", 5000, "Petrol", "BMW")

print(bike.color)
print(bike.fuel_type)
print(bike.custom_start())
print(bike.ride())
print(bike.stop())