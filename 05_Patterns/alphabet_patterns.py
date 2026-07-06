size = 5

for row in range(size):
    character = chr(65 + row)
    print(f"{character} " * size)


print()


character = 65

for _ in range(size):
    for _ in range(size):
        print(chr(character), end=" ")
        character += 1
    print()