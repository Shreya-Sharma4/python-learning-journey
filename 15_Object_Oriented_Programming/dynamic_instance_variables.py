class Mobile:
    def __init__(self, name, brand, color, price):
        self.name = name
        self.brand = brand
        self.color = color
        self.price = price


mobile1 = Mobile("iPhone 15", "Apple", "Black", 100000)
mobile2 = Mobile("Galaxy S25", "Samsung", "Blue", 85000)

print(mobile1.name, mobile1.brand, mobile1.price)
print(mobile2.name, mobile2.brand, mobile2.price)