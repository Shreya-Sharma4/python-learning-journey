size = 5

for row in range(size):
    for column in range(size):
        if (
            row == 0
            or row == size - 1
            or column == 0
            or column == size - 1
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()