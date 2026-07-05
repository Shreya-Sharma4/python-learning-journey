size = 5

for row in range(1, size + 1):
    spaces = " " * (size - row)
    stars = "* " * row
    print(spaces + stars)