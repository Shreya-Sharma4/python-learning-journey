size = 5

for row in range(size, 0, -1):
    print("* " * row)


print()


for row in range(size, 0, -1):
    for number in range(row):
        print(row, end=" ")
    print()