print("start")

try:
    numbers = [10, 20]
    print(numbers[9])
except IndexError as error:
    print(error)

print("program end")