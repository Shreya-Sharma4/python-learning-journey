number = 24

print(f"Factors of {number}:")

for factor in range(1, number + 1):
    if number % factor == 0:
        print(factor)