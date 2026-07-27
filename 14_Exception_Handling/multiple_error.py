print("start")

try:
    numbers = [10, 20]
    print(numbers[1])
    print(10 / 0)
    print(10 / "a")
except Exception as error:
    print(error)
finally:
    print("I will always execute")

print("program end")