size = 5

for row in range(1, size + 1):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()


print()


value = 1

for row in range(1, size + 1):
    for _ in range(row):
        print(value, end=" ")
        value += 1
    print()