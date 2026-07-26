print("start")

try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as error:
    print(error)

print("program end")