class Demo:
    institute = "LinkCode"

    @classmethod
    def greet(cls):
        return "Hello Students!"

    @classmethod
    def update_institute(cls, new_name):
        cls.institute = new_name


print(Demo.greet())
print(Demo.institute)

Demo.update_institute("OpenAI Academy")

print(Demo.institute)