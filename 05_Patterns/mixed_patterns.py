size = 5

for row in range(size):
    for column in range(size):
        if row == column:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()


print()


for row in range(size):
    for column in range(size):
        if row == column or row + column == size - 1:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()