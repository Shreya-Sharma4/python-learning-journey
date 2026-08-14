class person:
    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age

    def display_personal_details(self):
        print("===== Personal Details =====")
        print(f"Name: {self.name} Age: {self.age} City: {self.city}")