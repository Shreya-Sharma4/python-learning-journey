size = 5

for row in range(1, size + 1):
    print("* " * row)


print()


for row in range(1, size + 1):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()